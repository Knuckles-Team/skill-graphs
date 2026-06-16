# Configure Mem0 with Chroma
config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "my_memories",
            "path": "chroma_db",
        }
    }
}
