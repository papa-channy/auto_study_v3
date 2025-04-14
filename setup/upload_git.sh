#!/bin/bash
clear

# 📦 Git 자동 커밋 & 푸시 스크립트
# 🎨 색상 정의
RED='\033[1;31m'; GREEN='\033[1;32m'; YELLOW='\033[1;33m'
BLUE='\033[1;34m'; MAGENTA='\033[1;35m'; CYAN='\033[1;36m'; NC='\033[0m'
divider="────────────────────────────────────────────"

# 📦 출력 도우미
print_msg() { echo -e "${1}${2}${NC}"; }

# ❗ 에러 안내 박스
handle_error() {
    print_msg "$RED" "❌ $1"
    echo -e "${MAGENTA}$divider${NC}"
    echo "$2"
    echo -e "${MAGENTA}$divider${NC}"
}

# 💡 친절한 해결 안내
show_solution() {
    print_msg "$YELLOW" "📢 문제: $1"
    print_msg "$CYAN" "💡 해결 방법:"
    shift
    for line in "$@"; do echo "$line"; done
}

# 📝 커밋 로그 저장 함수
save_commit_log() {
    log_file=".git_commit_log.txt"
    {
        echo "[$(date '+%Y-%m-%d %H:%M:%S')]"
        echo "브랜치: $branch"
        echo "메시지: $commit_message"
        echo "결과: $1"
        echo "$divider"
    } >> "$log_file"
}

# 1️⃣ Git 설정 자동 적용
print_msg "$CYAN" "1️⃣   Git 설정 점검 및 자동 적용 중..."
autocrlf=$(git config --global core.autocrlf)
[[ "$autocrlf" != "input" ]] && git config --global core.autocrlf input && echo "✅ core.autocrlf = input 설정 완료"
quotepath=$(git config --global core.quotepath)
[[ "$quotepath" != "false" ]] && git config --global core.quotepath false && echo "✅ core.quotepath = false 설정 완료"

name=$(git config --global user.name)
email=$(git config --global user.email)
if [[ -z "$name" || -z "$email" ]]; then
  echo -e "\n⚠️ 사용자 정보가 없어 입력을 받습니다."
  read -p "👤 이름: " name; read -p "📧 이메일: " email
  git config --global user.name "$name"
  git config --global user.email "$email"
  echo "✅ 사용자 정보 등록 완료: $name <$email>"
else
  echo "✅ 사용자 정보: $name <$email>"
fi

# 2️⃣ CRLF/LF 문제 예방 설정 파일 생성
print_msg "$CYAN" "2️⃣   CRLF/LF 방지용 설정 파일 생성 중..."
if [[ ! -f .gitattributes ]]; then
  echo "* text=auto" > .gitattributes
  echo "✅ .gitattributes 파일 생성 완료"
fi

if [[ ! -f .editorconfig ]]; then
  cat <<EOL > .editorconfig
