import json
import random

from config.derived_config import DERIVED_CONFIG
from tools.paths import QUESTIONS_PATH, PROMPT_PATH, SETTING_PATH
from generator.q_gen_utils import parse_llm_response
from LLM.llm_selector import generate_by_llm

def generate_all_questions():
    """
    ✅ derived_config 기반 문제 자동 생성기
    - 도구별 난이도 × 호출횟수 만큼 LLM 호출
    - prompt.json 참조하여 프롬프트 기반 생성
    - questions.json에 누적 저장
    """
    tool_summary = DERIVED_CONFIG["tool_summary"]
    selected_datasets = DERIVED_CONFIG["random_datasets"]

    # LLM 이름 가져오기
    with open(SETTING_PATH, encoding="utf-8") as f:
        config = json.load(f)
    llm_name = config.get("LLM", "groq")

    # 1️⃣ 프롬프트 로딩
    with open(PROMPT_PATH, encoding="utf-8") as f:
        prompts = json.load(f)

    all_questions = []

    for tool, info in tool_summary.items():
        prompt = prompts.get(tool)
        if not prompt:
            print(f"⚠️ 프롬프트 누락: {tool}")
            continue

        print(f"\n🚀 [{tool.upper()}] 문제 생성 중...")

        for level in info["difficulties"]:
            for _ in range(info["calls"]):
                dataset = random.choice(selected_datasets)

                # 🔥 LLM 호출 (tool, count 인자 제거됨)
                raw = generate_by_llm(prompt, llm_name=llm_name)
                parsed = parse_llm_response(raw, tool)

                # 메타정보 부여
                for q in parsed:
                    q["tool"] = tool
                    q["dataset"] = dataset
                    q["difficulty"] = level

                all_questions.extend(parsed)

    # 2️⃣ 결과 저장
    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 전체 문제 {len(all_questions)}개 저장 완료 (📁 questions.json)")
