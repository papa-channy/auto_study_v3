import os
from tools.paths import DATA_DIR, RECENT_EX_DIR, PROMPT_DIR

def archive_all_questions(tool_list):
    """
    ✅ 도구 리스트 기반으로:
    - new_q → archived_q 저장
    - recent_ex에 최근 3개 유지
    - new_q 파일 초기화
    - prompt 파일 초기화
    """
    for tool in tool_list:
        tool = tool.lower()
        new_path = os.path.join(DATA_DIR, f"new_q_{tool}.txt")
        archived_path = os.path.join(DATA_DIR, f"archived_q_{tool}.txt")
        recent_path = os.path.join(RECENT_EX_DIR, f"ex_{tool}.txt")
        prompt_path = os.path.join(PROMPT_DIR, f"p_{tool}.txt")

        if not os.path.exists(new_path):
            print(f"❗ {tool} → new_q 파일 없음: {new_path}")
            continue

        with open(new_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print(f"📭 [{tool}] 저장할 문제가 없습니다.")
            continue

        # 1️⃣ 아카이브 append
        with open(archived_path, "a", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")

        # 2️⃣ recent_ex append 후 최근 3개 유지
        recent_lines = []
        if os.path.exists(recent_path):
            with open(recent_path, "r", encoding="utf-8") as f:
                recent_lines = [line.strip() for line in f if line.strip()]

        combined = recent_lines + lines
        latest_three = combined[-3:]

        with open(recent_path, "w", encoding="utf-8") as f:
            for line in latest_three:
                f.write(line + "\n")

        # 3️⃣ new_q 초기화
        open(new_path, "w", encoding="utf-8").close()

        # 4️⃣ 프롬프트 초기화
        open(prompt_path, "w", encoding="utf-8").close()

        print(f"✅ [{tool}] {len(lines)}문제 → 아카이브 / 최근예시 정리 완료")

    print("🧹 전체 도구 정리 완료")
