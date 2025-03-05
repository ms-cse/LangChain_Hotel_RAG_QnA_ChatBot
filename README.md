## LangChain: Hotel Document RAG QnA Chatbot App


### Overview:
- The goal of the chatbot app is to facilitate the customers with the latest information
  about the various services and deals offered by the hotel for their stay.
- This app is a demo created using the LangChain framework and the ChromaDB vector store.
- App is based on the fake data (generated using Gemini model) about a Hotel named 'Ocean Breeze Resort'.
- This app has been implemented in two versions using memory:
  - response chat (V1).
  - streamed chat (V2).


### Dataset:
- Input Data: PDF file provided in the 'data' folder
- Vector Store: Inside 'chroma_db' folder.
- Chat History: SQLite DB file 'hotel_cb_chats.db'


### Implementation Process:
- Follow the Jupyter Notebook to see the implementation process in detail.


### App:
- Inside the 'app' folder.
- Install the necessary packages using 'requirements.txt'
- Set the GROQ_API_KEY in the '.env' file to run the app.


### Tech Stack:
- LangChain
- Groq API
- ChromaDB
- Ollama
- Streamlit
- pypdf
