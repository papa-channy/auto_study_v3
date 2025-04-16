from pathlib import Path
from datetime import datetime
from tools.paths import NOTEBOOK_DIR

# 🔤 한글 도구명 매핑
tool_name_map = {
    "pds": "pandas 라이브러리",
    "sql": "SQL",
    "viz": "시각화"
}

def generate_py_files(questions):
    """
    ✅ 도구별 파이썬 학습 파일 생성
    - 저장 위치: notebooks/{tool}/{YYYY-MM-DD}/문제{i}.py
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
            file_path = folder / f"문제{i}.py"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# 🔧 Tool: {kor_tool}\n")
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

        print(f"📄 [{tool}] {len(items)}개 파이썬 파일 생성 완료 → {folder}")
