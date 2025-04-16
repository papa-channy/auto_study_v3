# 📁 generator/core/q_enhancer.py

from config.conf_p import (
    prompt_enhance_difficulty,
    prompt_enhance_reasoning
)
from LLM.llm_selector import call_llm

def enhance_difficulty(f: list[str], llm_name: str) -> list[str]:
    """
    ✅ 난이도 디테일 강화 (f → g)
    """
    g = []
    for question in f:
        prompt = prompt_enhance_difficulty(question)
        response = call_llm(prompt=prompt, llm_name=llm_name)
        g.append(response.strip())
    return g

def enhance_reasoning(g: list[str], llm_name: str) -> list[str]:
    """
    ✅ 추론 및 응용 강화 (g → h)
    """
    h = []
    for question in g:
        prompt = prompt_enhance_reasoning(question)
        response = call_llm(prompt=prompt, llm_name=llm_name)
        h.append(response.strip())
    return h
