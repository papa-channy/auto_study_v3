# 📁 scripts/option_admin.py
from scripts.base_import import add_root_path
add_root_path()

import json
from tools.paths import SETTING_JSON_PATH
from opt_set.add import handle_addition

# 📦 JSON 로딩 & 저장

def load_options():
    with open(SETTING_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_options(options):
    with open(SETTING_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(options, f, ensure_ascii=False, indent=2)

# 📋 항목 선택 및 편집

def edit_option_category(category, values):
    print(f"\n📘 현재 '{category}' 옵션 목록:")
    for i, val in enumerate(values):
        print(f"{i+1}. {val}")

    print("\n1. 그대로 사용\n2. 기타 항목 추가")
    choice = input("선택 > ").strip()

    if choice == "1":
        return values
    elif choice == "2":
        new = input("➕ 추가할 새 항목 이름: ").strip()
        if new and new not in values:
            values.append(new)
            print(f"✅ '{new}' 추가 완료")

            # 자동 생성기 호출 필요 시
            if category in ["llm", "study_matrix", "file_type"]:
                handle_addition(category, new)

    return values

# ▶️ 실행 시작

if __name__ == "__main__":
    options = load_options()

    print("⚙️ 편집할 항목을 선택하세요:")
    editable_keys = [k for k in options.keys() if k != "count"]
    for i, key in enumerate(editable_keys):
        print(f"{i+1}. {key}")

    sel = input("> ").strip()

    if sel.isdigit() and 1 <= int(sel) <= len(editable_keys):
        key = editable_keys[int(sel) - 1]
        options[key] = edit_option_category(key, options[key])
        save_options(options)
        print("✅ 옵션이 저장되었습니다!")
    else:
        print("❗ 올바른 항목을 선택하세요.")