[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8
EOL
  echo "✅ .editorconfig 파일 생성 완료"
fi

# ✨ .gitignore 줄바꿈 정리 (CRLF → LF)
if command -v dos2unix &> /dev/null; then
  dos2unix .gitignore 2>/dev/null
  echo "✅ .gitignore 줄바꿈(LF) 정리 완료"
fi

# 🧾 커밋 로그 파일 생성 및 .gitignore 등록
if [[ ! -f .git_commit_log.txt ]]; then
    touch .git_commit_log.txt
    echo "✅ .git_commit_log.txt 파일 생성 완료"
fi

if [[ ! -f .gitignore ]]; then
    echo ".git_commit_log.txt" > .gitignore
    echo "✅ .gitignore 생성 및 로그 파일 등록 완료"
elif ! grep -q ".git_commit_log.txt" .gitignore; then
    echo ".git_commit_log.txt" >> .gitignore
    echo "✅ .gitignore에 로그 파일 경로 추가 완료"
fi

# 3️⃣ Git 저장소 확인
print_msg "$CYAN" "3️⃣   현재 위치 확인 중..."
git rev-parse --is-inside-work-tree &>/dev/null || {
  handle_error "현재 디렉토리에 Git 저장소가 없어요!" "git init 또는 git clone <URL> 후 다시 실행해 주세요."
  exit 1
}

# 4️⃣ 변경사항 확인 및 병합 충돌 검사
[[ -z "$(git status -s)" ]] && print_msg "$GREEN" "✅  변경된 파일이 없어요!" && exit 0

if git ls-files -u | grep . &>/dev/null; then
  handle_error "병합 충돌이 감지되었어요!" "충돌 파일을 수정하고 git add 후 다시 실행하세요."
  exit 1
fi

if [[ -f ".git/index.lock" ]]; then
  show_solution "index.lock 파일이 남아있어요" \
    "1️⃣  삭제: rm -f .git/index.lock" "2️⃣  다시 실행해 주세요."
  exit 1
fi

# 5️⃣ 커밋 메시지 입력
print_msg "$BLUE" "🔍  변경된 파일 목록"; git status -s; echo ""
read -p "✏️   커밋 메시지를 입력하세요 (엔터 → 자동 메시지): " commit_message
branch=$(git rev-parse --abbrev-ref HEAD)
timestamp=$(TZ=Asia/Seoul date "+%Y-%m-%d %H:%M")
os_type=$(uname)
default_message="🚀  [$branch] auto commit | $timestamp | $os_type"
commit_message="${commit_message:-$default_message}"

clear
# 6️⃣ 커밋 실행
git add .
commit_output=$(git commit -m "$commit_message" 2>&1)
commit_status=$?

if [ $commit_status -ne 0 ]; then
    handle_error "커밋 중 오류가 발생했어요!" "$commit_output"
    save_commit_log "❌ 실패 - $commit_output"

    if echo "$commit_output" | grep -q "Permission denied"; then
        show_solution "파일 시스템 권한 문제" \
            "1️⃣  파일이 현재 사용자 계정 소유인지 확인: ${CYAN}ls -l${NC}" \
            "2️⃣  필요시 소유권 변경: ${CYAN}sudo chown -R 사용자명 .${NC}" \
            "3️⃣  다시 실행해 주세요."
    elif echo "$commit_output" | grep -q "unable to write new index file"; then
        show_solution "디스크 쓰기 오류" \
            "1️⃣  디스크 용량 확인: ${CYAN}df -h${NC}" \
            "2️⃣  권한 문제일 수도 있으니 권한 확인"
    elif echo "$commit_output" | grep -q "Unable to create '.git/index.lock'"; then
        show_solution "다른 Git 작업이 충돌 중이에요." \
            "1️⃣  lock 파일 삭제: ${CYAN}rm -f .git/index.lock${NC}" \
            "2️⃣  이후 다시 시도해 주세요."
    elif echo "$commit_output" | grep -q "fatal:"; then
        show_solution "치명적인 Git 오류(fatal)가 발생했어요." \
            "1️⃣  위 로그를 확인해 주세요." \
            "2️⃣  필요한 경우 터미널에 직접 명령을 실행해 원인을 파악해 주세요."
    else
        print_msg "$YELLOW" "📢  예상치 못한 커밋 오류입니다. 위 로그를 확인해 주세요."
    fi
    exit 1
fi

save_commit_log "✅  성공"

# 🌐 원격 저장소 확인
remote_url=$(git config --get remote.origin.url)
if [ -z "$remote_url" ]; then
    print_msg "$RED" "❌ 원격 저장소(remote.origin.url)가 설정되어 있지 않아요!"
    show_solution "Push를 하려면 원격 저장소 주소가 필요해요." \
        "1️⃣  원격 저장소 추가: ${CYAN}git remote add origin <URL>${NC}" \
        "2️⃣  또는 설정 확인: ${CYAN}git remote -v${NC}"
    exit 1
fi

# 🌐 원격 저장소 접근 테스트
if ! git ls-remote "$remote_url" &> /dev/null; then
    print_msg "$RED" "❌ 원격 저장소에 연결할 수 없어요."
    show_solution "네트워크 또는 인증 문제일 수 있어요." \
        "1️⃣  인터넷 연결 확인" \
        "2️⃣  remote URL 확인: ${CYAN}git remote -v${NC}" \
        "3️⃣  인증 토큰 또는 SSH 키 확인"
    exit 1
fi

# 🚀 Push 실행
push_output=$(git push 2>&1)
push_status=$?

if [ $push_status -ne 0 ]; then
    handle_error "푸시 도중 문제가 발생했어요!" "$push_output"

    if echo "$push_output" | grep -qi "permission denied"; then
        show_solution "원격 저장소에 푸시 권한이 없어요." \
            "1️⃣  계정 권한 확인" \
            "2️⃣  SSH 키 또는 Personal Access Token 설정 확인"
    elif echo "$push_output" | grep -qi "Could not resolve host"; then
        show_solution "원격 저장소 주소를 찾을 수 없어요." \
            "1️⃣  인터넷 연결 확인" \
            "2️⃣  DNS 설정 또는 오타 확인"
    elif echo "$push_output" | grep -qi "failed to connect to"; then
        show_solution "네트워크 연결에 실패했어요." \
            "1️⃣  VPN/방화벽 확인" \
            "2️⃣  Git 서버 접근 차단 여부 확인"
    else
        print_msg "$YELLOW" "📢 예상치 못한 푸시 오류입니다. 위 로그를 참고해 주세요."
    fi
    exit 1
fi

# 🎉 종료 메시지
print_msg "$GREEN" "✅  모든 작업이 성공적으로 완료되었습니다!"
print_msg "$CYAN" "✏️   커밋 메시지: $commit_message"
print_msg "$CYAN" "🌈  잘 반영되었어요. 수고했어요 ! ☕"
echo ""
