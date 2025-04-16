# 📁 opt_admin/excel2json.py

import os
import json
import pandas as pd

# 📌 엑셀 파일 → ex_format.json 변환기

def convert_excel_to_json(excel_path, output_path):
    """
    📥 엑셀 파일 내 시트들을 읽어서 하나의 리스트로 합쳐서 저장합니다.
    각 시트는 도구명(pds, sql, viz 등)에 해당하며, 'tool' 필드로 구분 추가함
    """
    if not os.path.exists(excel_path):
        print(f"❌ 엑셀 파일이 존재하지 않아요: {excel_path}")
        return

    xls = pd.ExcelFile(excel_path)
    all_records = []

    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        df = df.dropna(how="all")
        df["tool"] = sheet_name  # 시트명을 tool 필드로 추가
        records = df.to_dict(orient="records")
        all_records.extend(records)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_records, f, ensure_ascii=False, indent=2)

    print(f"✅ 변환 완료 → {output_path} (총 {len(all_records)}개 항목)")


# ▶️ 실행 예시
if __name__ == "__main__":
    excel_file = "config/ex_format.xlsx"
    output_file = "recent_ex/ex_format.json"

    convert_excel_to_json(excel_file, output_file)
