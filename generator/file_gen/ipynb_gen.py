import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

NOTEBOOK_PATHS = {
    "pds": os.path.join("notebooks", "qpds.ipynb"),
    "sql": os.path.join("notebooks", "qsql.ipynb"),
    "viz": os.path.join("notebooks", "qviz.ipynb")
}

def generate_notebooks(questions):
    """
    도구별로 하나의 Jupyter Notebook에 누적 저장
    (notebooks/qpds.ipynb, qsql.ipynb, qviz.ipynb)
    """
    tool_buckets = {}

    for q in questions:
        tool = q["tool"]
        tool_buckets.setdefault(tool, []).append(q)

    for tool, qlist in tool_buckets.items():
        path = NOTEBOOK_PATHS[tool]

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
