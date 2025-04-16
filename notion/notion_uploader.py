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
        return list(set(categories)) or ["기타"]  # 기본 분류

    def upload(self, questions):
        success = 0
        fail = 0

        for i, q in enumerate(questions, 1):
            try:
                category = q.get("category", "")
                category_list = [category] if category else self.classify(q["question"])

                today = datetime.now().strftime("%Y-%m-%d")

                response = self.notion.pages.create(
                    parent={"database_id": self.database_id},
                    properties={
                        "날짜": {"rich_text": [{"text": {"content": today}}]},
                        "dataset": {"select": {"name": q["dataset"]}},
                        "문제": {"rich_text": [{"text": {"content": q["question"]}}]},
                        "분류": {"multi_select": [{"name": tag} for tag in category_list]},
                        "난이도": {"select": {"name": q["difficulty"]}},
                        "상태": {"select": {"name": "미풀이"}},
                    }
                )
                success += 1
                print(f"✅ {i} 업로드 성공 | 분류: {', '.join(category_list)}")
            except Exception as e:
                fail += 1
                print(f"❌ {i} 업로드 실패 | 내용: {q['question'][:30]}... → {e}")

        print(f"\n📤 업로드 요약: 성공 {success}개 / 실패 {fail}개")
