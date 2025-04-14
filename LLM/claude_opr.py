def call_llm(prompt: str, llm_name: str) -> str:
    """
    🔧 OpenRouter 기반 Claude LLM 호출
    """
    return f"[{llm_name} 응답] {prompt}"