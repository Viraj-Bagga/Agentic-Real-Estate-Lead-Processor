import chromadb
from pprint import pprint
import polars as ps

client = chromadb.PersistentClient(path="src/chroma_db")

client.get_or_create_collection(name="real_estate_leads")
