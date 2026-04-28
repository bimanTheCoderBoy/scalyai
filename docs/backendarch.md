src/
│
├
│
├── api/                       # 🌐 HTTP layer (controllers)
│   ├── deps.py                # dependencies (auth, db)
│   ├── v1/
│   │   ├── routes/
│   │   │   ├── user_routes.py
│   │   │   ├── agent_routes.py
│   │   │   ├── chat_routes.py
│
├── agents/                    # 🤖 LangGraph layer
│   ├── graphs/                # graph definitions
│   │   ├── chat_graph.py
│   │   ├── rag_graph.py
│   │
│   ├── nodes/                 # node functions
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── observer.py
│
│   ├── tools/                 # tools used by agents
│   │   ├── db_tools.py        # calls services (NOT DB directly)
│   │   ├── api_tools.py
│
│   ├── state/                 # graph state schemas
│   │   ├── chat_state.py
│
│   └── agent_manager.py       # wrapper to run graph
│
├── services/                  # 🧠 BUSINESS LOGIC (CORE)
│   ├── user_service.py
│   ├── agent_service.py       # bridge between API & LangGraph
│   ├── chat_service.py
│
├── repositories/              # 🗄️ DB access layer
│   ├── user_repo.py
│   ├── agent_repo.py
│   ├── chat_repo.py
│
├── models/                    # 🧩 SQLAlchemy models
│   ├── user.py
│   ├── agent.py
│   ├── chat.py
│
├── schemas/                   # 📦 Pydantic DTOs
│   ├── user_schema.py
│   ├── chat_schema.py
│
├── db/                        # 🔌 DB setup
│   ├── base.py
│   ├── session.py             # engine + SessionLocal
│   ├── init_db.py
│
├── core/                      # ⚙️ config & shared utils
│   ├── config.py
│   ├── security.py
│   ├── logger.py
│
├── infrastructure/            # external integrations
│   ├── llm/
│   │   ├── openai_client.py
│   ├── vector_db/
│   │   ├── chroma.py
│
├── tests/
│
└── alembic/                   # migrations

Emaple base repo arch:

```
class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get(self, db, id):
        return db.query(self.model).filter(self.model.id == id).first()
```

```
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
```

----
Who Will handle Error?
-> 
Repo → raises technical errors
Service → raises business errors
API → returns HTTP errors
 Example: 
      
  