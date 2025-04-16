# 📁 scripts/run_all.py

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.base_import import add_root_path
add_root_path()

# 🔧 설정 불러오기
import json
from tools.paths import SETTING_PATH
from config.derived_config import DERIVED_CONFIG

# ✨ 기능 import
from generator.p_gen import update_prompt_templates
from generator.q_gen import generate_all_questions
from notion.preprocess import preprocess_questions
from generator.file_gen.ipynb_gen import generate_notebooks
from generator.file_gen.txt_gen import generate_txt_files
from generator.file_gen.py_gen import generate_py_files
from tools.archiver import archive_all
from logs.log_reporter import save_log_report
from tools.clean_cache import clean_all_cache
from notion.notion_uploader import NotionUploader

# ───────────────────────────────
# 1️⃣ 사용자 설정 로딩
with open(SETTING_PATH, encoding="utf-8") as f:
    config = json.load(f)

tool_list = list(config["study_matrix&difficulty"].keys())
difficulty_map = config["study_matrix&difficulty"]
file_type = config["file_type"]
llm_name = config["LLM"]
count = config["count"]
dataset_list = DERIVED_CONFIG["random_datasets"]

# ───────────────────────────────
# 2️⃣ 설정 출력
print("📌 설정 요약")
print(f"- 도구: {tool_list}")
print(f"- 난이도: {difficulty_map}")
print(f"- LLM: {llm_name}")
print(f"- 파일 형식: {file_type}")
print(f"- 데이터셋 (랜덤): {dataset_list}")
print(f"- 호출 횟수: {count}")

# ───────────────────────────────
# 3️⃣ 프롬프트 생성
update_prompt_templates(tool_list, dataset_list, difficulty_map, count)

# 4️⃣ 문제 생성
generate_all_questions()

# 5️⃣ 전처리
processed_questions = preprocess_questions(tool_list)

# 6️⃣ 파일 생성
if file_type == "ipynb":
    generate_notebooks(processed_questions)
elif file_type == "txt":
    generate_txt_files(processed_questions)
elif file_type == "py":
    generate_py_files(processed_questions)
else:
    print(f"⚠️ 지원하지 않는 파일 형식: {file_type}")

# 7️⃣ Notion 업로드
# uploader = NotionUploader()
# uploader.upload(processed_questions)

# 8️⃣ 아카이브
archive_all()

# 9️⃣ 로그 저장
save_log_report()

# 🔟 캐시 삭제
clean_all_cache()
