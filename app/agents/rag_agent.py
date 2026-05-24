from typing import List

from app.rag.chroma_store import vectorstore


def retrieve_similar_incidents(query: str, k: int = 3) -> List[str]:
    """Return the top-k similar historical incident texts for a query."""
    try:
        docs = vectorstore.similarity_search(query, k=k)
    except AttributeError:
        # Fallback for older/alternate API names
        docs = vectorstore.similarity_search_with_score(query, k=k)
        docs = [doc for doc, _ in docs]

    return [doc.page_content for doc in docs]
