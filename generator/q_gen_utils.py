def parse_llm_response(response_text, tool):
    """
    ✅ LLM 응답 텍스트에서 실제 질문만 추출하여 리스트 반환
    - 'Problem 1:', 'Translation:' 제거
    - 숫자/기호로 시작하는 불필요한 헤더 제거
    - 짧거나 안내성 문장 제외
    - tool은 아직 그대로 넘김 (포맷에서 합쳐짐)
    """
    lines = response_text.strip().split("\n")
    questions = []

    for line in lines:
        line = line.strip()

        # ❌ 빈 줄, 너무 짧은 줄
        if not line or len(line) < 5:
            continue

        # ❌ 안내 문구 제거
        lower = line.lower()
        if "translation" in lower or "here are" in lower or "analyze the following" in lower:
            continue

        # ❌ "Problem 1:", "문제 2)", "1. " 등 제거
        if line.lower().startswith("problem") and ":" in line:
            line = line.split(":", 1)[1].strip()
        elif line[0].isdigit() and line[1] in [".", ")", " "]:
            line = line[2:].strip()

        # ✅ Q. 붙여줄 필요 없음, format_questions()에서 번호 붙임
        questions.append({"question": line})

    return questions
