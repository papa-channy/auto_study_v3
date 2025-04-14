from scripts.base_import import add_root_path
add_root_path()

import os
import json
from tools.paths import (
    SETTING_JSON_PATH, COUNT_PATH, FILE_TYPE_PATH,
    DATASETS_PATH, LLMS_TXT_PATH, TOOLS_PATH, DIFFICULTY_PATH
)

def load_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_setting():
    with open(SETTING_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_setting(config):
    with open(SETTING_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def edit_list_setting(name, current, options):
    while True:
        print(f"\n📘 현재 {name}: {', '.join(current)}")
        print("1. 그대로 사용  2. 수정")
        sel = input("> ").strip()
        if sel == "1":
            return current
        elif sel == "2":
            selected = set(current)
            while True:
                print(f"\n✅ 가능한 {name}: {', '.join(options)}")
                print("1. 추가  2. 삭제  3. 완료")
                act = input("> ").strip()
                if act == "1":
                    val = input("추가할 항목 입력: ").strip()
                    if val in options:
                        selected.add(val)
                elif act == "2":
                    val = input("삭제할 항목 입력: ").strip()
                    if val in selected and len(selected) > 1:
                        selected.remove(val)
                    else:
                        print("⚠️ 최소 1개는 유지해야 해요.")
                elif act == "3":
                    return list(sorted(selected))

def edit_single_choice(name, current, options):
    while True:
        print(f"\n🎯 현재 {name}: {current}")
        print("1. 그대로 사용  2. 변경")
        sel = input("> ").strip()
        if sel == "1":
            return current
        elif sel == "2":
            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")
            idx = input("선택 번호 > ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(options):
                return options[int(idx)-1]

def edit_study_matrix_difficulty(current, tool_opts, diff_opts):
    updated = current.copy()
    print("\n🛠 도구별 난이도 설정")
    print("1. 그대로 사용  2. 수정")
    sel = input("> ").strip()
    if sel == "1":
        return updated
    elif sel == "2":
        while True:
            print(f"\n현재 설정:")
            for tool, levels in updated.items():
                print(f" - {tool}: {', '.join(levels)}")
            print("\n1. 도구 추가  2. 도구 삭제  3. 난이도 수정  4. 완료")
            act = input("> ").strip()
            if act == "1":
                tool = input("추가할 도구: ").strip()
                if tool in tool_opts and tool not in updated:
                    updated[tool] = []
            elif act == "2":
                tool = input("삭제할 도구: ").strip()
                if tool in updated and len(updated) > 1:
                    del updated[tool]
            elif act == "3":
                tool = input("수정할 도구 이름: ").strip()
                if tool in updated:
                    print(f"현재 난이도: {', '.join(updated[tool])}")
                    print("1. 추가  2. 삭제")
                    action = input("> ").strip()
                    if action == "1":
                        lv = input("추가할 난이도: ").strip()
                        if lv in diff_opts and lv not in updated[tool]:
                            updated[tool].append(lv)
                    elif action == "2":
                        lv = input("삭제할 난이도: ").strip()
                        if lv in updated[tool] and len(updated[tool]) > 1:
                            updated[tool].remove(lv)
            elif act == "4":
                return updated

def edit_count(current):
    while True:
        print(f"\n🔁 현재 호출 횟수: {current}")
        val = input("새로운 호출 횟수 입력 (1~10): ").strip()
        if val.isdigit() and 1 <= int(val) <= 10:
            return int(val)
        print("❗ 1에서 10 사이 숫자를 입력해 주세요.")

# ▶️ 실행
if __name__ == "__main__":
    config = load_setting()

    dataset_options = load_list(DATASETS_PATH)
    llm_options = load_list(LLMS_TXT_PATH)
    tool_options = load_list(TOOLS_PATH)
    diff_options = load_list(DIFFICULTY_PATH)
    file_type_options = load_list(FILE_TYPE_PATH)

    config["DATASET"] = edit_list_setting("데이터셋", config["DATASET"], dataset_options)
    config["LLM"] = edit_single_choice("LLM", config["LLM"], llm_options)
    config["study_matrix&difficulty"] = edit_study_matrix_difficulty(
        config.get("study_matrix&difficulty", {}),
        tool_options,
        diff_options
    )
    config["file_type"] = edit_single_choice("파일 형식", config.get("file_type", "ipynb"), file_type_options)
    config["count"] = edit_count(config.get("count", 3))

    print("\n🧾 최종 설정 요약:")
    print(f"- 데이터셋: {', '.join(config['DATASET'])}")
    print(f"- LLM: {config['LLM']}")
    print(f"- 파일형식: {config['file_type']}")
    print(f"- 호출 횟수: {config['count']}")
    for tool, levels in config["study_matrix&difficulty"].items():
        print(f"- {tool}: {', '.join(levels)}")

    save_setting(config)
    print("\n✅ 설정이 저장되었습니다!")
