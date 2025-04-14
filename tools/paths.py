import os

# 📁 루트 기준 경로
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 🔧 CONFIG
CONFIG_DIR = os.path.join(BASE_DIR, "config")
SETTING_JSON_PATH = os.path.join(CONFIG_DIR, "setting_config.json")
KEYWORDS_JSON_PATH = os.path.join(CONFIG_DIR, "keywords.json")

# 📂 AVAILABLE OPTIONS
OPTION_DIR = os.path.join(CONFIG_DIR, "available_option")
DATASETS_PATH = os.path.join(OPTION_DIR, "datasets.txt")
LLMS_TXT_PATH = os.path.join(OPTION_DIR, "llms.txt")
TOOLS_PATH = os.path.join(OPTION_DIR, "study_matrix.txt")
DIFFICULTY_PATH = os.path.join(OPTION_DIR, "difficulty.txt")
COUNT_PATH = os.path.join(OPTION_DIR, "count.txt")
FILE_TYPE_PATH = os.path.join(OPTION_DIR, "file_type.txt")

# 📁 DATA (문제 저장 관련)
DATA_DIR = os.path.join(BASE_DIR, "data")
NEW_Q_PATH = os.path.join(DATA_DIR, "new_q.txt")
ARCHIVED_Q_PATH = os.path.join(DATA_DIR, "archived_q.txt")
NEW_Q_PDS_PATH = os.path.join(DATA_DIR, "new_q_pds.txt")
NEW_Q_SQL_PATH = os.path.join(DATA_DIR, "new_q_sql.txt")
NEW_Q_VIZ_PATH = os.path.join(DATA_DIR, "new_q_viz.txt")
ARCHIVED_Q_PDS_PATH = os.path.join(DATA_DIR, "archived_q_pds.txt")
ARCHIVED_Q_SQL_PATH = os.path.join(DATA_DIR, "archived_q_sql.txt")
ARCHIVED_Q_VIZ_PATH = os.path.join(DATA_DIR, "archived_q_viz.txt")

# 📁 GENERATOR
GENERATOR_DIR = os.path.join(BASE_DIR, "generator")
Q_GEN_PATH = os.path.join(GENERATOR_DIR, "q_gen.py")
P_GEN_PATH = os.path.join(GENERATOR_DIR, "p_gen.py")

# 📁 FILE GEN (파일 생성기 모듈 위치)
FILE_GEN_DIR = os.path.join(GENERATOR_DIR, "file_gen")
TXT_GEN_PATH = os.path.join(FILE_GEN_DIR, "txt_gen.py")
PY_GEN_PATH = os.path.join(FILE_GEN_DIR, "py_gen.py")
IPYNB_GEN_PATH = os.path.join(FILE_GEN_DIR, "ipynb_gen.py")

# 📁 LLM (LLM 모듈들)
LLM_DIR = os.path.join(BASE_DIR, "LLM")
LLM_GROQ_PATH = os.path.join(LLM_DIR, "llama3_groq.py")
LLM_OPENAI_PATH = os.path.join(LLM_DIR, "gpt_openai.py")
LLM_OPR_PATH = os.path.join(LLM_DIR, "claude_opr.py")

# 📁 PROMPT
PROMPT_DIR = os.path.join(BASE_DIR, "prompt")
P_PDS_PATH = os.path.join(PROMPT_DIR, "p_pds.txt")
P_SQL_PATH = os.path.join(PROMPT_DIR, "p_sql.txt")
P_VIZ_PATH = os.path.join(PROMPT_DIR, "p_viz.txt")

# 📁 RECENT EXAMPLES
RECENT_EX_DIR = os.path.join(BASE_DIR, "recent_ex")
EX_PDS_PATH = os.path.join(RECENT_EX_DIR, "ex_pds.txt")
EX_SQL_PATH = os.path.join(RECENT_EX_DIR, "ex_sql.txt")
EX_VIZ_PATH = os.path.join(RECENT_EX_DIR, "ex_viz.txt")

# 📁 NOTION
NOTION_DIR = os.path.join(BASE_DIR, "notion")
PREPROCESS_PATH = os.path.join(NOTION_DIR, "preprocess.py")
UPLOADER_PATH = os.path.join(NOTION_DIR, "notion_uploader.py")

# 📁 NOTEBOOK
NOTEBOOK_DIR = os.path.join(BASE_DIR, "notebooks")

# 📁 LOGS
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 📁 SCRIPTS
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
RUN_ALL_PATH = os.path.join(SCRIPTS_DIR, "run_all.py")
CUSTOM_SETTING_PATH = os.path.join(SCRIPTS_DIR, "custom_setting.py")
OPTION_ADMIN_PATH = os.path.join(SCRIPTS_DIR, "option_admin.py")
BASE_IMPORT_PATH = os.path.join(SCRIPTS_DIR, "base_import.py")

# 📁 SETUP
SETUP_DIR = os.path.join(BASE_DIR, "setup")
CRON_SCRIPT_PATH = os.path.join(SETUP_DIR, "auto_cron.sh")
GIT_SCRIPT_PATH = os.path.join(SETUP_DIR, "git_auto.sh")

# 📁 ENV
ENV_PATH = os.path.join(BASE_DIR, ".env")
