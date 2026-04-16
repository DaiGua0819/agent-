"""
测试生成技能
"""
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.core import get_agent


def generate_test(code: str, framework: str = "pytest") -> str:
    """
    为代码生成单元测试

    Args:
        code: 要测试的代码
        framework: 测试框架 (pytest/unittest)

    Returns:
        测试代码
    """
    agent = get_agent()

    framework_instruction = {
        "pytest": "使用 pytest 框架，简洁的断言风格",
        "unittest": "使用 Python 内置的 unittest 框架"
    }

    prompt = f"""
请为以下代码生成单元测试：

```python
{code}
```

**要求**：
- 使用 {framework_instruction.get(framework, 'pytest')}
- 覆盖正常情况和边界情况
- 包含必要的断言
- 测试函数命名清晰
"""

    return agent.call_llm(prompt)
