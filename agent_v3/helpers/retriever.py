from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings import OpenAIEmbeddings


class Retriever:
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

    def __init__(self, conn_string: str, collection: str):
        self.collection = collection
        self.conn_string = conn_string
        self.store = PGVector(
            collection_name=self.collection,
            connection_string=conn_string,
            embedding_function=self.embeddings,
        )

    def get_docs(self, query: str, k=5, fetch_k=10) -> str:
        result = self.store.max_marginal_relevance_search(query, k=k, fetch_k=fetch_k)
        return result
