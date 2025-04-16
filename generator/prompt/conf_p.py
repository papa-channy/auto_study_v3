# 📁 generator/prompt/conf_p.py

def prompt_question_generation(kor_tool, dataset_line, difficulty_line, count):
    return f"""아래 조건에 따라 {kor_tool} 학습에 적합한 문제를 {count}개 생성해 주세요.

📊 사용 데이터셋: {dataset_line}
🎯 난이도 범위: {difficulty_line}
📝 문제는 한국어로 작성해 주세요.

✴️ 참고: 빅데이터 분석기사 시험에 출제되는 문제 유형을 참고해, 실제 출제 가능성이 높은 문제로 구성해 주세요.

📌 조건:
- 질문은 자연어 문장으로 구성하고 명령형 어미(하세요, 하시오 등)를 사용해 주세요.
- 배경 설명, 해설, 코드, 출력 예시는 포함하지 말고 질문 문장만 생성해 주세요.
"""

def prompt_enhance_difficulty(question: str):
    return f"""아래는 생성된 기본 문제입니다.  
이 문제의 난이도 수준이 명확히 드러나도록 다시 작성해 주세요.

🎯 요구사항:
1. 난이도 구간을 명확히 반영 (예: 중, 중상, 상, 최상)
2. 동일 주제를 유지하면서 더 어려운 방식으로 질문 구성
3. 명령형 문장 형태 유지 (ex. ~하세요, ~하시오)

--- 문제 원문 ---
{question}
"""

def prompt_enhance_reasoning(question: str):
    return f"""아래는 난이도 반영된 문제입니다.  
이 문제에 다음의 요소를 추가해, 사고력과 실무 응용력을 요구하는 고도화된 문제로 발전시켜 주세요.

🧠 요구사항:
1. 복합적인 추론이나 분석을 요구하도록 구성
2. 실무에서 접할 수 있는 시나리오 상황을 반영
3. 단순 통계나 시각화를 넘는 고차원적 사고를 유도

--- 문제 원문 ---
{question}
"""

def prompt_extract_tags(question: str):
    return f"""다음은 데이터 분석 관련 자연어 문제입니다.  
이 문제를 아래 포맷에 따라 분석하고, 해당 정보를 리스트로 추출해 주세요.

📌 출력 포맷:
[이 문제를 풀기 위해 필요한 학습 영역, 사용된 데이터셋명, 문제 난이도, 문제의 주요 키워드 목록]

📌 항목 설명:
- 학습 영역: pandas, sql, matplotlib 등 실질적으로 필요한 도구
- 데이터셋: 문제에서 실제로 언급된 dataset (예: titanic, iris 등)
- 난이도: 초급, 중급, 고급, 최상급 중 LLM이 판단한 수준
- 키워드: 이 문제에서 필요한 분석 기술, 개념 (예: groupby, 회귀, 시각화 등)

📝 문제:
{question}
"""
