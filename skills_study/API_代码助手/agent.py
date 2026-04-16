"""
Agent 核心模块 - API 版本
支持通过 HTTP API 调用
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import dashscope
from typing import Optional, List

from config import DASHSCOPE_API_KEY, DEFAULT_MODEL


class AgentCore:
    """Agent 核心类"""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or DASHSCOPE_API_KEY
        self.model = model or DEFAULT_MODEL
        dashscope.api_key = self.api_key

    def call_llm(self, user_prompt: str, system_prompt: str = "", max_tokens: int = 2000) -> str:
        """调用 LLM"""
        try:
            response = dashscope.Generation.call(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=max_tokens,
                result_format="message"
            )

            if response.status_code == 200:
                return response.output.choices[0].message.content
            else:
                return f"错误：{response.code} - {response.message}"

        except Exception as e:
            return f"错误：{type(e).__name__} - {str(e)}"

    def chat(self, message: str, history: Optional[List[dict]] = None) -> str:
        """支持上下文的对话"""
        messages = history or []
        messages.insert(0, {"role": "system", "content": "你是专业的 Python 代码助手"})
        messages.append({"role": "user", "content": message})

        try:
            response = dashscope.Generation.call(
                model=self.model,
                messages=messages,
                max_tokens=2000,
                result_format="message"
            )

            if response.status_code == 200:
                return response.output.choices[0].message.content
            else:
                return f"错误：{response.code} - {response.message}"

        except Exception as e:
            return f"错误：{str(e)}"


# 全局实例
_agent_instance: Optional[AgentCore] = None


def get_agent() -> AgentCore:
    """获取全局 Agent 实例"""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = AgentCore()
    return _agent_instance
