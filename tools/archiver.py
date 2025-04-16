import json
import pandas as pd
from datetime import datetime
from tools.paths import (
    ARCHIVE_PATH, QUESTIONS_PATH, PROMPT_PATH, EX_JSON_PATH, ARCHIVE_QUESTION_TXT_PATH
)

import re

def clean_question_text(text: str) -> str:
    """
    ✅ 질문 텍스트에서:
    - 영어 안내문 제거
    - "Problem", "Translation", "Here are" 등 필터링
    - markdown 메타 제거 (**문제:**, **데이터:** 등)
    - 여러 줄 중 실제 질문 줄만 추출
    """
    text = text.strip()
    if not text or len(text) < 5:
        return ""

    lowered = text.lower()
    if any(kw in lowered for kw in ["translation", "here are", "example", "total score", "note:", "answer:"]):
        return ""

    # 줄 분할 후 "문제"만 남기기
    lines = text.split("\n")
    filtered_lines = []

    for line in lines:
        line = line.strip()

        # markdown 요소 제거
        if re.match(r"^\*\*(문제|데이터|힌트|참고|정답|Answer|Expected Output|점수).*", line):
            continue

        if "plt." in line or "sns." in line or "import " in line:
            continue  # 코드 제거

        # 한글 문제처럼 보이는 것만 남기기
        if re.search(r"[가-힣]{4,}", line):
            filtered_lines.append(line)

    return filtered_lines[0] if filtered_lines else ""


def archive_all():
    """
    ✅ 전체 아카이브 처리
    1. archive.xlsx 누적
    2. archive_questions.txt 저장 (정제된 질문만)
    3. ex.json 최신 예시 갱신
    4. prompt.json, questions.json 초기화
    """
    # 1️⃣ 질문 로딩
    if not QUESTIONS_PATH.exists():
        print("📭 questions.json이 존재하지 않습니다.")
        return

    with open(QUESTIONS_PATH, encoding="utf-8") as f:
        questions = json.load(f)

    if not questions:
        print("📭 저장할 질문이 없습니다.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    today_short = datetime.now().strftime("%y%m%d")

    # 2️⃣ archive.xlsx 누적 저장
    for q in questions:
        q["created_at"] = today

    new_df = pd.DataFrame(questions)
    if ARCHIVE_PATH.exists() and ARCHIVE_PATH.stat().st_size > 0:
        old_df = pd.read_excel(ARCHIVE_PATH)
        new_df = pd.concat([old_df, new_df], ignore_index=True)

    new_df.to_excel(ARCHIVE_PATH, index=False)
    print(f"✅ archive.xlsx에 {len(questions)}문제 누적 저장 완료")

    # 3️⃣ archive_questions.txt 저장 (정제된 질문만)
    with open(ARCHIVE_QUESTION_TXT_PATH, "a", encoding="utf-8") as f:
        for q in questions:
            line = clean_question_text(q.get("question", ""))
            if line:
                f.write(f"{line}\n")
    print("✅ archive_questions.txt 정제된 질문 저장 완료")

    # 4️⃣ 최신 예시 갱신 (ex.json)
    ex_dict = {}
    for q in questions:
        tool = q.get("tool")
        if not tool:
            continue
        ex_dict.setdefault(tool, []).append(q)

    trimmed = {tool: items[-5:] for tool, items in ex_dict.items()}

    with open(EX_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(trimmed, f, indent=2, ensure_ascii=False)
    print("✅ ex.json 최신 예시 갱신 완료 (도구별 5개)")

    # 5️⃣ prompt, questions 초기화
    with open(PROMPT_PATH, "w", encoding="utf-8") as f:
        json.dump({}, f, indent=2, ensure_ascii=False)

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2, ensure_ascii=False)

    print("🧹 프롬프트 및 문제 초기화 완료")
