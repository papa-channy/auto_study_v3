from pathlib import Path

# 🔹 프로젝트 최상위 디렉토리
BASE_DIR = Path(__file__).resolve().parent.parent

# ───────────────────────────────────────────────
# 📁 config 관련
CONFIG_DIR = BASE_DIR / "config"
SETTING_PATH = CONFIG_DIR / "setting_config.json"
KEYWORDS_PATH = CONFIG_DIR / "keywords.json"
AVAILABLE_OPTION_PATH = CONFIG_DIR / "available_option.json"
ENV_PATH = BASE_DIR / ".env"
KEYWORDS_JSON_PATH = CONFIG_DIR / "keywords.json"
EX_FORMAT_XLSX_PATH = CONFIG_DIR / "ex_format.xlsx"

# ───────────────────────────────────────────────
# 📁 data (생성된 문제 / 프롬프트 / 전체 아카이브)
DATA_DIR = BASE_DIR / "data"
QUESTIONS_PATH = DATA_DIR / "questions.json"
PROMPT_PATH = DATA_DIR / "prompt.json"
ARCHIVE_PATH = DATA_DIR / "archive.xlsx"
ARCHIVE_QUESTION_TXT_PATH = DATA_DIR / "archive_questions.txt"
ARCHIVE_QUESTION_LOG_PATH = DATA_DIR / "archive_question_log.txt"

# ───────────────────────────────────────────────
# 📁 examples (예시)
EXAMPLES_DIR = BASE_DIR / "examples"
EX_JSON_PATH = EXAMPLES_DIR / "ex.json"
EX_FORMAT_JSON_PATH = EXAMPLES_DIR / "ex_format.json"

# ───────────────────────────────────────────────
# 📁 notebooks
NOTEBOOK_DIR = BASE_DIR / "notebooks"
NOTEBOOK_PDS_PATH = NOTEBOOK_DIR / "qpds.ipynb"
NOTEBOOK_SQL_PATH = NOTEBOOK_DIR / "qsql.ipynb"
NOTEBOOK_VIZ_PATH = NOTEBOOK_DIR / "qviz.ipynb"

# ───────────────────────────────────────────────
# 📁 logs (리포트 & 예시 아카이브)
LOG_DIR = BASE_DIR / "logs"
LOG_REPORT_DIR = LOG_DIR / "report"
EX_ARCHIVE_PATH = LOG_DIR / "ex_archive.xlsx"

# ───────────────────────────────────────────────
# 📁 opt_set (설정 도우미)
OPT_SET_DIR = BASE_DIR / "opt_set"
CUSTOM_SETTING_PATH = OPT_SET_DIR / "custom_setting.py"
OPTION_ADMIN_PATH = OPT_SET_DIR / "option_admin.py"
ADD_PATH = OPT_SET_DIR / "add.py"
EXCEL2JSON_PATH = OPT_SET_DIR / "excel2json.py"

# ───────────────────────────────────────────────
# 🛠 기타 (setup, tools, scripts 등은 필요시만 지정)
SETUP_DIR = BASE_DIR / "setup"
SCRIPTS_DIR = BASE_DIR / "scripts"
TOOLS_DIR = BASE_DIR / "tools"
NOTION_DIR = BASE_DIR / "notion"
GENERATOR_DIR = BASE_DIR / "generator"
