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