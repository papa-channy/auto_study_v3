# 📁 tools/store_manager.py

import json
import pandas as pd
from tools.paths import DATA_DIR, LOG_DIR

# ─────────────────────────────────────────────
# 🔹 JSON 저장
# ─────────────────────────────────────────────
def save_json(data: dict | list, filename: str, subdir: str = "data"):
    dir_path = DATA_DIR if subdir == "data" else LOG_DIR
    path = dir_path / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"📁 JSON 저장 완료 → {path.name}")

# ─────────────────────────────────────────────
# 🔹 TXT 저장 (줄 단위)
# ─────────────────────────────────────────────
def save_txt(lines: list[str], filename: str, subdir: str = "data"):
    dir_path = DATA_DIR if subdir == "data" else LOG_DIR
    path = dir_path / filename
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + "\n")
    print(f"📄 TXT 저장 완료 → {path.name}")

# ─────────────────────────────────────────────
# 🔹 pandas DataFrame 저장
# ─────────────────────────────────────────────
def save_df(df: pd.DataFrame, filename: str, subdir: str = "data", excel: bool = False):
    dir_path = DATA_DIR if subdir == "data" else LOG_DIR
    path = dir_path / filename

    if excel or filename.endswith(".xlsx"):
        path = path.with_suffix(".xlsx")
        df.to_excel(path, index=False)
    else:
        df.to_json(path, orient="records", force_ascii=False, indent=2)

    print(f"📊 DataFrame 저장 완료 → {path.name}")
