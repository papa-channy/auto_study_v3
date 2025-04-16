# 📁 scripts/add.py
import os
from tools.paths import (
    LLM_DIR, PROMPT_DIR, RECENT_EX_DIR, FILE_GEN_DIR,
    DATA_DIR
)

# ✅ 항목 추가 시 필요한 파일 자동 생성기

def create_files_for_llm(name):
    path = os.path.join(LLM_DIR, f"{name}.py")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"""
# ✅ LLM: {name}
# TODO: 이 LLM에 맞는 call_llm(prompt, llm_name, temperature) 함수를 작성해 주세요

def call_llm(prompt, llm_name, temperature=0.7):
    raise NotImplementedError("{name}용 LLM 호출 함수가 아직 구현되지 않았습니다.")
""".strip())
        print(f"✅ LLM 파일 생성 완료 → {path}")


def create_files_for_study_matrix(name):
    targets = [
        os.path.join(DATA_DIR, f"new_q_{name}.txt"),
        os.path.join(DATA_DIR, f"archived_q_{name}.txt"),
        os.path.join(PROMPT_DIR, f"p_{name}.txt"),
        os.path.join(RECENT_EX_DIR, f"ex_{name}.txt")
    ]
    for path in targets:
        if not os.path.exists(path):
            open(path, "w", encoding="utf-8").close()
            print(f"✅ 파일 생성: {path}")


def create_files_for_file_type(name):
    path = os.path.join(FILE_GEN_DIR, f"{name}.py")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"""
# ✅ 파일 생성기: {name}.py
# TODO: 이 형식의 문제 파일을 생성하는 함수를 작성해 주세요

def generate_{name}_files(processed_questions):
    raise NotImplementedError("{name} 형식 파일 생성기는 아직 작성되지 않았습니다.")
""".strip())
        print(f"✅ 파일 생성: {path}")


# 🎯 진입점 함수

def handle_addition(category: str, name: str):
    name = name.strip().lower()

    if category == "llm":
        create_files_for_llm(name)
    elif category == "study_matrix":
        create_files_for_study_matrix(name)
    elif category == "file_type":
        create_files_for_file_type(name)
    else:
        print(f"⚠️ 자동 생성 대상이 아닌 항목입니다: {category}")
