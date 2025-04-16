import os
import json
from tools.paths import QUESTIONS_PATH

def preprocess_questions(tool_list):
    """
    ✅ questions.json → Notion 업로드용 구조로 정제
    - 질문 앞번호 제거 X
    - "question" 필드 기반으로 필수 항목 추출
    """
    if not os.path.exists(QUESTIONS_PATH):
        print("📭 questions.json 파일이 없습니다.")
        return []

    with open(QUESTIONS_PATH, encoding="utf-8") as f:
        raw_data = json.load(f)

    processed = []

    for item in raw_data:
        q_text = item.get("question", "").strip()
        if not q_text:
            continue

        processed.append({
            "tool": item.get("tool", "unknown"),
            "index": "",
            "difficulty": item.get("difficulty", "중"),
            "dataset": item.get("dataset", "unknown"),
            "category": item.get("category", "기타"),
            "question": q_text
        })

    print(f"✅ preprocess 완료: {len(processed)}개 문제 정제됨")
    return processed
