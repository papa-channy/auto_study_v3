# 📁 config/conf_p.py

def prompt_question_generation(kor_tool, dataset_line, difficulty_line, count):
    return f"""다음 조건에 맞춰 {kor_tool} 학습에 적합한 문제를 {count}개 생성해 주세요.

📌 목적: 실제 현업 또는 시험 대비를 위한 자연어 문제 생성

📊 사용 가능한 데이터셋: {dataset_line}
🎯 난이도 범위: {difficulty_line}

✅ 요구 사항:
- 문제는 반드시 **한글**로 작성할 것
- 문제는 한 문장 또는 한 문단으로 끝나는 **질문형 문장**일 것
- 명령형 종결어미 사용 (예: ~하세요, ~하시오, ~구하세요 등)
- 배경 설명, 해설, 코드, 출력 예시는 포함하지 말 것

💡 참고:
- 빅데이터 분석기사 시험에 출제된 문제 유형을 참고해
  실제 출제 가능성 있는 형태로 구성해 주세요.
"""

def prompt_difficulty_enhancement(answer_a):
    return f"""아래는 초안으로 작성된 데이터 분석 문제입니다.

이 문제에 아래 조건을 반영하여 **난이도에 따라 고도화된 문제**로 다시 작성해 주세요:

1. 난이도 구간을 명확히 반영 (중, 상, 최상 등)
2. **추론**, **응용**, **복합 분석** 요소를 반드시 포함
3. 실제 실무 시나리오나 현업 상황에서 마주칠 수 있는 맥락을 반영

--- 문제 초안 ---
{answer_a}
"""

def prompt_format_conversion(answer_a_dash):
    return f"""다음은 고도화된 자연어 질문입니다.  
이 내용을 아래 예시에 맞춰 구조화된 JSON 형식으로 변환해 주세요.

🎯 목적: 시스템에 자동 저장하기 위한 포맷 정제

요구 포맷 예시:
{{
  "question": "...",
  "difficulty": "...",
  "dataset": "...",
  "category": "기타"
}}

📝 주의:
- JSON 형식 오류 없이 완전하게 작성해 주세요
- 키 순서는 유지하고, 문자열은 "..." 형태로 감싸 주세요

--- 변환 대상 ---
{answer_a_dash}
"""
