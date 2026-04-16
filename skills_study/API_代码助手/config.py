"""
配置模块
"""
import os

# 阿里云 DashScope API Key
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")

if not DASHSCOPE_API_KEY:
    raise ValueError("请设置环境变量 DASHSCOPE_API_KEY")

# 默认模型
DEFAULT_MODEL = "qwen-plus"

# 服务配置
HOST = "0.0.0.0"
PORT = 8000
