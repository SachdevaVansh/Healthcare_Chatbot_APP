from flask import Flask, request, render_template, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re


#app
app=Flask(__name__)

#load the model and tokenizer 
model= T5ForConditionalGeneration.from_pretrained("chatbot_model")
tokenizer=T5Tokenizer.from_pretrained("chatbot_model")

device=model.device

## Cleaning function
def clean_text(text):
  text=re.sub(r'\r\n',' ',text)
  text=re.sub(r'\s',' ',text)
  text=re.sub(r'<.*?>',' ',text)
  text=text.strip().lower()
  return text

#Chatbot function
def chatbot(query):
  query=clean_text(query)
  input_ids=tokenizer(query,return_tensors="pt",max_length=250, truncation=True)

  inputs={key:value.to(device) for key, value in input_ids.items()}

  outputs=model.generate(
      input_ids["input_ids"],
      max_length=250,
      num_beams=5,
      early_stopping=True
  )

  response=tokenizer.decode(outputs[0] ,skip_special_tokens=True)
  return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat",methods=['POST'])
def chat():
    user_message=request.json.get("message","")

    if not user_message:
        return jsonify({'error':"Message is required"}),400
    response=chatbot(user_message)
    return jsonify({'response':response})


if __name__=="__main__":
    app.run(debug=True)