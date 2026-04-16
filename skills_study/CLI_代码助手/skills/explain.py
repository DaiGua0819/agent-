"""
代码解释技能
"""
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.core import get_agent
from agent.prompt import EXPLAIN_PROMPT


def explain_code(code: str, detail_level: str = "medium") -> str:
    """
    解释代码的功能

    Args:
        code: 要解释的 Python 代码
        detail_level: 详细程度 (low/medium/high)

    Returns:
        解释文本
    """
    agent = get_agent()

    # 根据详细程度调整 prompt
    if detail_level == "low":
        instruction = "请用 1-2 句话简单概述这段代码的功能"
    elif detail_level == "high":
        instruction = """请详细解释：
1. 功能概述 - 这段代码是做什么的
2. 关键逻辑 - 逐行或逐函数分析
3. 输入输出 - 参数和返回值的含义
4. 使用示例 - 给出调用示例
5. 潜在问题 - 可能的边界情况或改进建议"""
    else:  # medium
        instruction = """请解释：
1. 功能概述 - 这段代码是做什么的
2. 关键逻辑 - 核心算法或工作流程
3. 输入输出 - 参数和返回值的含义"""

    prompt = f"""
{instruction}

代码：
```python
{code}
```
"""

    return agent.call_llm(prompt)


async def explain_code_async(code: str, detail_level: str = "medium") -> str:
    """
    异步版本（预留，目前同步调用）
    """
    return explain_code(code, detail_level)
