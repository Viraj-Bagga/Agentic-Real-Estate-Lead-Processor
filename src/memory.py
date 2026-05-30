def save_lead(lead, collection, status: str):
    collection.add(
        documents=[lead.raw_message],
        metadatas=[{"email": lead.email, "min": lead.minBudget, "max": lead.maxBudget, "status": status}],
        ids=[lead.email] 
    )
    print("SUCCESS: Lead stored with AI metadata.")