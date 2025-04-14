import os

def clean_all_cache(tool_list=None):
    """
    🧹 전체 디렉토리에서 __pycache__ 및 *.pyc 삭제
    """
    removed = 0
    for root, dirs, files in os.walk("."):
        for dirname in dirs:
            if dirname == "__pycache__":
                full_path = os.path.join(root, dirname)
                os.system(f"rm -rf \"{full_path}\"")
                print(f"🗑️  삭제됨: {full_path}")
                removed += 1
        for file in files:
            if file.endswith(".pyc"):
                full_path = os.path.join(root, file)
                os.remove(full_path)
                removed += 1

    print(f"🧼 캐시 정리 완료! 삭제된 파일/폴더: {removed}개")
