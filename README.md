# GPT Flask API

A RESTful web service created using the [xtekky/gpt4free](https://github.com/xtekky/gpt4free) library.

```bash
# Clone the repository
git clone https://github.com/nagarajpandith/gpt-flask.git

# Navigate to the project directory
cd gpt-flask

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip3 install -r requirements.txt
```

Create a .flaskenv file and fill the API_KEY var.

```bash
python3 index.py
```

## Local Usage

1. Using `curl`

```bash
curl -X POST -H "Content-Type: application/json" -d '{"content": "YOUR_PROMPT", "provider": "PROVIDER_NAME", "api_key":"API_KEY_HERE"}' http://127.0.0.1:5000/chat_completion
```

2. Using Any API testing platform like Postman, Thunder client etc.

- Endpoint: http://127.0.0.1:5000/chat_completion
- Body Example:

```json
{
  "content": "YOUR_PROMPT",
  "provider": "PROVIDER_NAME",
  "api_key": "API_KEY_HERE"
}
```

> **Note**
> If you want to use the Hosted API, it's live at [https://gpt-flask.onrender.com](https://gpt-flask.onrender.com/). For the API key, email me at [nagaraj.pandith2002@gmail.com](mailto:nagaraj.pandith2002@gmail.com).
