## Phase 1: Foundations (MVP)
*Objective: Build a stable, testable core pipeline.*

| # | Task | Detailed Objective |
| :--- | :--- | :--- |
| **1** | Project Init | Establish directory structure (`src/`, `data/`, `logs/`) and configure `git` to ignore system/environment files. |
| **2** | Pydantic Schema | Define `RealEstateLead` class; enforce type safety (int/str) and semantic constraints (e.g., `budget_min` < `budget_max`). |
| **3** | Logger Setup | Implement a centralized `logger` that logs events to both console and a rotating `project.log` file for observability. |
| **4** | Base Ingestion | Build a script that opens a local file (e.g., `leads_raw.json`), reads the payload, and outputs raw data for verification. |
| **5** | Firewall Logic | Integrate the Pydantic model into the ingestion flow to catch and block malformed data before it reaches processing. |
| **6** | ChromaDB Init | Configure a persistent ChromaDB instance in your local environment to handle vector storage. |
| **7** | Embedding Test | Implement a utility to convert text snippets into high-dimensional vectors (using a local embedding model). |
| **8** | Database Upsert | Create a function to convert the `RealEstateLead` object into a vector and store it in ChromaDB with associated metadata. |
| **9** | Vector Retrieval | Write a query function to retrieve the "top K" most similar leads from ChromaDB to verify storage integrity. |
| **10** | Agent Shell | Build a LangGraph graph with a `START`, a `process_node`, and an `END` to define the agent's movement. |
| **11** | Ollama Connection | Establish an API client connection to your local Ollama instance to perform LLM inference. |
| **12** | Basic Classification | Pass a validated lead into the LLM; ask it to classify the lead as 'Hot', 'Warm', or 'Cold' based on the schema. |
| **13** | Storage Output | Write a `storage.py` module to export the LLM-classified result object into a structured `results.json` file. |
| **14** | MVP Smoke Test | Execute the full pipeline: Input -> Firewall -> Embed -> Store -> Classify -> Export -> Validate integrity. |

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