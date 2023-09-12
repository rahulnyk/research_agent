from langchain.vectorstores import PGVector


class DocumentStore(PGVector):
    collection_name = 'mahabharat_combined_text'

    def __init__(self, connection_string, embeddings):
        self.connection_string = connection_string
        self.embeddings = embeddings

    def store(self):
        return self(
            collection_name='mahabharat_combined_text',
            connection_string=self.connection_string,
            embedding_function=self.embeddings,
        )
        