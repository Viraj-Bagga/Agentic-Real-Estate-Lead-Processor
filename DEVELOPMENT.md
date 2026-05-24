## Phase 1: Foundations (MVP)
*Objective: Build a stable, testable core pipeline.*

| # | Task | Objective |
| :--- | :--- | :--- |
| 1 | Project Init | Initialize repo, `.gitignore`, and `src/` directory. |
| 2 | Pydantic Schema | Create strict schema for lead data (Name, Budget, Location). |
| 3 | Logger Setup | Configure `project.log` for execution tracking. |
| 4 | Base Ingestion | Parse raw input file and print to terminal. |
| 5 | Firewall Logic | Implement Pydantic validator; reject invalid data. |
| 6 | ChromaDB Init | Initialize local vector database instance. |
| 7 | Embedding Test | Generate vector embeddings for test strings. |
| 8 | Database Upsert | Write validated lead into ChromaDB. |
| 9 | Vector Retrieval | Query DB and retrieve stored lead. |
| 10 | Agent Shell | Setup LangGraph node shell. |
| 11 | Ollama Connection | Connect agent to local Ollama LLM. |
| 12 | Basic Classification | Agent processes lead and classifies intent. |
| 13 | Storage Output | Save agent results to `results.json`. |
| 14 | MVP Smoke Test | Full end-to-end run: Ingest -> Firewall -> Classify -> Store. |

---

## Phase 2: Enterprise Reliability & Integration
*Objective: Scale to production with observability and safety.*

| # | Task | Objective |
| :--- | :--- | :--- |
| 15 | Email API | Setup listeners to trigger ingestion automatically. |
| 16 | Google Forms Webhook | Configure webhook for real-time form data. |
| 17 | Audit Trail | Create `audit_log` DB table for decision logging. |
| 18 | Circuit Breaker | Build fault monitoring; trigger 'Hold' state on failure. |
| 19 | Redis State Store | Implement session persistence for lead context. |
| 20 | HITL Checkpoint | Integrate "Human-in-the-Loop" for high-value leads. |
| 21 | LangSmith | Instrument LangGraph for real-time observability. |
| 22 | Dockerization | Create `Dockerfile` and `docker-compose.yml`. |
| 23 | Cloud Deployment | Deploy to AWS/Render for 24/7 uptime. |
| 24 | Semantic Cache | Upgrade to Redis-backed semantic caching. |
| 25 | RLHF Interface | Build feedback loop for "Correct/Incorrect" flagging. |
| 26 | Auto Fine-tuning | Script to update prompts based on feedback data. |
| 27 | Health Dashboard | Visualize lead volume, error rates, and system costs. |