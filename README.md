# 🩺 HEALTHCARE CHATBOT using Hugging Face Transformers
This project demonstrates how to build a domain-specific customer support chatbot for healthcare using the T5 model from Hugging Face Transformers. The model is fine-tuned on custom Q&A data and deployed using a Flask-based frontend for real-time interaction.

## 📌 Key Features
✅ Fine-tuned T5 model on domain-specific healthcare Q&A data

✅ Tokenizer and model saved and reused locally

✅ Flask web application with clean UI for interaction

✅ Modular and production-ready code

✅ Model served in real-time with inference API

## 🧠 Objectives
- Build a domain-specific NLP model for healthcare-related customer queries

- Explore the use of transformer-based models for conversational AI

- Enable real-time interaction using a Flask web server

- Deploy the model in a lightweight environment suitable for demos and prototyping

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/4e32de1f-5f5f-4a29-9290-9afa42791132)

## 🔧 Technical Stack

| Component  | Technology                                            |
| ---------- | ----------------------------------------------------- |
| Model      | [T5-base](https://huggingface.co/t5-base) Transformer |
| Framework  | Hugging Face Transformers, PyTorch                    |
| Web App    | Flask (Python Microframework)                         |
| UI         | HTML + Bootstrap                                      |
| Deployment | Localhost (can be Dockerized)                         |

## 📊 Dataset & Preprocessing
The dataset consists of healthcare-related question-answer pairs. I used Chatgpt in order to generate specific domain related dataset as following. This contains queries that can be asked by the User which can be general like How to login to the system or it can be spefic related to Finance or health-realted problems faced by the user.

![image](https://github.com/user-attachments/assets/487ed6f5-c30a-4976-86bb-5075867bcefc)

Cleaned and normalized using custom preprocessing routines.

Split into training and validation sets using train_test_split.

## 🏗️ Model Development Pipeline
1. Data Loading & Cleaning
   
- Loaded domain-specific Q&A pairs into a DataFrame

Text preprocessing included:

- Lowercasing

- Special character removal

- Token normalization (optional)

2. Tokenization & Encoding
   
- Used T5Tokenizer from Hugging Face to tokenize inputs.

- Set max sequence lengths and applied padding/truncation.

**Before Tokenization:**
  
  ![image](https://github.com/user-attachments/assets/33e2cfe9-a752-4cc2-8abd-36ae75ce1e8f)

**After Tokenization**

![image](https://github.com/user-attachments/assets/948bb2fa-ce86-4eec-839d-ac167992d62d)

3. Model Training
- Fine-tuned T5ForConditionalGeneration on the prepared dataset.

- Used PyTorch DataLoader for batching.

- Saved the model and tokenizer to ./chatbot_model

The Training and Validation Validation Losses for 6 no. of epochs is as follows:

![image](https://github.com/user-attachments/assets/515b4ccd-d225-4e33-a486-3850f57b1264)

4. Inference Logic
Implemented a chatbot() function to:

- Accept a user query

- Tokenize the input

- Use model.generate() with beam search for better output

- Decode the response into human-readable text

![image](https://github.com/user-attachments/assets/22bb652b-6b5f-436d-aaa3-32f66f35eb3e)

![image](https://github.com/user-attachments/assets/f45c96f8-c503-4976-8fe3-bc5054ae7391)

## 🧪 Evaluation
Performed qualitative evaluation using example prompts.

Calculated BLEU score to compare generated vs. reference responses.

![image](https://github.com/user-attachments/assets/7c96f805-4e27-4f77-8971-c589ed5b7f15)


## 💬 Deployment – Flask Web Application
After training, I wrapped the chatbot functionality into a lightweight Flask web application.

🔁 Flow:
User submits query via HTML form

Flask calls the chatbot inference function

The response is rendered on the same page.

##🧪 Sample Interaction

![image](https://github.com/user-attachments/assets/67402bcb-f48d-405b-8c12-b768b30d6079)

📦 Installation
Clone the repo:

```bash

git clone https://github.com/SachdevaVansh/Healthcare_Chatbot_APP.git
cd Healthcare_Chatbot_APP
```
Create a virtual environment (optional)
```
bash
conda create -p venv python=3.8 -y
```
Activate the virtual environment (if you created it)
```
bash
conda activate venv/
```

Install dependencies:
```
bash

pip install -r requirements.txt
```
Run the app:
```
bash
python main.py
```
## 🔮 Future Improvements

✅ Add streaming/chat history

✅ Improve with attention visualization

✅ Integrate authentication for sensitive usage

✅ Deploy on cloud (AWS/GCP/Heroku)

✅ Expand to multi-turn conversations with RAG/LLMs



