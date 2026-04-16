"""
API 代码助手 - Flask HTTP 服务
提供 RESTful API 接口
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import get_agent

app = Flask(__name__)
CORS(app)  # 允许跨域请求

agent = get_agent()


@app.route('/api/explain', methods=['POST'])
def explain_code():
    """解释代码"""
    data = request.json
    code = data.get('code', '')
    detail = data.get('detail', 'medium')

    if detail == 'low':
        prompt = f"请用 1-2 句话简单概述这段代码的功能：\n```python\n{code}\n```"
    elif detail == 'high':
        prompt = f"""请详细解释以下代码：
1. 功能概述
2. 关键逻辑
3. 输入输出
4. 使用示例
5. 潜在问题

代码：
```python
{code}
```"""
    else:
        prompt = f"""请解释以下代码：
1. 功能概述
2. 关键逻辑
3. 输入输出

代码：
```python
{code}
```"""

    result = agent.call_llm(prompt)
    return jsonify({"success": True, "result": result})


@app.route('/api/generate', methods=['POST'])
def generate_code():
    """生成代码"""
    data = request.json
    prompt = data.get('prompt', '')
    style = data.get('style', 'pythonic')

    style_instruction = {
        "pythonic": "代码要 Pythonic，简洁优雅",
        "verbose": "代码要详细，包含完整的注释和错误处理",
        "minimal": "代码要尽可能简洁，只保留核心逻辑"
    }

    full_prompt = f"""请帮我生成 Python 代码：
{style_instruction.get(style, '代码要简洁优雅')}

需求：{prompt}

要求：
- 包含完整的类型注解
- 添加必要的 docstring
- 考虑边界情况和错误处理
"""

    result = agent.call_llm(full_prompt)
    return jsonify({"success": True, "result": result})


@app.route('/api/fix', methods=['POST'])
def fix_bug():
    """修复 Bug"""
    data = request.json
    code = data.get('code', '')
    error = data.get('error', '运行结果不符合预期')

    prompt = f"""请帮我分析并修复以下代码的问题：

**代码**：
```python
{code}
```

**错误信息**：
{error}

请：
1. 分析错误原因
2. 给出修复后的完整代码
3. 解释为什么这样修复
"""

    result = agent.call_llm(prompt)
    return jsonify({"success": True, "result": result})


@app.route('/api/test', methods=['POST'])
def generate_test():
    """生成测试"""
    data = request.json
    code = data.get('code', '')
    framework = data.get('framework', 'pytest')

    framework_instruction = {
        "pytest": "使用 pytest 框架，简洁的断言风格",
        "unittest": "使用 Python 内置的 unittest 框架"
    }

    prompt = f"""请为以下代码生成单元测试：

```python
{code}
```

**要求**：
- 使用 {framework_instruction.get(framework, 'pytest')}
- 覆盖正常情况和边界情况
- 包含必要的断言
- 测试函数命名清晰
"""

    result = agent.call_llm(prompt)
    return jsonify({"success": True, "result": result})


@app.route('/api/chat', methods=['POST'])
def chat():
    """多轮对话"""
    data = request.json
    message = data.get('message', '')
    history = data.get('history', [])

    result = agent.chat(message, history)
    return jsonify({"success": True, "result": result, "history": history})


@app.route('/api/health', methods=['GET'])
def health():
    """健康检查"""
    return jsonify({"status": "ok", "service": "API 代码助手"})


if __name__ == '__main__':
    from config import HOST, PORT
    print(f"🚀 API 服务启动：http://{HOST}:{PORT}")
    print(f"📚 API 文档：http://localhost:{PORT}/api/health")
    app.run(host=HOST, port=PORT, debug=True)
