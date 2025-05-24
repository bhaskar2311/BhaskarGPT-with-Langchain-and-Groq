# 🦙 BhaskarGPT with Langchain and Groq

An advanced Q&A chatbot application built using **Langchain** and the **Groq LLM API**, powered by the **Meta llama3-70b-8192 model**. Designed for fast, cost-effective inference using cutting-edge open-source models.


## 📌 Features
* Uses the **LLaMA 3 70B model** via **Groq API**
* Real-time Q&A interaction in a Streamlit interface
* Adjustable model settings: temperature, max tokens, and model selection
* Clean, fast, and hosted with secure key management
* Built with Langchain prompt-chaining architecture
  
## 🧠 Technologies Used
* Streamlit
* Langchain
* Groq LLM API
* LLaMA 3 70B model
* `st.secrets` for secure API key handling
* Prompt Engineering with ChatPromptTemplate

## 🌍 Project Structure
```
├── app.py # Main Streamlit app using Groq LLM
├── requirements.txt # All dependencies for environment setup
└── .streamlit/
└── secrets.toml # (you must create this for local use)
```

## ⚙️ Environment Setup
1. Clone the Repo
```
git clone https://github.com/bhaskar2311/BhaskarGPT-with-Langchain-and-Groq
cd BhaskarGPT-with-Langchain-and-Groq
```
2. Create a Virtual Environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Configure Streamlit Secrets
  * Create a file at .streamlit/secrets.toml and add the following:
```
GROQ_API_KEY = "your_groq_api_key"
LANGSMITH_API_KEY = "your_langsmith_api_key"
```
🔐 These values are accessed securely in app.py using st.secrets[]. No .env file is needed.

## 🚀 How to Run
#### 🚀 Live Demo: 
[bhaskargpt.streamlit.app](https://bhaskargpt.streamlit.app/)
```
streamlit run app.py
```
* Select the model (llama3.1) from the sidebar
* Tune temperature and max tokens
* Ask your question in the input field
* Receive instant answers from the LLaMA 3 70B model via Groq

## 📝 Detailed Logic
#### 🔹 app.py – BhaskarGPT with Groq
* Loads API keys from st.secrets[] (no dotenv required)
* Uses ChatGroq model from Langchain integration
* Model: llama3-70b-8192
* Parameters like temperature and max_tokens configurable from sidebar
* Prompt flow:
  ```
  ChatPromptTemplate → ChatGroq (LLM) → StrOutputParser → Response
  ```

## 📦 Reusability
* The requirements.txt is designed for reuse across all LLM projects.
* Secure key handling via Streamlit secrets
* Compatible with LangSmith for tracing/debugging


## 📸 Screenshots
![image](https://github.com/user-attachments/assets/514d591e-258a-424d-9b03-1c08e6c3a3bb)

## 📝 Notes
This project was fully developed by me. The README was written based on my knowledge and experience, with support from generative AI tools to refine its structure and presentation.

## 📄 License
This project is open source and available under the MIT License.

## 🙋‍♂️ Author
Made with ❤️ by Bhaskar Shivaji Kumbhar









