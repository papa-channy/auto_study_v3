# 📁 generator/core/q_main.py

import json
from tools.paths import SETTING_JSON_PATH
from generator.prompt.p_gen import generate_prompt_question
from generator.core.q_raw_generator import generate_raw_questions
from generator.core.q_enhancer import enhance_difficulty, enhance_reasoning
from generator.core.q_classifier import classify_questions
from generator.post.preprocess import preprocess_questions
from generator.post.prepro2 import structure_questions
from generator.post.connected_log import connect_setting_vs_llm

def run_pipeline():
    # 1️⃣ config 불러오기
    with open(SETTING_JSON_PATH, encoding="utf-8") as f:
        config = json.load(f)

    tool_list = list(config["study_matrix&difficulty"].keys())
    dataset_list = config["DATASET"]
    count = config["count"]
    llm = config["LLM"]

    all_o = []
    all_i = []
    all_p = []

    for tool in tool_list:
        kor_tool = tool.upper()
        difficulty_list = config["study_matrix&difficulty"][tool]
        recent_examples = "- (중) 샘플 예시 없음"  # 임시

        # j = a + e
        j = generate_prompt_question(kor_tool, dataset_list, difficulty_list, count, recent_examples)

        # f → g → h
        f = generate_raw_questions(j, llm)
        g = enhance_difficulty(f, llm)
        h = enhance_reasoning(g, llm)

        # h → m → o
        m = preprocess_questions(h)
        o = structure_questions(m, tool)

        # o["question"] + d → i
        i = classify_questions(o, llm)

        # o + i → p
        p = connect_setting_vs_llm(o, i)

        all_o.extend(o)
        all_i.extend(i)
        all_p.extend(p)

        print(f"✅ [{tool}] 처리 완료: {len(o)}문제")

    return all_o, all_i, all_p


if __name__ == "__main__":
    o, i, p = run_pipeline()

    print(f"\n🧩 전체 완료: {len(o)}문제 생성 / 비교 정보 {len(p)}건")
    print("-" * 50)
    for row in p[:3]:
        print(f"🔍 ID: {row['id']} | 예상: {row['tool']} vs LLM: {row['llm_tags']['tool']}")
