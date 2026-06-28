# settings.py - CRM系统配置文件

# 数据库配置
DB_PATH = "crm_app.db"

# 缓存配置
CACHE_TTL = 600  # 缓存过期时间（秒）

# 公海池配置
AUTO_RELEASE_TO_HIGH_SEAS = False  # 是否自动将客户释放到公海
HIGH_SEAS_DAYS_THRESHOLD = 30  # 多少天未跟进释放到公海

# 安全配置
MIN_PASSWORD_LENGTH = 6  # 最小密码长度
REQUIRE_STRONG_PASSWORD = True  # 是否要求强密码

# 业务配置
STAGES = ["初步洽谈", "方案报价", "商务谈判", "赢单成交"]
CUSTOMER_LEVELS = ["A(重点)", "B(普通)", "C(一般)"]
CUSTOMER_SOURCES = ["历史客户", "转介绍", "展会", "其它"]
CONTRACT_CLASSIFICATIONS = ["非密", "内部", "秘密", "机密", "绝密"]
BUSINESS_TYPES = ["J", "M", "K"]
BUSINESS_STATUS = {
    "active": "正常",
    "void": "已作废"
}

# 人月成本配置
WORK_DAYS_PER_MONTH = 21.75
WORK_HOURS_PER_DAY = 8
COST_PER_MONTH = 25000
