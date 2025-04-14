import os
from datetime import datetime

def generate_py_files(questions):
    """
    도구별 파이썬 학습 파일 생성 (notebooks/{tool}/YYYY-MM-DD/문제N.py)
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
            filename = os.path.join(folder, f"문제{i}.py")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# 🔧 Tool: {q['tool']}\n")
                f.write(f"# 📊 Dataset: {q['dataset']}\n")
                f.write(f"# 🎯 Difficulty: {q['difficulty']}\n\n")

                f.write("# 🧪 필요 라이브러리\n")
                f.write("import seaborn as sns\nimport pandas as pd\n\n")

                f.write('"""\n')
                f.write(f"Q. {q['question']}\n")
                f.write('"""\n\n')

                f.write("# 🔍 데이터 미리보기\n")
                f.write(f'dataset = sns.load_dataset("{q["dataset"]}")\n')
                f.write("dataset.head(1)\n")

        print(f"📄 [{tool}] {len(items)}개 파이썬 파일 생성 완료")
