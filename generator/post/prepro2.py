# 📁 generator/post/prepro2.py

import json
import uuid
from datetime import datetime
from tools.paths import SETTING_JSON_PATH, KEYWORDS_JSON_PATH

def load_settings():
    with open(SETTING_JSON_PATH, encoding="utf-8") as f:
        return json.load(f)

def load_keywords():
    with open(KEYWORDS_JSON_PATH, encoding="utf-8") as f:
        return json.load(f)

def auto_classify(text: str, keyword_map: dict) -> str:
    for category, keywords in keyword_map.items():
        if any(k in text for k in keywords):
            return category
    return "기타"

def generate_question_id(tool: str) -> str:
    short_time = datetime.now().strftime("%y%m%d")
    uid = uuid.uuid4().hex[:5]
    return f"{tool}_{short_time}_{uid}"

def structure_questions(m: list[str], tool: str) -> list[dict]:
    """
    ✅ m → o 변환
    tool: 'pds', 'sql', 'matplotlib' 등
    """
    config = load_settings()
    keywords = load_keywords()
    dataset = config["DATASET"][0]  # 랜덤 선택된 값
    difficulty = config["study_matrix&difficulty"][tool][0]
    filetype = config["file_type"]
    llm = config["LLM"]
    now = datetime.now().strftime("%Y-%m-%d")

    o = []

    for q in m:
        category = auto_classify(q, keywords)
        qid = generate_question_id(tool)

        o.append({
            "tool": tool,
            "dataset": dataset,
            "difficulty": difficulty,
            "filetype": filetype,
            "llm": llm,
            "category": category,
            "created_at": now,
            "question": q,
            "id": qid
        })

    return o
