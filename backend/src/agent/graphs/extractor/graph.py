"""LangGraph workflow with a single extractor node."""

from __future__ import annotations

from langchain_core.messages import HumanMessage
from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict
from typing import List, Any, Dict
from agent.graphs.extractor.utils import GraphUtils

import logging
logger = logging.getLogger(__name__)


class State(TypedDict):
    business_context: Any
    doc_link: str
    missing_fields: List[str]



async def extractor_node(state: State) -> Dict[str, Any]:

    logger.info("Starting extractor node with state: %s", state)

    doc_content = GraphUtils.doc_loader(state.get('doc_link', ''))

    llm = GraphUtils.get_extractor_llm()

    prompt = GraphUtils.get_information_extraction_prompt()

    chat = [prompt, HumanMessage(content=doc_content)]

    response = await llm.ainvoke(chat)

    missing_fields = GraphUtils.find_missing_fields(response)

    return {'business_context': response, 'missing_fields': missing_fields}


builder = StateGraph(State)

builder.add_node("extractor", extractor_node)
builder.set_entry_point("extractor")
builder.add_edge("extractor", END)

workflow = builder.compile()