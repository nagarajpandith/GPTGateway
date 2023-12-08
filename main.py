from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

@app.route('/chat_completion', methods=['POST'])
def chat_completion():
    data = request.get_json()

    if 'content' not in data:
        return jsonify({"error": "Missing 'content' in the request"}), 400

    content = data['content']

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.You,
        messages=[{"role": "user", "content": content}],
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
