# Agent Learning Journey

我的 AI Agent 学习之旅，记录学习过程中做的各种实例和项目。

---

## 📁 项目结构

```
skills_study/                    # Git 仓库根目录
├── README.md                    # 本文件
├── .gitignore                   # Git 忽略文件
├── CLI_代码助手/                # 实例 1：命令行版本
│   ├── main.py
│   ├── agent/
│   └── skills/
├── API_代码助手/                # 实例 2：HTTP API 版本
│   ├── app.py
│   ├── agent.py
│   └── config.py
├── notes/                       # 学习笔记（未来）
└── mcp_learning/                # MCP 学习（未来）
```

---

## 📚 学习实例

### 实例 1：CLI 代码助手

一个基于命令行的人工智能代码助手。

**特点**：
- 通过命令行调用
- 适合本地开发辅助
- 简单直接的使用方式

📂 位置：`CLI_代码助手/`

[查看详细文档](./CLI_代码助手/README.md)

---

### 实例 2：API 代码助手

基于 Flask 的 HTTP API 服务，提供 RESTful 接口。

**特点**：
- HTTP API 调用
- 支持 Web 服务集成
- 可处理并发请求
- 支持跨语言调用

📂 位置：`API_代码助手/`

[查看详细文档](./API_代码助手/README.md)

---

## 📊 CLI vs API 对比

| 特性 | CLI 版本 | API 版本 |
|------|----------|----------|
| **调用方式** | 命令行 `python main.py` | HTTP 请求 `POST /api/xxx` |
| **使用场景** | 本地开发、脚本调用 | Web 服务、应用集成 |
| **并发支持** | 单用户 | 多用户并发 |
| **跨语言** | 否（Python） | 是（任意 HTTP 客户端） |
| **部署方式** | 本地运行 | 可部署为独立服务 |
| **集成难度** | 低 | 中 |
| **扩展性** | 低 | 高 |

### 选择建议

- 选 **CLI 版本** 如果你：
  - 只是想快速在本地使用
  - 不需要集成到其他应用
  - 喜欢命令行工具

- 选 **API 版本** 如果你：
  - 想集成到自己的 Web 应用
  - 需要支持多用户
  - 想用其他语言（JS/Go 等）调用

---

## 📝 学习计划

- [x] CLI 代码助手 - 理解 Agent 基本架构
- [x] API 代码助手 - 理解 HTTP 服务封装
- [ ] 对话式 Agent - 支持多轮对话上下文
- [ ] RAG 应用 - 知识库问答
- [ ] Function Calling - 工具调用
- [ ] 多 Agent 协作

---

## 🔗 相关链接

- [阿里云 DashScope 文档](https://help.aliyun.com/zh/dashscope/)
- [LangChain 文档](https://python.langchain.com/)
- [Flask 文档](https://flask.palletsprojects.com/)

---

## 📄 许可证

MIT
