from flask import Flask, request, jsonify
import g4f
import sys

app = Flask(__name__)

@app.route('/chat_completion', methods=['POST'])
def chat_completion():
    data = request.get_json()

    if 'content' not in data or 'provider' not in data:
        return jsonify({"error": "Missing 'content' or 'provider' in the request"}), 400

    content = data['content']
    pname = data['provider']

    llm = getattr(getattr(getattr(sys.modules[__name__], "g4f"), "Provider"), pname)

    model = "gpt-3.5-turbo"

    if not llm.supports_gpt_35_turbo:
        model = "gpt-4"

    response = g4f.ChatCompletion.create(
        model=model,
        provider=llm,
        messages=[{"role": "user", "content": content}],
    )

    if response.strip() == '':
        raise Exception('Empty result')

    return jsonify({"response": response})

@app.route('/working_providers', methods=['GET'])
def working_providers():
    working_providers_list = [
        provider.__name__
        for provider in g4f.Provider.__providers__
        if provider.working
    ]

    return jsonify({"working_providers": working_providers_list})

if __name__ == '__main__':
    app.run(debug=True)
