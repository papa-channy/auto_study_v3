def format_questions(questions):
    """
    ✅ 자유형 질문 리스트를 구조화된 딕셔너리로 정리
    - 중복 제거
    - 필드 정제
    - "Q" 대신 "question" 필드 유지
    """
    formatted = []
    seen = set()

    for q in questions:
        raw = q.get("question", "").strip()

        if not raw or raw in seen:
            continue
        seen.add(raw)

        formatted.append({
            "question": raw,
            "answer": "",  # 향후 해설 추가 가능
            "category": q.get("category", "기타"),
            "tool": q.get("tool", ""),
            "difficulty": q.get("difficulty", ""),
            "dataset": q.get("dataset", "")
        })

    return formatted
