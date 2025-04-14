import os
from tools.paths import (
    DATA_DIR, PROMPT_DIR, RECENT_EX_DIR
)

def create_default_files_for_tool(tool_name):
    """
    ✅ 새로운 도구를 study_matrix에 추가할 때 호출하여
    필요한 텍스트 파일들을 자동으로 생성한다.
    생성 경로:
    - data/new_q_{tool}.txt
    - data/archived_q_{tool}.txt
    - prompt/p_{tool}.txt
    - recent_ex/ex_{tool}.txt
    """

    tool = tool_name.lower()

    files_to_create = {
        f"data/new_q_{tool}.txt": os.path.join(DATA_DIR, f"new_q_{tool}.txt"),
        f"data/archived_q_{tool}.txt": os.path.join(DATA_DIR, f"archived_q_{tool}.txt"),
        f"prompt/p_{tool}.txt": os.path.join(PROMPT_DIR, f"p_{tool}.txt"),
        f"recent_ex/ex_{tool}.txt": os.path.join(RECENT_EX_DIR, f"ex_{tool}.txt"),
    }

    for label, path in files_to_create.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                pass  # 빈 파일 생성
            print(f"📁 파일 생성: {label}")
        else:
            print(f"⚠️ 이미 존재: {label}")

import os
from tools.paths import (
    DATA_DIR, PROMPT_DIR, RECENT_EX_DIR
)

def create_default_files_for_tool(tool_name):
    """
    ✅ 새로운 도구를 study_matrix에 추가할 때 호출하여
    필요한 텍스트 파일들을 자동으로 생성한다.
    생성 경로:
    - data/new_q_{tool}.txt
    - data/archived_q_{tool}.txt
    - prompt/p_{tool}.txt
    - recent_ex/ex_{tool}.txt
    """

    tool = tool_name.lower()

    files_to_create = {
        f"data/new_q_{tool}.txt": os.path.join(DATA_DIR, f"new_q_{tool}.txt"),
        f"data/archived_q_{tool}.txt": os.path.join(DATA_DIR, f"archived_q_{tool}.txt"),
        f"prompt/p_{tool}.txt": os.path.join(PROMPT_DIR, f"p_{tool}.txt"),
        f"recent_ex/ex_{tool}.txt": os.path.join(RECENT_EX_DIR, f"ex_{tool}.txt"),
    }

    for label, path in files_to_create.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                pass  # 빈 파일 생성
            print(f"📁 파일 생성: {label}")
        else:
            print(f"⚠️ 이미 존재: {label}")

create_default_files_for_tool("statx")