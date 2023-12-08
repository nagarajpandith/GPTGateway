from flask import Flask, request, Response, jsonify
import g4f
import sys

app = Flask(__name__)

def generate_response(model, llm, content):
    response_generator = g4f.ChatCompletion.create(
        model=model,
        provider=llm,
        messages=[{"role": "user", "content": content}],
        stream=llm.supports_stream
    )

    for message in response_generator:
        yield message

@app.route('/chat_completion', methods=['POST'])
def chat_completion():
    data = request.get_json()

    if 'content' not in data or 'provider' not in data:
        return jsonify({"error": "Missing 'content' or 'provider' in the request"}), 400

    content = data['content']
    pname = data['provider']

    try:
        llm = getattr(getattr(getattr(sys.modules[__name__], "g4f"), "Provider"), pname)
    except AttributeError:
        return jsonify({"error": f"Invalid provider: {pname}"}), 400

    model = "gpt-3.5-turbo"

    return Response(generate_response(model, llm, content), mimetype="text/event-stream")

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
