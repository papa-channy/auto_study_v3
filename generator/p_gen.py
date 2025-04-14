# 📁 generator/p_gen.py

import os
from tools.paths import PROMPT_DIR, RECENT_EX_DIR

def load_recent_examples(tool):
    """자유형 문제 예시 불러오기 (최대 3개)"""
    path = os.path.join(RECENT_EX_DIR, f"ex_{tool}.txt")
    if not os.path.exists(path):
        return "# 예시 없음"

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        return "\n".join(lines[-3:]) if lines else "# 예시 없음"

def format_freestyle_prompt(tool, dataset_list, difficulty_list, count, examples):
    dataset_line = ", ".join(dataset_list)
    difficulty_line = ", ".join(difficulty_list)

    prompt = f"""아래 조건에 따라 {tool.upper()} 학습에 적합한 문제를 {count}개 생성해 주세요.

📊 사용 데이터셋: {dataset_line}
🎯 난이도 범위: {difficulty_line}
📝 문제는 한국어로 작성해 주세요.
❗ 형식은 자유롭게 구성하되, 실무에서 접할 수 있는 자연스러운 질문으로 구성해주세요.

---

📌 최근 예시:
{examples}
"""
    return prompt

def update_prompt_templates(tool_list, dataset_list, difficulty_map, count):
    """자유형 프롬프트 생성"""
    for tool in tool_list:
        prompt_path = os.path.join(PROMPT_DIR, f"p_{tool}.txt")
        difficulty_list = difficulty_map.get(tool, [])

        examples = load_recent_examples(tool)
        content = format_freestyle_prompt(tool, dataset_list, difficulty_list, count, examples)

        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"📄 [{tool}] 자유형 프롬프트 생성 완료 → {os.path.basename(prompt_path)}")
