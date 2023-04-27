import openai
openai.api_key = "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"

text_input = input("Please enter some text: ")

prompt = text_input
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=9,
  temperature=0.5
)

print(response.choices[0].text)
