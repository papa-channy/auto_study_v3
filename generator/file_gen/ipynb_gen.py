import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from tools.paths import NOTEBOOK_DIR, SETTING_PATH
import json

# ✅ 도구 목록 동적 로딩 (설정 기반)
with open(SETTING_PATH, encoding="utf-8") as f:
    config = json.load(f)
tool_list = list(config["study_matrix&difficulty"].keys())

# ✅ 도구 이름 → 노트북 경로 자동 생성
NOTEBOOK_PATHS = {
    tool: os.path.join(NOTEBOOK_DIR, f"{tool}.ipynb")
    for tool in tool_list
}

def generate_notebooks(questions):
    """
    ✅ 도구별로 하나의 Jupyter Notebook에 누적 저장
    - notebooks/{tool}.ipynb
    """
    tool_buckets = {}

    for q in questions:
        tool = q["tool"]
        tool_buckets.setdefault(tool, []).append(q)

    for tool, qlist in tool_buckets.items():
        path = NOTEBOOK_PATHS.get(tool)

        if not path:
            print(f"⚠️ 노트북 경로가 정의되지 않은 도구: {tool}")
            continue

        # 기존 노트북 불러오기 or 새로 만들기
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)
        else:
            nb = new_notebook()

        for q in qlist:
            md = f"# 🔧 Tool: {q['tool']}\n\n**Dataset:** {q['dataset']}\n**난이도:** {q['difficulty']}\n\n**Q.** {q['question']}"
            code = (
                "import seaborn as sns\n"
                "import pandas as pd\n"
                f'dataset = sns.load_dataset("{q["dataset"]}")\n'
                "dataset.head(1)"
            )
            nb.cells.append(new_markdown_cell(md))
            nb.cells.append(new_code_cell(code))

        with open(path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

        print(f"📓 [{tool}] {len(qlist)}개 셀 누적 완료 → {os.path.basename(path)}")
