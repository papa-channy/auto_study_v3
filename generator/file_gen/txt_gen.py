import os
from datetime import datetime

def generate_txt_files(questions):
    """
    도구별 텍스트 학습 파일 생성 (notebooks/{tool}/YYYY-MM-DD/문제N.txt)
    """
    today = datetime.today().strftime("%Y-%m-%d")
    base_dir = os.path.join("notebooks")

    tool_buckets = {}

    # 도구별로 묶기
    for q in questions:
        tool = q["tool"]
        tool_buckets.setdefault(tool, []).append(q)

    for tool, items in tool_buckets.items():
        folder = os.path.join(base_dir, tool, today)
        os.makedirs(folder, exist_ok=True)

        for i, q in enumerate(items, 1):
            filename = os.path.join(folder, f"문제{i}.txt")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"[{q['tool']}] {q['dataset']} | {q['difficulty']}\n")
                f.write(q["question"] + "\n")

        print(f"📄 [{tool}] {len(items)}개 텍스트 파일 생성 완료")
