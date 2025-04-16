import json
from config.derived_config import DERIVED_CONFIG
from tools.paths import EX_JSON_PATH, PROMPT_PATH

# 🔤 도구명 한글 매핑
tool_name_map = {
    "pds": "pandas 라이브러리",
    "sql": "SQL",
    "viz": "시각화"
}

def convert_tool_to_kor(tool):
    return tool_name_map.get(tool, tool)


def load_recent_examples(tool):
    """최근 예시 로딩 (ex.json 기준, 최대 5개)"""
    if not EX_JSON_PATH.exists():
        return "# 예시 없음"

    with open(EX_JSON_PATH, encoding="utf-8") as f:
        ex_data = json.load(f)

    examples = ex_data.get(tool, [])
    if not examples:
        return "# 예시 없음"

    # 🔧 examples가 문자열 리스트일 경우
    if isinstance(examples[0], str):
        return "\n\n".join(examples)

    # 🔧 examples가 dict 리스트일 경우 (이전 버전 대비 호환)
    return "\n\n".join(q.get("question", "") for q in examples if isinstance(q, dict) and q.get("question"))




def format_freestyle_prompt(tool, dataset_list, difficulty_list, count, examples):
    kor_tool = convert_tool_to_kor(tool)
    dataset_line = ", ".join(dataset_list)
    difficulty_line = ", ".join(difficulty_list)

    prompt = f"""아래 조건에 따라 {kor_tool} 학습에 적합한 문제를 {count}개 생성해 주세요.

📊 사용 데이터셋: {dataset_line}
🎯 난이도 범위: {difficulty_line}
📝 문제는 한국어로 작성해 주세요.
✴️ 참고: 빅데이터 분석기사 시험에 출제되는 문제 유형을 참고해 난이도에 맞게 수정해서 문제를 구성해주세요.
---

📌 최근 예시:
{examples}
"""
    return prompt


def update_prompt_templates(tool_list, dataset_list, difficulty_map, count):
    """자유형 프롬프트 생성기 (prompt.json 단일 저장 방식)"""
    prompt_dict = {}

    for tool in tool_list:
        difficulty_list = difficulty_map.get(tool, [])
        examples = load_recent_examples(tool)
        prompt = format_freestyle_prompt(tool, dataset_list, difficulty_list, count, examples)
        prompt_dict[tool] = prompt
        print(f"📄 [{tool}] 프롬프트 생성 완료")

    with open(PROMPT_PATH, "w", encoding="utf-8") as f:
        json.dump(prompt_dict, f, indent=2, ensure_ascii=False)
