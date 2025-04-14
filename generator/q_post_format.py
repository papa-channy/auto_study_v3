import os
from tools.paths import RECENT_EX_DIR
from LLM.llm_selector import call_llm

def load_format_examples(tool):
    """포맷 예시 파일 불러오기 (ex_format_{tool}.txt)"""
    path = os.path.join(RECENT_EX_DIR, f"ex_format_{tool}.txt")
    if not os.path.exists(path):
        return "# 예시 없음"

    with open(path, "r", encoding="utf-8") as f:
        return "\n".join([line.strip() for line in f if line.strip()])

def format_questions(tool, dataset, difficulty_list, raw_response, llm_name):
    """자유형 질문을 → 구조화된 문제 포맷으로 변환"""
    examples = load_format_examples(tool)
    difficulty_line = " → ".join(difficulty_list)

    prompt = f"""아래는 LLM이 생성한 자유형 문제입니다.
    ⚠️ 형식 오류가 없도록 유의하세요. 아래 예시처럼 **정확히 이 형식**을 따라 주세요.
출력은 반드시 다음과 같이 `번호|난이도|데이터셋|카테고리|질문` 구조로 구성해 주세요.
    
        각 항목은 `|`로 구분되어야 하며, 항목 사이에 공백이 없어야 합니다.
        예시와 다르게 작성된 경우, LLM이 생성한 질문을 그대로 사용하지 마세요.

🧾 원본 질문:
{raw_response}

---

📌 변환 양식: 번호 | 난이도 | 데이터셋 | 카테고리 | 질문  
📊 사용 데이터셋: {dataset}  
🎯 난이도 순서: {difficulty_line}  
📎 예시:
{examples}

⚠️ 형식 오류가 없도록 유의하며, 번호는 반드시 1부터 시작하고, 난이도는 순서대로 매핑해주세요.
"""

    # LLM 호출 (두 번째)
    formatted_text = call_llm(prompt, llm_name, temperature=0.3)

    formatted_lines = [line.strip() for line in formatted_text.split("\n") if line.strip() and "|" in line]

    return formatted_lines
