import chromadb

collection = client.get_or_create_collection(name="real_estate_leads")

def save_lead(lead: Lead, collection):

    collection.add(
        documents=[lead.raw_message],
        metadatas=[{"email": lead.email, "min": lead.minBudget, "max": lead.maxBudget}],
        ids=[lead.email] 
    )
    print("SUCCESS: Lead stored in Vector Database.")