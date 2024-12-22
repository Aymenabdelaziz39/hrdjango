import openai

class LLMHandler:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt, model="gpt-4", max_tokens=150):
        try:
            response = openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Erreur : {str(e)}"
