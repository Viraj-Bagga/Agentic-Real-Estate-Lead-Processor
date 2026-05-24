# Agentic Real Estate Lead Processor

## Overview
This project is developed to be an autonomous, agentic system designed to ingest, qualify, and organize real estate leads.

## System Architecture Map
```mermaid
graph TD
    subgraph Ingestion
        A[Email/Forms API] --> B{Pydantic Firewall}
        B -- Failed Validation --> J[Error Log/Hold Bucket]
    end

    subgraph Intelligence
        B -- Validated Lead --> C[Semantic Cache]
        C -- Cache Miss --> D[LangGraph Agent]
        C -- Cache Hit --> I[Fast Output]
        D --> E[(Chroma Vector DB)]
        D --> F[LLM Reasoning]
    end

    subgraph Reliability
        D --> G[Audit Logger]
        D -- Error Detected --> H[Circuit Breaker]
        H -- System Fault --> K[Admin Alert / Queue Hold]
    end

    subgraph Feedback_Loop
        L[Human Correction] --> M[Evaluation Table]
        M --> F
    end

    subgraph Output
        D --> N[CRM/Database Sync]
    end

    style G fill:#bbf,stroke:#333,stroke-width:2px
    style H fill:#fbb,stroke:#333,stroke-width:2px
    style C fill:#dfd,stroke:#333,stroke-width:2px
    style M fill:#ffd,stroke:#333,stroke-width:2px
```
*Explain map later*

## Development Roadmap
This project was developed using a phased, iterative approach, ensuring production grade quality while allowing for agile development. Phase 1 establishes the base of the project, allowing the agent to perform under a limited and monitored scope. This ensures the fundamentals of the projects are implemented accuretly and efficetnly. Phase 2 introduces enterprise-scale resilience, observability, and integration. 

You can see the detailed road map of both phases in [DEVELOPMENT.md](DEVELOPMENT.md).

## Tech Stack
* **Language:** Python
* **Orchestration:** LangGraph
* **Infrence** Ollama (Local LLM)
* **Knowledge** ChromaDB
* **Observability** LangSmith

## Documentation Strategy
I will use a live documentation approach for this project. I will maintain a detailed log to track my decision making process, challenges, and insights. 
