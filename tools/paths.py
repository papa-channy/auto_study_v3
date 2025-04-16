# 📁 tools/paths.py

from pathlib import Path

# 🔹 프로젝트 루트
BASE_DIR = Path(__file__).resolve().parent.parent

# ───────── config ─────────
CONFIG_DIR = BASE_DIR / "config"
SETTING_JSON_PATH = CONFIG_DIR / "setting_config.json"
KEYWORDS_JSON_PATH = CONFIG_DIR / "keywords.json"
AVAILABLE_OPTION_PATH = CONFIG_DIR / "available_option.json"
STORAGE_POLICY_PATH = CONFIG_DIR / "storage_policy.json"

# ───────── examples ─────────
EXAMPLES_DIR = BASE_DIR / "examples"
EX_PDS_PATH = EXAMPLES_DIR / "ex_pds.json"
EX_SQL_PATH = EXAMPLES_DIR / "ex_sql.json"
EX_MPL_PATH = EXAMPLES_DIR / "ex_matplotlib.json"

# ───────── data ─────────
DATA_DIR = BASE_DIR / "data"
RAW_QUESTIONS_PATH = DATA_DIR / "raw_questions.txt"
CLEAN_QUESTIONS_PATH = DATA_DIR / "clean_questions.txt"
STRUCTURED_QUESTIONS_PATH = DATA_DIR / "questions.json"
QUESTIONS_XLSX_PATH = DATA_DIR / "questions.xlsx"
LLM_TAGS_PATH = DATA_DIR / "llm_tags.json"

# ───────── logs ─────────
LOG_DIR = BASE_DIR / "logs"
LOG_REPORT_DIR = LOG_DIR / "report"
LOG_PREPROCESS_FAIL_DIR = LOG_DIR / "preprocess_fails"
COMPARISON_JSON_PATH = LOG_DIR / "q_comparison_log.json"
COMPARISON_XLSX_PATH = LOG_DIR / "q_comparison_log.xlsx"

# ───────── notebooks ─────────
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
NOTEBOOK_PDS_PATH = NOTEBOOKS_DIR / "qpds.ipynb"
NOTEBOOK_SQL_PATH = NOTEBOOKS_DIR / "qsql.ipynb"
NOTEBOOK_VIZ_PATH = NOTEBOOKS_DIR / "qviz.ipynb"
NOTEBOOK_MPL_PATH = NOTEBOOKS_DIR / "matplotlib.ipynb"

# ───────── generator ─────────
GENERATOR_DIR = BASE_DIR / "generator"
PROMPT_DIR = GENERATOR_DIR / "prompt"
CORE_DIR = GENERATOR_DIR / "core"
POST_DIR = GENERATOR_DIR / "post"
FILE_GEN_DIR = GENERATOR_DIR / "file_gen"

# ───────── notion ─────────
NOTION_DIR = BASE_DIR / "notion"
NOTION_UPLOAD_PATH = NOTION_DIR / "notion_uploader.py"
SEC_PP_PATH = NOTION_DIR / "sec_pp.py"
SYNC_CHECKER_PATH = NOTION_DIR / "sync_checker.py"

# ───────── scripts / tools / setup ─────────
SCRIPTS_DIR = BASE_DIR / "scripts"
OPT_SET_PATH = SCRIPTS_DIR / "opt_set.py"
BASE_IMPORT_PATH = SCRIPTS_DIR / "base_import.py"

TOOLS_DIR = BASE_DIR / "tools"
ARCHIVER_PATH = TOOLS_DIR / "archiver.py"
CACHE_CLEANER_PATH = TOOLS_DIR / "clean_cache.py"
STORE_MANAGER_PATH = TOOLS_DIR / "store_manager.py"

SETUP_DIR = BASE_DIR / "setup"
