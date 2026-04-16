"""
Agent 核心模块 - 支持阿里云 DashScope
"""
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

import dashscope
from typing import Optional

from agent.prompt import SYSTEM_PROMPT
from config import DASHSCOPE_API_KEY, DEFAULT_MODEL, MAX_TOKENS


class AgentCore:
    """
    Agent 核心类
    负责与 LLM 交互，处理请求并返回结果
    """

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        初始化 Agent

        Args:
            api_key: DashScope API key
            model: 使用的模型名称
        """
        self.api_key = api_key or DASHSCOPE_API_KEY
        self.model = model or DEFAULT_MODEL

        if not self.api_key:
            raise ValueError(
                "请设置 DASHSCOPE_API_KEY 环境变量或在 config.py 中配置 API key"
            )

        dashscope.api_key = self.api_key

    def call_llm(self, user_prompt: str, system_prompt: str = SYSTEM_PROMPT, max_retries: int = 3) -> str:
        """
        调用 LLM

        Args:
            user_prompt: 用户输入的 prompt
            system_prompt: 系统 Prompt，定义 Agent 角色
            max_retries: 最大重试次数

        Returns:
            LLM 返回的文本响应
        """
        import time

        for attempt in range(max_retries):
            try:
                response = dashscope.Generation.call(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=MAX_TOKENS,
                    result_format="message"
                )

                if response.status_code == 200:
                    content = response.output.choices[0].message.content
                    return content
                else:
                    return f"错误：{response.code} - {response.message}"

            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"[重试] 第 {attempt + 1} 次失败，{2 ** attempt} 秒后重试...")
                    time.sleep(2 ** attempt)
                else:
                    return f"错误：{type(e).__name__} - {str(e)}"

        return "错误：达到最大重试次数"

    def chat(self, message: str, context: Optional[list] = None) -> str:
        """
        支持上下文的对话

        Args:
            message: 当前消息
            context: 对话历史 [{"role": "user/assistant", "content": "..."}]

        Returns:
            LLM 响应
        """
        messages = context or []

        # 添加 system prompt
        full_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        full_messages.extend(messages)
        full_messages.append({"role": "user", "content": message})

        try:
            response = dashscope.Generation.call(
                model=self.model,
                messages=full_messages,
                max_tokens=MAX_TOKENS,
                result_format="message"
            )

            if response.status_code == 200:
                assistant_message = response.output.choices[0].message.content

                # 更新上下文
                context.append({"role": "assistant", "content": assistant_message})

                return assistant_message
            else:
                return f"错误：{response.code} - {response.message}"

        except Exception as e:
            return f"错误：{str(e)}"


# 全局 Agent 实例（单例模式）
_agent_instance: Optional[AgentCore] = None


def get_agent() -> AgentCore:
    """获取全局 Agent 实例"""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = AgentCore()
    return _agent_instance
