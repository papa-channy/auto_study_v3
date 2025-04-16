# 📁 generator/core/q_classifier.py

from generator.prompt.p_gen import generate_prompt_extract_tags
from generator.core.q_raw_generator import generate_raw_questions

def classify_questions(o: list[dict], llm_name: str) -> list[list]:
    """
    ✅ o["question"] + d → i
    - 각 문제에 대해 분류 프롬프트 생성(n)
    - LLM에게 전달하여 분석 정보(i) 추출
    - 결과는 [tool, dataset, 난이도, 키워드리스트] 형식의 리스트로 구성됨
    """
    i = []

    for q in o:
        prompt = generate_prompt_extract_tags(q["question"])
        response = generate_raw_questions(prompt, llm_name)
        try:
            tags = eval(response[0]) if response else ["", "", "", []]
            if not isinstance(tags, list) or len(tags) < 4:
                raise ValueError
        except:
            tags = ["", "", "", []]

        i.append(tags)

    return i
