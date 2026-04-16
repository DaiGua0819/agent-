"""
Bug 修复技能
"""
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.core import get_agent


def fix_bug(code: str, error: str = "") -> str:
    """
    分析并修复代码 bug

    Args:
        code: 有问题的代码
        error: 错误信息（可选）

    Returns:
        修复建议和修复后的代码
    """
    agent = get_agent()

    error_info = error if error else "运行结果不符合预期"

    prompt = f"""
请帮我分析并修复以下代码的问题：

**代码**：
```python
{code}
```

**错误信息**：
{error_info}

请：
1. 分析错误原因
2. 给出修复后的完整代码
3. 解释为什么这样修复
"""

    return agent.call_llm(prompt)
