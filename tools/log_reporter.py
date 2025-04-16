import os
import json
import pandas as pd
from datetime import datetime
from tools.paths import (
    SETTING_PATH, LOG_REPORT_DIR, ARCHIVE_PATH,
    NOTEBOOK_DIR
)

def save_log_report():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%d %H:%M")
    log_path = LOG_REPORT_DIR / f"report_{date_str}.txt"

    # 1️⃣ 설정 로딩
    with open(SETTING_PATH, encoding="utf-8") as f:
        config = json.load(f)

    # 2️⃣ 문제 아카이브 로딩
    tool_counts = {}
    total = 0
    if ARCHIVE_PATH.exists():
        df = pd.read_excel(ARCHIVE_PATH)
        group = df.groupby("tool").size()
        for tool, count in group.items():
            tool_counts[tool] = int(count)
            total += int(count)

    # 3️⃣ 노트북 확인
    ipynb_files = [f.name for f in NOTEBOOK_DIR.glob("*.ipynb")]
    ipynb_summary = ', '.join(ipynb_files) if ipynb_files else "없음"

    # 4️⃣ 로그 작성
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

        f.write(f"\n📊 아카이브 문제 수:\n")
        for tool, count in tool_counts.items():
            f.write(f"- {tool}: {count}문제\n")
        f.write(f"→ 총합: {total}문제\n")

        f.write(f"\n📓 노트북 생성: {ipynb_summary}\n")
        f.write(f"📤 노션 업로드: 완료 (추정)\n")
        f.write(f"🕒 실행 시각: {time_str}\n")

    print(f"📝 로그 저장 완료 → {log_path.name}")
