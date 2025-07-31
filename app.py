from flask import Flask, request, jsonify, render_template
from chatbot import get_response
from database import log_interaction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = get_response(user_input)
    log_interaction(user_input, response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

