import json
from tools.paths import AVAILABLE_OPTION_PATH
from LLM.llama3_groq import call_llm as call_llm_groq
from LLM.gpt_openai import call_llm as call_llm_openai
from LLM.claude_opr import call_llm as call_llm_claude

# ✅ LLM 이름 → 함수 매핑
LLM_MAP = {
    "groq": call_llm_groq,
    "openai": call_llm_openai,
    "claude": call_llm_claude,
    "openrouter": call_llm_claude,
}

def get_available_llms():
    """ available_option.json에서 사용 가능한 LLM 목록 반환 """
    if not AVAILABLE_OPTION_PATH.exists():
        return []
    with open(AVAILABLE_OPTION_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return [llm.lower() for llm in data.get("LLM", [])]

def call_llm(prompt: str, llm_name: str, temperature: float = 0.6) -> str:
    """
    LLM 이름에 따라 자동으로 적절한 call_llm 함수 연결
    """
    key = llm_name.lower()

    if key not in get_available_llms():
        raise ValueError(f"❌ available_option.json에 정의되지 않은 LLM입니다: {llm_name}")

    for name, func in LLM_MAP.items():
        if name in key:
            return func(prompt, llm_name, temperature)

    raise ValueError(f"❌ 지원하지 않는 LLM: {llm_name}")

# 🔁 q_gen.py 호환성 유지용 export
generate_by_llm = call_llm
