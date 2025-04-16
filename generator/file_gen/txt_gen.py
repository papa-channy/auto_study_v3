from pathlib import Path
from datetime import datetime
from tools.paths import NOTEBOOK_DIR

# 🔤 도구명 한글 변환
tool_name_map = {
    "pds": "pandas 라이브러리",
    "sql": "SQL",
    "viz": "시각화"
}

def generate_txt_files(questions):
    """
    ✅ 도구별 텍스트 학습 파일 생성
    - 저장 경로: notebooks/{tool}/{YYYY-MM-DD}/문제{i}.txt
    """
    today = datetime.today().strftime("%Y-%m-%d")
    tool_buckets = {}

    for q in questions:
        tool = q["tool"]
        tool_buckets.setdefault(tool, []).append(q)

    for tool, items in tool_buckets.items():
        folder = NOTEBOOK_DIR / tool / today
        folder.mkdir(parents=True, exist_ok=True)

        kor_tool = tool_name_map.get(tool, tool)

        for i, q in enumerate(items, 1):
            file_path = folder / f"문제{i}.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"[{kor_tool}] {q['dataset']} | {q['difficulty']}\n")
                f.write(q["question"] + "\n")

        print(f"📄 [{tool}] {len(items)}개 텍스트 파일 생성 완료 → {folder}")
