from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, Document
from llama_index.core.node_parser import SentenceSplitter
import faiss
import numpy as np
import ollama
from pydantic import BaseModel, ValidationError
import os

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 is not installed. Run 'pip install PyPDF2' if you need to extract text from PDFs.")

class ResponseModel(BaseModel):
    description: str  

# Store the conversation history
conversation_history = []

def chat_with_llm(message_list):
    # Keep track of the conversation history
    try:
        response = ollama.chat(
            model='llama3.1',
            messages=message_list
        )
        return response.get("message", {}).get("content", "")
    except Exception as e:
        print("Error during chat_with_llm:", e)
        return "Sorry, I couldn't generate a response."

EMBED_MODEL = 'BAAI/bge-small-en-v1.5'
K = 3  # Retrieve top 3 relevant chunks

Settings.embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL)

docs = []
faiss_index = None

PROMPT_SYS_INITIAL_RESPONSE_2 = """
Imagine you are an assistant that helps users search for detailed information about the Republic of Nivarra, an island located in the southern quadrant of the Elari Ocean. 
You have knowledge about Nivarra geography, culture, politics, history, economy, tourism, healthcare, and more.

Based on the user's input, provide an overview of the relevant details about Nivarra. This could include information on:
- The country's history and political structure
- The local climate, agriculture, and economy
- Key cultural practices, languages, and religions
- Famous landmarks, tourist attractions, and local traditions
- Current news and developments about the island

Here is some context related to the user query:
-----------------------------------------
{context_str}
-----------------------------------------
Considering the above information about Nivarra, answer the user's question clearly and concisely. 
Provide relevant facts, context, and guidance, ensuring the user gains an accurate understanding of Nivarra.

Please keep in mind the following guidelines:
    - Always provide short textual output. Do not respond with code, HTML, or any other format.
    - If the user's query is not related to Nivarra, respond with:
    "I'm an assistant for Nivarra-related information, and I don't know about other fields."
    - Provide an overview including key details about Nivarra, considering its geography, politics, culture, and society.
"""

def init_():
    global docs, faiss_index

    if os.path.exists("data.txt"):
        with open("data.txt", 'r', encoding="utf-8") as file:
            text = file.read()
    else:
        pdf_file_path = "island.pdf"
        text = ""
        if os.path.exists(pdf_file_path):
            with open(pdf_file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        else:
            raise FileNotFoundError("Neither data.txt nor island.pdf was found.")

    
    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    chunks = splitter.split_text(text)
    docs.extend([Document(text=chunk) for chunk in chunks])

    # Create FAISS index with embeddings
    embeddings = np.array([Settings.embed_model._embed(doc.text) for doc in docs])
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss_index = index

    print(f"FAISS index created with {len(docs)} chunks.")

def response_(user_question):
    question_embedding = Settings.embed_model._embed(user_question)
    D, I = faiss_index.search(np.array([question_embedding]), k=K)
    top_docs = [docs[i] for i in I[0]]
    context_str = " ".join([doc.text for doc in top_docs])

    system_prompt = PROMPT_SYS_INITIAL_RESPONSE_2.format(context_str=context_str)

    # Update the message history with the system's context and the user's question
    message_list = conversation_history.copy()
    message_list.append({'role': 'system', 'content': system_prompt})
    message_list.append({'role': 'user', 'content': user_question})

    try:
        # Get response from the LLM
        response = chat_with_llm(message_list)
        
        # Save the response into the history
        conversation_history.append({'role': 'assistant', 'content': response})

        return response
    except Exception as e:
        print("Error during response:", e)
        return "Sorry, I couldn't generate a response."

# Initialize the system
init_()
