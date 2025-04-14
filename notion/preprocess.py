import os
from tools.paths import DATA_DIR

def preprocess_questions(tool_list):
    """
    ✅ 각 도구별 new_q_{tool}.txt에서 문제를 불러와 | 기준으로 분리하여 구조화된 리스트 반환
    실패하지 않도록 최대한 보정하며 필드 분해함
    """
    all_questions = []

    for tool in tool_list:
        path = os.path.join(DATA_DIR, f"new_q_{tool}.txt")
        if not os.path.exists(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip() or "|" not in line:
                    continue

                parts = line.strip().split("|", 4)
                while len(parts) < 5:
                    parts.append("")  # 부족한 필드는 빈칸으로 채움

                번호, 난이도, 데이터셋, 카테고리, 질문 = parts
                all_questions.append({
                    "tool": tool,
                    "index": 번호,
                    "difficulty": 난이도,
                    "dataset": 데이터셋,
                    "category": 카테고리,
                    "question": 질문
                })


    return all_questions
