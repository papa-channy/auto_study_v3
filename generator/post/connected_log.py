# 📁 generator/post/connected_log.py

def connect_setting_vs_llm(o: list[dict], i: list[list]) -> list[dict]:
    """
    ✅ o + i → p
    - 각 문제에 대해 설정값과 LLM 판단값을 통합 저장
    - i는 [[tool, dataset, 난이도, 키워드리스트], ...] 형태
    """
    result = []
    for q, tags in zip(o, i):
        if not isinstance(tags, list) or len(tags) < 4:
            tags = ["", "", "", []]

        result.append({
            "tool": q["tool"],
            "dataset": q["dataset"],
            "difficulty": q["difficulty"],
            "category": q["category"],
            "id": q["id"],
            "llm_tags": {
                "tool": tags[0],
                "dataset": tags[1],
                "difficulty": tags[2],
                "keywords": tags[3]
            }
        })

    return result
