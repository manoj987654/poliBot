from openai import OpenAI
client = OpenAI()

def parse_query(query: str) -> dict:
    prompt = f"""Extract structured details (age, procedure, location, policy duration) from: "{query}" Respond in JSON."""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return eval(resp.choices[0].message.content)
