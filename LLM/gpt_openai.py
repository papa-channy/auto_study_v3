import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt: str, llm_name: str) -> str:
    """
    🔧 OpenAI GPT 호출 (gpt-3.5-turbo 사용)
    """
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return res.choices[0].message["content"].strip()
    except Exception as e:
        return f"[OPENAI ERROR] {e}"
