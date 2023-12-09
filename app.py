from flask import Flask, request, Response, jsonify, render_template, url_for
import g4f
import sys

import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ.get('API_KEY')

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='/favicon.ico')

@app.route('/')
def index():
    return render_template('index.html')

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

    required_params = {'content', 'api_key'}
    missing_params = required_params - set(data.keys())

    if missing_params:
        error_msg = f"Missing parameters: {', '.join(missing_params)}"
        return jsonify({"error": error_msg}), 400

    content = data['content']
    pname = data.get('provider', 'Bing')  # Use 'Bing' by default, if not provided
    api_key = data['api_key']
    stream = data.get('stream', True)  # Use True by default, if not provided

    if not api_key == API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    try:
        llm = getattr(getattr(getattr(sys.modules[__name__], "g4f"), "Provider"), pname)
    except AttributeError:
        return jsonify({"error": f"Invalid provider: {pname}"}), 400

    model = "gpt-3.5-turbo"
    if not llm.supports_gpt_35_turbo:
        model = "gpt-4"

    if stream:
        return Response(generate_response(model, llm, content), content_type='text/event-stream', mimetype='text/event-stream')
    else:
        response = g4f.ChatCompletion.create(
            model=model,
            provider=llm,
            messages=[{"role": "user", "content": content}],
        )

        return jsonify(response)

@app.route('/working_providers', methods=['GET'])
def working_providers():
    working_providers_list = [
        provider.__name__
        for provider in g4f.Provider.__providers__
        if provider.working
    ]

    return jsonify({"working_providers": working_providers_list})

if __name__ == '__main__':
    app.run(threaded=True)
