import openai

openai.api_key = "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"

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": 
             "Write me a script for hosting a \
             conference on technology"}]
)

# Print out the whole output dictionary
print(output)

# Get the output text only
print(output['choices'][0]['message']['content'])