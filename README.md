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
*I plan to document the whole development lifecycle, from ideation to production*

ADD ROADMAP HERE

## Tech Stack
* **Language:** Python
* **Orchestration:** LangGraph
* **Infrence** Ollama (Local LLM)
* **Knowledge** ChromaDB
* **Observability** LangSmith

## Documentation Strategy
I will use a live documentation approach for this project. I will maintain a detailed log to track my decision making process, challenges, and insights. 
