import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')

hosted_providers_url = "https://gpt-flask.onrender.com/working_providers"
response = requests.get(hosted_providers_url)
providers = response.json().get("working_providers", [])

local_endpoint = "http://127.0.0.1:5000/chat_completion"
hosted_endpoint = "https://gpt-flask.onrender.com/chat_completion"

example_body_base = {
    "content": "Hello!",
    "api_key": API_KEY
}

def test_provider(provider, endpoint):
    example_body = example_body_base.copy()
    example_body["provider"] = provider

    start_time = time.time()

    try:
        response = requests.post(endpoint, json=example_body, timeout=60) 
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"{provider} - Request timed out after 60 seconds")
        return 408, 60
    except requests.exceptions.RequestException as e:
        print(f"{provider} - Request failed with error: {e}")
        return 500, 0

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{provider} - Response Time: {elapsed_time:.4f} seconds - Status Code: {response.status_code}")

    return response.status_code, elapsed_time

markdown_table = "| Provider | Local/Hosted/Both | Average Response Time |\n| -------- | ----------------- | ------------------------------------- |\n"

for provider in providers:
    local_status, local_time = test_provider(provider, local_endpoint)
    hosted_status, hosted_time = test_provider(provider, hosted_endpoint)

    if local_status == 200 and hosted_status == 200:
        status = "Both"
        average_time = (local_time + hosted_time) / 2
    elif local_status == 200:
        status = "Local"
        average_time = local_time
    elif hosted_status == 200:
        status = "Hosted"
        average_time = hosted_time
    else:
        status = "None"
        average_time = 0.0

    markdown_table += f"| {provider} | {status} | {average_time:.4f} | \n"

print(markdown_table)
