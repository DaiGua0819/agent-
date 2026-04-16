"""
配置模块
"""
import os

# 阿里云 DashScope API Key
# 请设置环境变量 DASHSCOPE_API_KEY，或在本地创建 .env 文件
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")

if not DASHSCOPE_API_KEY:
    raise ValueError("请设置环境变量 DASHSCOPE_API_KEY")

# 默认模型 (阿里云百炼)
DEFAULT_MODEL = "qwen-plus"

# 默认最大 token 数
MAX_TOKENS = 2000

# 阿里云 API 端点
API_BASE_URL = "https://dashscope.aliyuncs.com/api/v1"
