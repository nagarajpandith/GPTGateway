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

Create an .env file and fill the API_KEY var.

```bash
python3 index.py
```

## Local Usage

1. Using `curl`

```bash
curl -X POST -H "Content-Type: application/json" -d '{"content": "YOUR_PROMPT", "api_key":"API_KEY_HERE", "provider": "PROVIDER_NAME", "stream": false}' http://127.0.0.1:5000/chat_completion
```

2. Using Any API testing platform like Postman, Thunder client etc.

- Endpoint: http://127.0.0.1:5000/chat_completion
- Body Example:

```json
{
  "content": "YOUR_PROMPT",
  "api_key": "API_KEY_HERE",
  "provider": "PROVIDER_NAME",
  "stream": false
}
```

> [!NOTE]
> If you want to use the Hosted API, it's live at [https://gpt-flask.onrender.com](https://gpt-flask.onrender.com/). For the API key, email me at [nagaraj.pandith2002@gmail.com](mailto:nagaraj.pandith2002@gmail.com).

## Available Endpoints

| Endpoint             | Description                                        | Method | Example Body                                                                        |
| -------------------- | -------------------------------------------------- | ------ | ----------------------------------------------------------------------------------- |
| `/chat_completion`   | Generates text using LLM & Model based on Provider | POST   | `{"content": "YOUR_PROMPT", "api_key": "API_KEY_HERE", "provider": "PROVIDER_NAME", "stream": false}` |
| `/working_providers` | Retrieves a list of Working Providers              | GET    | `{}`                                                                                |

> [!TIP]
> The provider and stream parameters are optional. If not provided, the default provider is set to "You" and the default stream is set to true. If stream is set to false, the response will be in direct final output format.

## Providers Testing Results

> Last Tested on 9-12-2023 using "stream"=False

> [!IMPORTANT]  
> If a Provider isn't working, it's probably because it needs special args like auth='cookie' or 'jwt' or the WebDriver fails to connect, as web scraping is needed for most of the providers here or IP address blocking etc. Hence, do not consider the below results as final source of truth. To test it yourself, run `python3 test.py` script.

> [!NOTE]
> To know the Providers and their Models refer [this](https://github.com/xtekky/gpt4free?tab=readme-ov-file#-providers-and-models).

**Status Values**

- **Both:** The provider works successfully on both the local and hosted API.
- **Local:** The provider works successfully only on the local API.
- **Hosted:** The provider works successfully only on the hosted API.
- **None:** The provider did not return a successful response on either the local or hosted API.

| Provider       | Local/Hosted/Both | Average Response Time |
| -------------- | ----------------- | --------------------- |
| AItianhuSpace  | None              | 0.0000                |
| AiChatOnline   | Both              | 1.7481                |
| Bard           | None              | 0.0000                |
| Bing           | Both              | 7.1729                |
| ChatBase       | Both              | 10.5962               |
| ChatForAi      | Local             | 1.6945                |
| Chatgpt4Online | None              | 0.0000                |
| ChatgptAi      | Both              | 4.0908                |
| ChatgptNext    | Both              | 1.5508                |
| DeepInfra      | Both              | 3.6010                |
| FakeGpt        | None              | 0.0000                |
| GPTalk         | None              | 0.0000                |
| GeekGpt        | Local             | 2.3581                |
| GptChatly      | Local             | 20.6423               |
| GptForLove     | None              | 0.0000                |
| GptGo          | Local             | 1.1042                |
| GptTalkRu      | Both              | 1.2230                |
| Hashnode       | Both              | 12.7480               |
| HuggingChat    | None              | 0.0000                |
| Koala          | Local             | 5.4211                |
| Liaobots       | None              | 0.0000                |
| Llama2         | None              | 0.0000                |
| MyShell        | Local             | 9.9238                |
| OnlineGpt      | Both              | 2.1422                |
| OpenaiChat     | None              | 0.0000                |
| PerplexityAi   | Local             | 7.9256                |
| Phind          | Both              | 0.4448                |
| Pi             | Local             | 9.1299                |
| Poe            | None              | 0.0000                |
| Raycast        | None              | 0.0000                |
| RetryProvider  | None              | 0.0000                |
| TalkAi         | Local             | 11.4960               |
| Theb           | None              | 0.0000                |
| ThebApi        | None              | 0.0000                |
| You            | Local             | 1.1193                |
| Yqcloud        | None              | 0.0000                |
