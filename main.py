import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=1, max_tokens=7)

print(response.choices[0].text)
