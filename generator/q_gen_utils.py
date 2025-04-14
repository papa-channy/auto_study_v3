import os
from tools.paths import PROMPT_DIR

def reset_prompt_file(tool):
    """LLM 프롬프트 사용 후 p_{tool}.txt 초기화"""
    prompt_path = os.path.join(PROMPT_DIR, f"p_{tool}.txt")
    if os.path.exists(prompt_path):
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write("")
        print(f"🧹 프롬프트 파일 초기화 완료 → {os.path.basename(prompt_path)}")
    else:
        print(f"⚠️ 프롬프트 파일 없음: {prompt_path}")
