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
        with open(path, "r", encoding="utf-8") as f:
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
