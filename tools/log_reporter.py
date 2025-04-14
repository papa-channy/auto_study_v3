import os
import json
from datetime import datetime
from tools.paths import (
    SETTING_JSON_PATH, LOG_DIR, NOTEBOOK_DIR,
    ARCHIVED_Q_PDS_PATH, ARCHIVED_Q_SQL_PATH, ARCHIVED_Q_VIZ_PATH
)

ARCHIVE_PATHS = {
    "pds": ARCHIVED_Q_PDS_PATH,
    "sql": ARCHIVED_Q_SQL_PATH,
    "viz": ARCHIVED_Q_VIZ_PATH
}

def save_log_report():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%d %H:%M")
    log_path = os.path.join(LOG_DIR, f"report_{date_str}.txt")

    # 🔧 설정 로딩
    with open(SETTING_JSON_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    # 📊 문제 수 계산
    tool_counts = {}
    total = 0
    for tool, path in ARCHIVE_PATHS.items():
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                count = sum(1 for line in f if line.strip())
                tool_counts[tool] = count
                total += count

    # 📓 노트북 파일 수 확인
    ipynb_files = [f for f in os.listdir(NOTEBOOK_DIR) if f.endswith(".ipynb")]
    ipynb_summary = ', '.join(ipynb_files) if ipynb_files else "없음"

    # 📝 로그 작성
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"📅 자동화 실행 리포트 - {time_str}\n\n")
        f.write(f"✅ 설정 요약:\n")
        f.write(f"- 데이터셋: {', '.join(config['DATASET'])}\n")
        f.write(f"- LLM: {config['LLM']}\n")
        f.write(f"- 파일 형식: {config['file_type']}\n")
        f.write(f"- 호출 횟수: {config['count']}\n")
        f.write(f"\n✅ 도구별 난이도 설정:\n")
        for tool, levels in config["study_matrix&difficulty"].items():
            f.write(f"- {tool}: {', '.join(levels)}\n")

        f.write(f"\n📊 문제 아카이브 수:\n")
        for tool, count in tool_counts.items():
            f.write(f"- {tool}: {count}문제\n")
        f.write(f"→ 총합: {total}문제\n")

        f.write(f"\n📓 노트북 생성: {ipynb_summary}\n")
        f.write(f"📤 노션 업로드: 완료 (추정)\n")
        f.write(f"🕒 실행 시각: {time_str}\n")

    print(f"📝 로그 저장 완료 → {os.path.basename(log_path)}")
