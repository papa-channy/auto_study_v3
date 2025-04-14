# 📁 notion/notion_uploader.py
import os
import json
from dotenv import load_dotenv
from datetime import datetime
from notion_client import Client
from tools.paths import KEYWORDS_JSON_PATH, ENV_PATH

class NotionUploader:
    def __init__(self):
        self.keyword_map = self.load_keyword_map(KEYWORDS_JSON_PATH)

        load_dotenv(dotenv_path=ENV_PATH)
        self.api_key = os.getenv("NOTION_API_KEY")
        self.database_id = os.getenv("NOTION_DATABASE_ID")

        print(f"🔐 NOTION_API_KEY 시작: {self.api_key[:10]}...")
        print(f"📘 NOTION_DATABASE_ID: {self.database_id}")

        self.notion = Client(auth=self.api_key)

    def load_keyword_map(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def classify(self, text):
        categories = []
        for category, keywords in self.keyword_map.items():
            if any(k in text for k in keywords):
                categories.append(category)
        return list(set(categories))

    def upload(self, questions):
        for i, q in enumerate(questions, 1):
            try:
                category = q.get("category", "")
                category_list = [category] if category else self.classify(q["question"])

                today = datetime.now()
                today_str = f"{today.month}/{today.day}"
                self.notion.pages.create(
                    parent={"database_id": self.database_id},
                    properties={
                        "날짜": {"rich_text": [{"text": {"content": today_str}}]},
                        "dataset": {"select": {"name": q["dataset"]}},
                        "문제": {"rich_text": [{"text": {"content": q["question"]}}]},
                        "분류": {"multi_select": [{"name": tag} for tag in category_list]} if category_list else {} ,
                        "난이도": {"select": {"name": q["difficulty"]}},
                        "상태": {"select": {"name": "미풀이"}},
                    }
                )
                print(f"✅ {i} 업로드 성공 | 분류: {', '.join(category_list) if category_list else '없음'}")
            except Exception as e:
                print(f"❌ {i} 업로드 실패: {e}")

# ▶️ run_all.py 또는 test에서:
# from notion.notion_uploader import NotionUploader
# uploader = NotionUploader()
# uploader.upload(processed_questions)
