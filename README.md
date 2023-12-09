# GPTGateway

A RESTful web service created to provide a simple API for generating text using various GPT models based on different providers. Whether you want to integrate chat completion into your application or explore the capabilities of different GPT models, this project has you covered.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/nagarajpandith/GPTGateway)

```bash
# Clone the repository
git clone https://github.com/nagarajpandith/GPTGateway.git

# Navigate to the project directory
cd GPTGateway

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
> If you want to use the Hosted API, it's live at [https://gptgateway.onrender.com](https://gptgateway.onrender.com/). For the API key, email me at [nagaraj.pandith2002@gmail.com](mailto:nagaraj.pandith2002@gmail.com).

## Available Endpoints

| Endpoint             | Description                                  | Method | Example Body                                                                                          |
| -------------------- | -------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
| `/chat_completion`   | Generates text using Model based on Provider | POST   | `{"content": "YOUR_PROMPT", "api_key": "API_KEY_HERE", "provider": "PROVIDER_NAME", "stream": false}` |
| `/working_providers` | Retrieves a list of Working Providers        | GET    | `{}`                                                                                                  |

> [!TIP]
> The provider and stream parameters are optional. If not provided, the default provider is set to "Bing" and the default stream is set to true. If stream is set to false, the response will be in direct final output format.

## Providers Testing Results

> Last Tested on 9-12-2023 using "stream"=False

> [!NOTE]
> To know the Providers and their Models refer [this](https://github.com/xtekky/gpt4free?tab=readme-ov-file#-providers-and-models).

**Status Values**

- **Both:** The provider works successfully on both the local and hosted API.
- **Local:** The provider works successfully only on the local API.
- **Hosted:** The provider works successfully only on the hosted API.
- **None:** The provider did not return a successful response on either the local or hosted API.

### Automated Testing

> [!IMPORTANT]  
> If a Provider isn't working, it's probably because it needs special args like auth='cookie' or 'jwt' or the WebDriver fails to connect, as web scraping is needed for most of the providers here or IP address blocking etc. Hence, do not consider the below results as final source of truth. To test it yourself, run `python3 test.py` script.

| Provider       | Local/Hosted/Both | Average Response Time |
| -------------- | ----------------- | --------------------- |
| AItianhuSpace  | None              | 0.0000                |
| AiChatOnline   | Both              | 1.7414                |
| Bard           | None              | 0.0000                |
| Bing           | Both              | 7.5283                |
| ChatBase       | Both              | 11.0944               |
| ChatForAi      | None              | 0.0000                |
| Chatgpt4Online | None              | 0.0000                |
| ChatgptAi      | Both              | 4.0048                |
| ChatgptNext    | Both              | 1.1684                |
| DeepInfra      | Both              | 2.9104                |
| FakeGpt        | None              | 0.0000                |
| GPTalk         | None              | 0.0000                |
| GeekGpt        | Hosted            | 2.6676                |
| GptChatly      | None              | 0.0000                |
| GptForLove     | None              | 0.0000                |
| GptGo          | Local             | 1.0809                |
| GptTalkRu      | Both              | 1.3263                |
| Hashnode       | Both              | 14.0748               |
| HuggingChat    | None              | 0.0000                |
| Koala          | Local             | 2.3503                |
| Liaobots       | None              | 0.0000                |
| Llama2         | None              | 0.0000                |
| MyShell        | Local             | 9.0187                |
| OnlineGpt      | Both              | 2.3497                |
| OpenaiChat     | None              | 0.0000                |
| PerplexityAi   | Local             | 10.8567               |
| Phind          | Both              | 0.4872                |
| Pi             | Local             | 8.9026                |
| Poe            | None              | 0.0000                |
| Raycast        | None              | 0.0000                |
| RetryProvider  | None              | 0.0000                |
| TalkAi         | Local             | 13.3812               |
| Theb           | None              | 0.0000                |
| ThebApi        | None              | 0.0000                |
| You            | Local             | 1.6147                |
| Yqcloud        | None              | 0.0000                |

### Manual Testing

I tested these providers manually and I find them to be the most reliable & fast ones.

| Provider     | Local/Hosted/Both | Average Response Time |
| ------------ | ----------------- | --------------------- |
| GptTalkRu    | Both              | 2-3s                  |
| GeekGpt      | Both              | 6-8s                  |
| ChatgptAi    | Both              | 5s                    |
| ChatgptNext  | Both              | 7-8s                  |
| AiChatOnline | Local             | 4s                    |
| GptChatly    | Local             | 4-5s                  |
| OnlineGpt    | Local             | 4s                    |
| Bing         | Both              | 15-20s                |
| ChatBase     | Both              | 12-13s                |
| Koala        | Local             | 4s                    |
| GptGo        | Local             | 12s                   |
| You          | Local             | 10s                   |
| MyShell      | Local             | 11s                   |
| Pi           | Local             | 11s                   |
| PerplexityAi | Local             | 14s                   |
| Hashnode     | Both              | 18s                   |
| TalkAi       | Local             | 20s                   |
| DeepInfra    | Both              | 31-47s                |
| Theb         | Local             | 12s                   |

> [!IMPORTANT]
>
> - For GptChatly to work, you need to bypass Cloudflare captcha manually.
> - GptTalkRu does not provide right answers usually. Needs detailed prompts.
