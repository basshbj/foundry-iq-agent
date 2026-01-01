import os
import requests
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.identity import DefaultAzureCredential

credentials = DefaultAzureCredential()

def load_documents_dummy():
  url = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json"
  documents = requests.get(url).json()

  rename_map = {"page_chunk": "chunk", "page_embedding_text_3_large": "contentVector", "page_number": "pageNumber"}

  return [
    {rename_map.get(k, k): v for k, v in doc.items()}
    for doc in documents
  ]

documents = load_documents_dummy()

#from azure.search.documents import SearchIndexingBufferedSender


search_client = SearchClient(os.getenv("AI_SEARCH_ENDPOINT"), os.getenv("AI_SEARCH_INDEX_NAME"), credential=credentials)

for item in documents:
  try:
    search_client.upload_documents(documents=[item])
  except Exception as e:
    print(f"An error occurred: ID: {item['id']} - {e}")

print("Documents uploaded successfully.")