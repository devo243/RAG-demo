from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

key = os.environ.get('OPENAI_API_KEY')
print(key)

# os.environ['OPENAI_API_KEY'] = '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'

# documents = SimpleDirectoryReader("data").load_data()
# index = VectorStoreIndex.from_documents(documents)