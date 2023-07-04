# AI Question Answering over Documents

This repository demonstrates the implementation of an AI question answering system. The system utilizes document loading, text embedding models, vector stores, and retrievers to provide relevant answers to user queries.

## Getting Started

1. Clone the repository: `git clone https://github.com/sumirasystem/QA-Over-Documents.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Download the required language models and embeddings.

## Usage

1. Load your documents: Edit the path in the code to specify the location of your documents.
2. Split the documents into chunks: Adjust the chunk size and overlap as per your requirements.
3. Choose the vector processing method: Select either Chroma or FASS based on your needs.

### Chroma

- Chroma is an NLP system developed by OpenAI that aims to generate high-quality automatic text.
- To use Chroma:
  - Save the Chroma index if it doesn't exist.
  - Load the Chroma index if it already exists.

### FASS

- FASS (Facebook AI Similarity Search) is an AI-based similarity search system developed by Facebook to quickly search for similar texts on a large scale.
- To use FASS:
  - Load the Faiss index if it already exists.
  - Save the Faiss index if it doesn't exist.

4. Perform a search: Provide a query to retrieve relevant documents based on the question.
5. Natural language processing for answer generation: Choose the appropriate `chain_type` based on your requirements.

### Chain Types

- "stuff":
  - This is the default chain_type used for regular language strings.
  - It is simple and does not involve complex processing stages.
  - Suitable for simple tasks that do not require extensive processing.

- "map_reduce":
  - Uses the map and reduce operations to represent language strings.
  - Suitable for tasks that require distributed and parallel processing on multiple data elements.
  - Provides scalability and high performance when dealing with large datasets.

- "refine":
  - This chain_type is used for refining and improving language strings.
  - It involves complex processing stages such as refinement, filtering, and data transformation.
  - Often used in advanced language processing and optimization tasks.

- "map-rerank":
  - Uses the map and rerank operations to process and evaluate the results.
  - Typically used in search tasks, where an initial result list is mapped and then re-evaluated to improve accuracy and performance.
  - Particularly useful in information retrieval tasks and recommendation systems.

6. Run the question answering system: Provide a question and obtain the answer based on the input documents.

## Conclusion

This repository showcases the implementation of an AI question answering system. It demonstrates the process of loading and processing documents, performing searches, and generating answers using different chain types. Feel free to explore and modify the code to suit your specific needs.

Please note that the answer content can be quite lengthy in textual format.

Happy exploring!