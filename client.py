from openai import OpenAI
client = OpenAI(
    
)
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role":"system","content":"You are a virtual Assistant named Siri"},
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message)