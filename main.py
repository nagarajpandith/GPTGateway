import g4f

response = g4f.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')