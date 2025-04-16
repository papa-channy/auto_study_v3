# 📁 generator/prompt/p_gen.py

import os
from config.conf_p import (
    prompt_question_generation,
    prompt_enhance_difficulty,
    prompt_enhance_reasoning,
    prompt_extract_tags
)
from tools.paths import PROMPT_DIR


# ─────────────────────────────────────────────
# 🔹 j = a + e : 질문 생성 프롬프트
# ─────────────────────────────────────────────
def generate_prompt_question(kor_tool, dataset_list, difficulty_list, count, examples_str):
    dataset_line = ", ".join(dataset_list)
    difficulty_line = ", ".join(difficulty_list)
    base = prompt_question_generation(kor_tool, dataset_line, difficulty_line, count)
    return f"{base}\n\n📌 최근 예시:\n{examples_str}"

# ─────────────────────────────────────────────
# 🔹 k = f + b : 난이도 강화 프롬프트
# ─────────────────────────────────────────────
def generate_prompt_enhance_difficulty(question: str):
    return prompt_enhance_difficulty(question)

# ─────────────────────────────────────────────
# 🔹 l = g + c : 추론 강화 프롬프트
# ─────────────────────────────────────────────
def generate_prompt_enhance_reasoning(question: str):
    return prompt_enhance_reasoning(question)

# ─────────────────────────────────────────────
# 🔹 n = m + d : 분류 태깅용 프롬프트
# ─────────────────────────────────────────────
def generate_prompt_extract_tags(question: str):
    return prompt_extract_tags(question)

# ─────────────────────────────────────────────
# 💾 저장 유틸
# ─────────────────────────────────────────────
def save_prompt(prompt: str, tool: str, stage: str, mode: str = "temp"):
    """
    mode:
    - temp: 임시 파일 (p_{tool}_{stage}.txt)
    - persistent: 보존용 로그 (p_{tool}_{stage}_log.txt)
    - split: prompt/{stage}/p_{tool}.txt
    """
    filename = f"p_{tool}_{stage}.txt"

    if mode == "persistent":
        filename = f"p_{tool}_{stage}_log.txt"
        path = os.path.join(PROMPT_DIR, filename)

    elif mode == "split":
        stage_dir = os.path.join(PROMPT_DIR, stage)
        os.makedirs(stage_dir, exist_ok=True)
        path = os.path.join(stage_dir, f"p_{tool}.txt")

    else:  # temp
        path = os.path.join(PROMPT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(prompt)

    print(f"💾 프롬프트 저장 완료 → {filename}")
