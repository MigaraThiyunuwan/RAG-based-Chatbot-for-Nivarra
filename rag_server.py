from flask import Flask, request, jsonify
from RagLlm import response_

app = Flask(__name__)

@app.route('/rag', methods=['POST'])
def rag_api():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = response_(question)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(port=8000)
