# 📁 scripts/add.py

from scripts.base_import import add_root_path
add_root_path()

import os
from tools.paths import (
    TOOLS_PATH, LLMS_TXT_PATH, FILE_TYPE_PATH,
    DATA_DIR, PROMPT_DIR, RECENT_EX_DIR,
    LLM_DIR, FILE_GEN_DIR
)

def append_if_not_exists(path, item):
    if not os.path.exists(path):
        items = []
    else:
        with open(path, "r", encimport os
import json
import pandas as pd
from datetime import datetime
from tools.paths import (
    SETTING_PATH, ARCHIVE_PATH,
    NOTEBOOK_DIR, LOG_REPORT_DIR
)
from config.derived_config import DERIVED_CONFIG

tool_name_map = {
    "pds": "pandas 라이브러리",
    "sql": "SQL",
    "viz": "시각화"
}

def save_log_report():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%d %H:%M")
    log_path = LOG_REPORT_DIR / f"report_{date_str}.txt"

    # 📥 설정 로딩
    with open(SETTING_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    # 📊 archive.xlsx 로딩
    if ARCHIVE_PATH.exists():
        df = pd.read_excel(ARCHIVE_PATH)
    else:
        df = pd.DataFrame(columns=["tool", "question"])

    # 도구별 문제 수 카운트
    tool_counts = df["tool"].value_counts().to_dict()
    total = len(df)

    # 📓 노트북 파일 수 확인
    ipynb_files = [f for f in os.listdir(NOTEBOOK_DIR) if f.endswith(".ipynb")]
    ipynb_summary = ', '.join(ipynb_files) if ipynb_files else "없음"

    # 📝 로그 작성
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"📅 자동화 실행 리포트 - {time_str}\n\n")

        f.write("✅ 설정 요약:\n")
        f.write(f"- 데이터셋: {', '.join(config['DATASET'])}\n")
        f.write(f"- LLM: {config['LLM']}\n")
        f.write(f"- 파일 형식: {config['file_type']}\n")
        f.write(f"- 호출 횟수: {config['count']}\n")

        f.write("\n✅ 도구별 난이도 설정:\n")
        for tool, levels in config["study_matrix&difficulty"].items():
            kor_tool = tool_name_map.get(tool, tool)
            f.write(f"- {kor_tool}: {', '.join(levels)}\n")

        f.write("\n📊 문제 아카이브 수:\n")
        for tool in config["study_matrix&difficulty"]:
            kor_tool = tool_name_map.get(tool, tool)
            count = tool_counts.get(tool, 0)
            f.write(f"- {kor_tool}: {count}문제\n")
        f.write(f"→ 총합: {total}문제\n")

        f.write(f"\n📓 노트북 생성: {ipynb_summary}\n")
        f.write(f"📤 노션 업로드: 완료 (추정)\n")
        f.write(f"🕒 실행 시각: {time_str}\n")

    print(f"📝 로그 저장 완료 → {log_path.name}")
oding="utf-8") as f:
            items = [line.strip() for line in f if line.strip()]

    if item in items:
        print(f"⚠️ 이미 존재합니다: {item}")
        return False

    with open(path, "a", encoding="utf-8") as f:
        f.write(item + "\n")
    print(f"✅ 추가 완료: {item}")
    return True

def create_tool_files(tool):
    tool = tool.lower()
    files = {
        f"data/new_q_{tool}.txt": os.path.join(DATA_DIR, f"new_q_{tool}.txt"),
        f"data/archived_q_{tool}.txt": os.path.join(DATA_DIR, f"archived_q_{tool}.txt"),
        f"prompt/p_{tool}.txt": os.path.join(PROMPT_DIR, f"p_{tool}.txt"),
        f"recent_ex/ex_{tool}.txt": os.path.join(RECENT_EX_DIR, f"ex_{tool}.txt"),
    }

    for label, path in files.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                pass
            print(f"📁 파일 생성: {label}")
        else:
            print(f"⚠️ 이미 존재: {label}")

