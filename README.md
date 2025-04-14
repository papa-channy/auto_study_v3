#  📚 초보 개발자가 만든 auto_study(학습자동화) 프로젝트

## 🔧 프로젝트 목적
`auto_study`는 데이터 분석 학습을 위한 문제를 **GPT 기반 LLM**을 통해 자동으로 생성하고,
Notion에 자동 업로드하며, 정리된 문제를 `.ipynb` 파일로 변환해주는 **AI 기반 학습 자동화 시스템**입니다.

이 시스템은 학습자의 목적에 맞게 난이도/도구/데이터셋을 설정하여 자유롭게 문제를 생성하고,
바로 실행 가능한 노트북 파일로 만들어주며, 복습 기록도 Notion에 정리해 줍니다.

---

## 🚀 핵심 기능 요약

### ✅ 1. 자동 문제 생성
- 사용자가 선택한 도구(pandas/sql/시각화 등), 난이도, 데이터셋을 기반으로 문제 생성
- 다양한 LLM(Groq, OpenAI, Claude 등) 중 선택 가능
- 설정 파일 기반으로 완전 자동 실행 가능

### ✅ 2. 프롬프트 고도화 (ver_3 기준)
- 자유형 프롬프트로 1차 LLM 호출 → 문제 아이디어 생성
- 구조화된 포맷(`번호|난이도|데이터셋|카테고리|질문`)으로 2차 변환 요청
- 기존 `ex_format_*.txt` 예시를 활용하여 형식 안정성 확보

### ✅ 3. 노션 자동 업로드
- 문제는 Notion의 데이터베이스에 자동 업로드됨
- 날짜, 난이도, 데이터셋, 카테고리, 상태(select) 등을 자동 분류
- 업로드 오류 최소화를 위해 '|' 기준 파싱 방식 적용

### ✅ 4. Jupyter 노트북 자동 생성
- 각 도구별로 문제를 누적 기록한 `.ipynb` 파일 자동 생성 (ex: qpds.ipynb)
- 문제 설명과 함께 `sns.load_dataset()` 예시 삽입 → 바로 실행 가능
- pandas/sql/시각화 도구별로 구조화된 코드 블럭 구성

### ✅ 5. 정리 및 캐시 자동화
- 문제 생성 후 new_q_*.txt → archived_q_*.txt 로 이관
- 최근 예시는 ex_*.txt 파일에 자동 축적 (최대 3개 유지)
- 사용한 프롬프트는 자동 초기화
- 캐시 디렉토리(`__pycache__`, *.pyc) 자동 삭제 스크립트 포함

---

## 🧩 폴더 구조 요약

```
📦 auto_study_v3
├── config/                 # 설정 파일, 설정 가능한 옵션 목록 관리
├── data/                   # 문제 저장 (new_q, archived_q 등)
├── generator/              # 문제 생성 및 포맷 변환 로직 (p_gen, q_gen, q_post_format 등)
│   └── file_gen/           # txt, py, ipynb 파일 생성기
├── LLM/                    # 각 LLM별 call_llm 함수 정의
├── notion/                 # preprocess.py + Notion 업로더
├── notebooks/              # 누적된 학습용 노트북 저장소 (도구별)
├── prompt/                 # 도구별 프롬프트 템플릿 저장 (p_pds.txt 등)
├── recent_ex/              # 예시 문제 저장 (ex_*.txt + ex_format_*.txt)
├── scripts/                # run_all.py 및 사용자 설정 관리 스크립트
├── tools/                  # 공용 유틸 함수 및 경로 설정, 정리(log, archive, clean_cache 등)
├── setup/                  # cron 등록, git 자동 커밋 스크립트
```

---

## 🧠 실행 흐름 (`scripts/run_all.py` 기준)

```text
1. 📥 설정 로딩 (setting_config.json)
2. 🧾 자유형 프롬프트 생성 (도구별 recent 예시 기반)
3. 🧠 1차 LLM 호출 → 자유 문제 생성
4. 🔁 2차 LLM 호출 → 구조화된 포맷으로 변환
5. 💾 new_q_*.txt 에 문제 저장
6. 🔎 preprocess.py → 문제를 '|' 기준으로 파싱
7. 📤 Notion에 업로드
8. 🧪 ipynb 파일 자동 생성 (코드+설명 포함)
9. 📦 문제 아카이브 + 최근 예시 업데이트
10. 🧼 캐시 및 로그 정리 (report, pycache 등)
```

---

## ⚙️ 주요 설정 파일 및 텍스트

| 파일 | 설명 |
|------|------|
| `setting_config.json` | 사용자 설정값 요약 (dataset/tool/difficulty/llm/file_type/count 등) |
| `available_option/*.txt` | 선택 가능한 옵션 목록 (datasets.txt, study_matrix.txt 등) |
| `count.txt` | 도구별 문제 생성 시 LLM 호출 횟수 |
| `ex_format_*.txt` | 구조화 포맷 변환 참고 예시 (업데이트 없음, 고정 예시) |

---

## ✅ 시스템 특징 정리

- ⛓ 완전 자동화: 설정만 해두면 문제 생성~정리까지 자동 처리
- 🔄 유연한 프롬프트: 자유형 질문 생성 및 포맷화 분리로 품질 향상
- 🧠 LLM 교체 쉬움: Groq, OpenAI, Claude 등 자유롭게 교체 가능
- 🧪 실행 즉시 학습 가능: `load_dataset()` 자동 포함된 ipynb 생성
- 🔐 Git 환경 최적화: CRLF 문제 자동 해결 (`.gitattributes`, `git_auto.sh` 포함)

---

## 💡 향후 계획 (ver_4 미리보기)

- 🧠 정답 자동 생성 + 정답 평가 기능 (코드 기반 평가)
- 📤 업로드된 문제 중 '미풀이' 문제만 골라 재학습 요청
- 🔄 구조 변경 없이 설정만으로 새로운 도구 추가 기능
- 📊 사용자 풀이 통계 기록 및 Notion 연동
- 🎯 토픽별 큐레이션 기능 (주제/카테고리 기반 추천 문제)

---

> Made with ❤️ by 찬 - auto_study 프로젝트는 확장성과 실용성을 위해 계속 발전 중입니다!

