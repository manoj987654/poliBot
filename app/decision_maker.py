from openai import OpenAI
client = OpenAI()

def make_decision(structured_query, clauses):
    prompt = f"""Based on these clauses: {clauses} And this query: {structured_query} Decide if the claim is approved or rejected. Provide amount if applicable and justify citing clauses. Respond in JSON with keys: decision, amount, justification."""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return eval(resp.choices[0].message.content)
