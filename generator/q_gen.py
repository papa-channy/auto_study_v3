# 📁 generator/q_gen.py

import os
from tools.paths import PROMPT_DIR, DATA_DIR
from LLM.llm_selector import call_llm  # 자유형 문제 생성용
from generator.q_post_format import format_questions  # 2차 호출용 (포맷 변환 함수)
from generator.q_gen_utils import reset_prompt_file  # 프롬프트 초기화 함수

def generate_all_questions(dataset_list, tool_list, difficulty_map, llm_name, count):
    for tool in tool_list:
        prompt_path = os.path.join(PROMPT_DIR, f"p_{tool}.txt")
        output_path = os.path.join(DATA_DIR, f"new_q_{tool}.txt")

        # 1️⃣ 자유 프롬프트 불러오기
        if not os.path.exists(prompt_path):
            print(f"❗ {tool} → 프롬프트 파일 없음: {prompt_path}")
            continue

        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read().strip()

        if not prompt:
            print(f"❗ {tool} 프롬프트 내용 없음, 건너뜀")
            continue

        print(f"🧠 [{tool}] 1차 문제 생성 중...")
        raw_response = call_llm(prompt, llm_name, temperature=1.0)
        print(f"🔍 [{tool}] 1차 응답 완료 → 포맷 변환 중...")

        # 2️⃣ 포맷 변환 (ex_format_pds.txt 참고)
        formatted = format_questions(tool, dataset_list[0], difficulty_map[tool], raw_response, llm_name)
        if not formatted:
            print(f"❌ [{tool}] 포맷 변환 실패")
            continue

        with open(output_path, "w", encoding="utf-8") as f:
            for line in formatted:
                f.write(line + "\n")

        print(f"✅ [{tool}] {len(formatted)}문제 저장 완료 → {os.path.basename(output_path)}")

        # 3️⃣ 프롬프트 초기화
        reset_prompt_file(tool)
