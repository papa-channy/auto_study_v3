# 📁 notion/check_notion_count.py

import os
from datetime import datetime
from dotenv import load_dotenv
from notion_client import Client
from tools.paths import LOG_DIR, ENV_PATH

# 1️⃣ Notion API 설정
load_dotenv(dotenv_path=ENV_PATH)
notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")

# 2️⃣ 오늘 날짜
today_full = datetime.now().strftime("%Y-%m-%d")      # 로그용
today_notion = datetime.now().strftime("%m/%d")       # Notion 필드용
log_file = os.path.join(LOG_DIR, f"report_{today_full}.txt")

# 3️⃣ Notion에서 오늘 날짜에 해당하는 문제 수만 조회
notion_total = 0
try:
    response = notion.databases.query(
        database_id=database_id,
        filter={
            "property": "날짜",
            "rich_text": {
                "equals": today_notion
            }
        },
        page_size=100
    )
    notion_total += len(response["results"])
    while response.get("has_more"):
        response = notion.databases.query(
            database_id=database_id,
            start_cursor=response["next_cursor"],
            filter={
                "property": "날짜",
                "rich_text": {
                    "equals": today_notion
                }
            },
            page_size=100
        )
        notion_total += len(response["results"])
except Exception as e:
    print(f"❌ Notion API 에러: {e}")
    exit()

# 4️⃣ 로그에서 오늘 업로드된 문제 수 추출
log_total = None
if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("→ 총합:"):
                try:
                    log_total = int(line.strip().split(":")[1].replace("문제", "").strip())
                except:
                    log_total = None
else:
    print(f"⚠️ 오늘 로그 파일 없음: {log_file}")

# 5️⃣ 결과 비교
print(f"\n📅 오늘 날짜 기준: {today_notion}")
print(f"📊 Notion 등록 문제 수 (오늘): {notion_total}")
if log_total is not None:
    print(f"📝 로그 기록 문제 수: {log_total}")
    if log_total == notion_total:
        print("✅ 업로드 정상 완료! 🎉")
    else:
        print("❌ 누락 또는 불일치 발생 (Notion vs 로그)")
else:
    print("⚠️ 로그 비교 불가 (문제 수 정보 없음)")
