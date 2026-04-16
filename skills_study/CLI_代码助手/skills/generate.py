"""
代码生成技能
"""
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.core import get_agent
from agent.prompt import GENERATE_PROMPT


def generate_code(prompt: str, style: str = "pythonic") -> str:
    """
    根据需求生成代码

    Args:
        prompt: 代码需求描述
        style: 代码风格 (pythonic/verbose/minimal)

    Returns:
        生成的代码
    """
    agent = get_agent()

    style_instruction = {
        "pythonic": "代码要 Pythonic，简洁优雅",
        "verbose": "代码要详细，包含完整的注释和错误处理",
        "minimal": "代码要尽可能简洁，只保留核心逻辑"
    }

    full_prompt = f"""
{GENERATE_PROMPT}

{style_instruction.get(style, style_instruction['pythonic'])}

需求：{prompt}
"""

    return agent.call_llm(full_prompt)
