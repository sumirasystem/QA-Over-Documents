from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# Load Your Documents
with open("./documents/state_of_the_union.txt") as f:
    state_of_the_union = f.read()

# Split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_text(state_of_the_union)

# Vectorize the documents and create a retriever
embeddings = OpenAIEmbeddings()

# Here, there will be multiple Vector processing methods, but in this article, I will mention two methods: Chroma and FASS. 
# When using them, you just need to choose one of the two based on your specific needs.
folder_faiss_index = "./db/fass"
folder_chroma_index = "./db/chroma"
type = 'chroma'

if(type == 'chroma'):
    ##### Chroma action
    if(os.path.exists(folder_chroma_index) and any(os.listdir(folder_chroma_index))):
        # Load Chroma index
        db_vector = Chroma(persist_directory=folder_chroma_index)
    else:
        # Save Chroma index
        db_vector = Chroma.from_texts(docs, embeddings, persist_directory=folder_chroma_index, metadatas=[{"source": str(i)} for i in range(len(docs))])
        db_vector.persist()
else:
    ##### FASS action
    if(os.path.exists(folder_faiss_index) and any(os.listdir(folder_faiss_index))):
        # Load the Faiss Index
        db_vector = FAISS.load_local(folder_path = folder_faiss_index, index_name = "faiss_index", embeddings = embeddings)
    else:
        # Save the Faiss Index
        db_vector = FAISS.from_texts(docs, embeddings, metadatas=[{"source": str(i)} for i in range(len(docs))])
        db_vector.save_local(folder_path = folder_faiss_index,index_name="faiss_index")

docsearch = db_vector.as_retriever()

# Perform a search for a document segment, the result will provide the corresponding content based on the question through vectors.
# However, the answer content can be quite lengthy in textual format.
query = "What did the president say about Justice Breyer"
docs = docsearch.get_relevant_documents(query)
print(docs)


# Natural language processing for answer generation
### Types of chain_type: "stuff", "map_reduce", "refine", and "map-rerank" can be chosen based on your specific needs
chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
question = "What did the president say about Justice Breyer"
answer = chain.run(input_documents=docs, question=question)
print(answer)