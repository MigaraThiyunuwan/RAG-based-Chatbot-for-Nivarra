from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question']
    if user_question:
        try:
            r = requests.post("http://localhost:8000/rag", json={"question": user_question})
            return jsonify(r.json())
        except Exception as e:
            print("Error talking to RAG server:", e)
            return jsonify({"answer": "Sorry, couldn't get a response."})
    return jsonify({"answer": "No question provided."})

if __name__ == "__main__":
    app.run(debug=True)
