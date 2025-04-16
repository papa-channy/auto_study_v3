# 📁 generator/core/q_raw_generator.py

from LLM.llm_selector import call_llm

def generate_raw_questions(prompt_text: str, llm_name: str) -> list[str]:
    """
    ✅ 자유형 문제 생성
    입력 프롬프트(prompt_text)를 받아 LLM에게 전달 → 문제 리스트 반환
    """
    response = call_llm(prompt=prompt_text, llm_name=llm_name)

    # 기본 줄 단위 분해 + 정제
    lines = response.strip().split("\n")
    questions = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 접두어 제거: "Q.", "문제1", "1.", "-", "*", 등
        for prefix in ["Q.", "Q:", "문제", "1.", "2.", "-", "*"]:
            if line.lower().startswith(prefix.lower()):
                line = line[len(prefix):].strip()
        # 영어-only 문장 제거
        if line.isascii() and len(line.split()) > 4:
            continue
        if len(line) > 10:  # 너무 짧은건 제외
            questions.append(line)

    return questions
