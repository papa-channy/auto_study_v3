import json
import random
from pathlib import Path

# ─────────────────────────────────────────────
# 📍 기본 경로 설정
# ─────────────────────────────────────────────
CONFIG_DIR = Path(__file__).parent
SETTING_PATH = CONFIG_DIR / "setting_config.json"

# ─────────────────────────────────────────────
# 📥 설정 파일 로드
# ─────────────────────────────────────────────
with open(SETTING_PATH, encoding="utf-8") as f:
    config = json.load(f)

# ─────────────────────────────────────────────
# 📊 설정 항목 추출
# ─────────────────────────────────────────────
study_matrix = config["study_matrix&difficulty"]  # 도구별 난이도
call_count = config["count"]                      # 도구별 호출 횟수
example_count = config.get("example_count", 2)    # 예시 개수 (기본값 2)
all_datasets = config["DATASET"]                  # 전체 데이터셋 목록

# 🔢 랜덤으로 선택할 dataset 수 (기본값: 3개)
random_dataset_count = config.get("random_dataset_count", 3)

# ─────────────────────────────────────────────
# 🧠 도구별 문제 수 계산
# ─────────────────────────────────────────────
tool_summary = {}

for tool, difficulties in study_matrix.items():
    difficulty_count = len(difficulties)
    total_questions = difficulty_count * call_count
    batch_size = call_count  # 호출 횟수 = 한 번에 생성할 문제 수 기준 (수정 가능)

    tool_summary[tool] = {
        "difficulties": difficulties,
        "total_questions": total_questions,
        "batch_size": batch_size,
        "calls": call_count
    }

# ─────────────────────────────────────────────
# 🧾 최종 구성 객체
# ─────────────────────────────────────────────
DERIVED_CONFIG = {
    "tool_summary": tool_summary,
    "total_questions": sum(t["total_questions"] for t in tool_summary.values()),
    "example_count_per_prompt": example_count,
    "random_dataset_count": random_dataset_count,
    "random_datasets": random.sample(all_datasets, min(random_dataset_count, len(all_datasets)))
}
