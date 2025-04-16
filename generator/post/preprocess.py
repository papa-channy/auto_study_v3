# 📁 generator/post/preprocess.py

import re
from datetime import datetime
from tools.paths import LOG_DIR

def clean_question(text: str) -> str:
    """
    ✅ 접두어 제거 + 줄 정리
    """
    prefixes = ["Q.", "Q:", "문제", "1.", "2.", "-", "*"]
    text = text.strip()
    for prefix in prefixes:
        if text.lower().startswith(prefix.lower()):
            text = text[len(prefix):].strip()
    return text

def is_english_only(text: str) -> bool:
    """
    ✅ 영어-only 여부 판단 (한글 포함 안된 경우)
    """
    return re.fullmatch(r"[a-zA-Z0-9\s\.\,\-\!\?\(\)\[\]\"']+", text) is not None

def preprocess_questions(h: list[str], log_fail: bool = True) -> list[str]:
    """
    ✅ h → m 변환
    - 유효 질문만 추출
    - 제거된 질문은 로그 기록
    """
    m = []
    removed = []

    for q in h:
        original = q.strip()
        cleaned = clean_question(original)

        if not cleaned:
            removed.append(("빈문장", original))
        elif len(cleaned) < 8:
            removed.append(("너무 짧음", original))
        elif is_english_only(cleaned):
            removed.append(("영어-only", original))
        else:
            m.append(cleaned)

    # 로그 저장
    if log_fail and removed:
        now = datetime.now().strftime("%Y%m%d_%H%M")
        log_file = LOG_DIR / f"preprocess_fail_{now}.txt"
        with open(log_file, "w", encoding="utf-8") as f:
            for reason, text in removed:
                f.write(f"[⛔ {reason}]\n{text}\n\n")
        print(f"🧹 전처리 로그 저장 완료 → {log_file.name}")

    print(f"✅ preprocess 완료: {len(m)}개 정제됨 / 제거 {len(removed)}개")
    return m
