# 📁 scripts/run_all.py

import sys, os, json, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 루트 등록

from scripts.base_import import add_root_path
add_root_path()

# 🔧 설정 및 기능 import
from tools.paths import SETTING_JSON_PATH
from generator.p_gen import update_prompt_templates
from generator.q_gen import generate_all_questions
from notion.preprocess import preprocess_questions
from generator.file_gen.ipynb_gen import generate_notebooks
from generator.file_gen.txt_gen import generate_txt_files
from generator.file_gen.py_gen import generate_py_files
from tools.archiver import archive_all_questions
from tools.log_reporter import save_log_report
from notion.notion_uploader import NotionUploader
from tools.clean_cache import clean_all_cache

# 1️⃣ 설정 로딩
with open(SETTING_JSON_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

tool_list = list(config["study_matrix&difficulty"].keys())
all_datasets = config["DATASET"]
selected_dataset = random.choice(all_datasets)
dataset_list = [selected_dataset]

difficulty_map = config["study_matrix&difficulty"]
llm_name = config["LLM"]
file_type = config["file_type"]
count = config["count"]

# ✅ 설정 요약 출력
print("📌 설정 로딩 완료:")
print(f"- 도구: {tool_list}")
print(f"- 데이터셋 (랜덤 선택): {dataset_list[0]}")
print(f"- LLM: {llm_name}")
print(f"- 파일형식: {file_type}")
print(f"- 호출 횟수: {count}")

# 2️⃣ 프롬프트 생성
update_prompt_templates(tool_list, dataset_list, difficulty_map, count)

# 3️⃣ 문제 생성
generate_all_questions(dataset_list, tool_list, difficulty_map, llm_name, count)

# 4️⃣ 전처리
processed_questions = preprocess_questions(tool_list)

# 5️⃣ 파일 생성
if file_type == "ipynb":
    generate_notebooks(processed_questions)
elif file_type == "txt":
    generate_txt_files(processed_questions)
elif file_type == "py":
    generate_py_files(processed_questions)
else:
    print(f"⚠️ 지원하지 않는 파일 형식입니다: {file_type}")

# 6️⃣ Notion 업로드
uploader = NotionUploader()
uploader.upload(processed_questions)

# 7️⃣ 아카이브 처리
archive_all_questions(tool_list)

# 8️⃣ 로그 저장
save_log_report()

# 9️⃣ 캐시 정리
clean_all_cache()