def create_llm_template(name):
    path = os.path.join(LLM_DIR, f"{name.lower()}.py")
    if os.path.exists(path):
        print(f"⚠️ LLM 파일 이미 존재: {path}")
        return

    template = f'''
def call_llm(prompt: str, llm_name: str, temperature: float = 0.6) -> str:
    """
    ✨ 신규 LLM '{name}' 구현 영역
    여기에 실제 LLM API 연동 코드를 작성하세요.
    """
    return f"[{{llm_name}} 응답 - 구현 필요] " + prompt
'''.strip()

    with open(path, "w", encoding="utf-8") as f:
        f.write(template + "\n")

    print(f"📄 LLM/{name.lower()}.py 생성 완료!")

def create_file_type_template(name):
    path = os.path.join(FILE_GEN_DIR, f"{name.lower()}.py")
    if os.path.exists(path):
        print(f"⚠️ 파일 생성기 이미 존재: {path}")
        return

    template = f'''
def generate_{name.lower()}_files(questions):
    """
    ✨ 신규 file_type '{name}' 구현 영역
    여기에 {name.upper()} 파일 생성 코드를 작성하세요.
    """
    print("⚠️ {name.upper()} 생성 기능은 아직 구현되지 않았습니다.")
'''.strip()

    with open(path, "w", encoding="utf-8") as f:
        f.write(template + "\n")

    print(f"📄 file_gen/{name.lower()}.py 생성 완료!")

def add_item(category, name):
    category = category.lower()
    name = name.strip()

    if category == "tool":
        if append_if_not_exists(TOOLS_PATH, name):
            create_tool_files(name)

    elif category == "llm":
        if append_if_not_exists(LLMS_TXT_PATH, name):
            create_llm_template(name)

    elif category in ["file_type", "filetype"]:
        if append_if_not_exists(FILE_TYPE_PATH, name):
            create_file_type_template(name)

    else:
        print(f"❌ 지원하지 않는 항목: {category}")


from scripts.base_import import add_root_path
add_root_path()

import os
from tools.paths import (
    DATASETS_PATH, LLMS_TXT_PATH, TOOLS_PATH,
    DIFFICULTY_PATH, FILE_TYPE_PATH, COUNT_PATH
)

option_map = {
    "datasets": DATASETS_PATH,
    "llms": LLMS_TXT_PATH,
    "study_matrix": TOOLS_PATH,
    "difficulty": DIFFICULTY_PATH,
    "file_type": FILE_TYPE_PATH,
    "count": COUNT_PATH
}

def load_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def edit_text_list(path, title):
    items = load_lines(path)
    while True:
        print(f"\n📘 현재 {title} 항목: {', '.join(items)}")
        print("1. 추가  2. 삭제  3. 초기화 후 다시쓰기  4. 완료")
        choice = input("> ").strip()
        if choice == "1":
            new = input("➕ 추가할 값: ").strip()
            if new and new not in items:
                items.append(new)
        elif choice == "2":
            for i, item in enumerate(items):
                print(f"{i+1}. {item}")
            idx = input("❌ 삭제할 번호: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(items):
                del items[int(idx) - 1]
        elif choice == "3":
            raw = input("📝 쉼표로 구분해 다시 입력: ").strip()
            items = [s.strip() for s in raw.split(",") if s.strip()]
        elif choice == "4":
            break
    save_lines(path, items)
    print(f"✅ {title} 항목 저장 완료")

def edit_count_value(path):
    while True:
        print(f"\n📶 호출 횟수 설정 (현재값: {load_lines(path)[0]})")
        val = input("새 값 입력 (1~10): ").strip()
        if val.isdigit() and 1 <= int(val) <= 10:
            save_lines(path, [val])
            print("✅ 호출 횟수 저장 완료")
            break
        else:
            print("❗ 1~10 사이 숫자를 입력하세요.")

# ▶️ 실행
if __name__ == "__main__":
    print("⚙️ 수정할 항목 선택")
    for i, key in enumerate(option_map.keys()):
        print(f"{i+1}. {key}")
    sel = input("> ").strip()

    keys = list(option_map.keys())
    if sel.isdigit() and 1 <= int(sel) <= len(keys):
        option = keys[int(sel) - 1]
        path = option_map[option]

        if option == "count":
            edit_count_value(path)
        else:
            edit_text_list(path, option)
    else:
        print("❗ 올바른 번호를 선택하세요.")
    print("✅ 설정 완료")