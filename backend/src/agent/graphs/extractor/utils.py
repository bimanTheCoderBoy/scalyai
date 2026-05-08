from langchain_community.document_loaders import PyMuPDFLoader
from typing import get_args, get_origin, Union
from langchain_openai import ChatOpenAI
from .schema import BusinessContext
import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from typing import Any, Dict, List
from pydantic import BaseModel
from .prompts import INFORMATION_EXTRACTION_PROMPT_JSON, CLARIFICATION_PROMPT, MAPPER_PROMPT, SCHEMA_JSON
load_dotenv()

class GraphUtils:

    _extractor_llm = None
    _clarifier_llm = None
    _mapper_llm = None
    _information_extraction_prompt = None

    @staticmethod
    def doc_loader(doc_link: str) -> str:
        docs = PyMuPDFLoader(doc_link).load()

        total_content = "\n".join([doc.page_content for doc in docs])

        return total_content

    @classmethod
    def get_extractor_llm(cls):
        if cls._extractor_llm is None:
            cls._extractor_llm = ChatOpenAI(
                model=os.getenv("MODEL_NAME", "inception/mercury-2"),
                temperature=float(os.getenv("TEMPERATURE", 0.1)),
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url=os.getenv("OPENROUTER_BASE_URL")
            ).with_structured_output(BusinessContext)
        return cls._extractor_llm

    
    @classmethod
    def get_clarifier_llm(cls):
        if cls._clarifier_llm is None:
            cls._clarifier_llm = ChatOpenAI(
                model=os.getenv("MODEL_NAME", "inception/mercury-2"),
                temperature=float(os.getenv("TEMPERATURE", 0.1)),
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url=os.getenv("OPENROUTER_BASE_URL")
            )
        return cls._clarifier_llm

    @classmethod
    def get_mapper_llm(cls):
        if cls._mapper_llm is None:
            cls._mapper_llm = ChatOpenAI(
                model=os.getenv("MAPPER_MODEL_NAME", "openai/gpt-4o-mini"),
                temperature=float(os.getenv("TEMPERATURE", 0.1)),
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url=os.getenv("OPENROUTER_BASE_URL")
            )
        return cls._mapper_llm
    

    @classmethod
    def get_information_extraction_prompt(cls):
        if cls._information_extraction_prompt is None:
            cls._information_extraction_prompt = SystemMessage(content=INFORMATION_EXTRACTION_PROMPT_JSON)
        return cls._information_extraction_prompt
    
    @classmethod
    def get_clarification_prompt(cls, missing_fields: List[str]):
        return SystemMessage(content=CLARIFICATION_PROMPT.format(missing_fields=missing_fields, schema=SCHEMA_JSON))

    @classmethod
    def get_mapper_prompt(cls, user_message: str, missing_fields: List[str], question: str):
        return SystemMessage(content=MAPPER_PROMPT.format(user_input=user_message, schema=SCHEMA_JSON, missing_fields=missing_fields, question=question))

    @classmethod
    def find_missing_fields(cls, business_context: BusinessContext, prefix: str = "") -> List[str]:
        missing_fields = []

        for field_name, field_info in business_context.model_fields.items():
            value = getattr(business_context, field_name, None)

            current_path = f"{prefix}.{field_name}" if prefix else field_name

            if value is None:
                # Check if the field type is a BaseModel subclass — if so, recurse into defaults
                annotation = business_context.model_fields[field_name].annotation
                # unwrap Optional[X]
                origin = get_origin(annotation)
                if origin is Union:
                    args = [a for a in get_args(annotation) if a is not type(None)]
                    if args:
                        annotation = args[0]
                if isinstance(annotation, type) and issubclass(annotation, BaseModel):
                    missing_fields.extend(cls.find_missing_fields(annotation(), current_path))
                else:
                    missing_fields.append(current_path)
            elif isinstance(value, BaseModel):
                missing_fields.extend(cls.find_missing_fields(value, current_path))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, BaseModel):
                        missing_fields.extend(cls.find_missing_fields(item, prefix=f"{current_path}[{i}]"))
        
        return missing_fields

    @staticmethod
    def update_missing_fields(missing_fields: List[str], updates: Dict[str, Any]):
         return [f for f in missing_fields if f not in updates]

    @staticmethod
    def _set_nested_value(model, path: str, value):
        keys = path.split(".")
        obj = model
        for key in keys[:-1]:
            child = getattr(obj, key, None)
            if child is None:
                field_type = obj.model_fields[key].annotation
                # Unwrap Optional[X] → X
                origin = get_origin(field_type)
                if origin is Union:
                    args = [a for a in get_args(field_type) if a is not type(None)]
                    if args:
                        field_type = args[0]
                child = field_type()
                setattr(obj, key, child)
            obj = child
        setattr(obj, keys[-1], value)

    @staticmethod
    def apply_updates(business_context: BusinessContext, updates: Dict[str, Any]):
        for field_path, value in updates.items():
            GraphUtils._set_nested_value(business_context, field_path, value)

        return business_context