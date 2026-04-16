#!/usr/bin/env python3
"""
Code Skills - 代码助手 CLI

使用方法:
    python main.py explain --code "def hello(): print('Hi')"
    python main.py generate --prompt "写一个快速排序"
    python main.py fix --code "..." --error "IndexError: list index out of range"
    python main.py test --code "def add(a, b): return a + b"
"""
import argparse
import sys
import io

# 设置 stdout 编码为 utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from skills.explain import explain_code
from skills.generate import generate_code
from skills.fix import fix_bug
from skills.test_gen import generate_test


def cmd_explain(args):
    """处理 explain 命令"""
    print("[INFO] 正在分析代码...\n")
    result = explain_code(args.code, args.detail)
    print(result)


def cmd_generate(args):
    """处理 generate 命令"""
    print("[INFO] 正在生成代码...\n")
    result = generate_code(args.prompt, args.style)
    print(result)


def cmd_fix(args):
    """处理 fix 命令"""
    print("[INFO] 正在分析 bug...\n")
    result = fix_bug(args.code, args.error)
    print(result)


def cmd_test(args):
    """处理 test 命令"""
    print("[INFO] 正在生成测试...\n")
    result = generate_test(args.code, args.framework)
    print(result)


def main():
    # 主解析器
    parser = argparse.ArgumentParser(
        prog="code_skills",
        description="Code Skills - AI 代码助手",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s explain --code "def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)"
  %(prog)s generate --prompt "写一个装饰器缓存函数结果"
  %(prog)s fix --code "..." --error "KeyError: 'name'"
        """
    )

    # 子命令解析器
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # ===== explain 命令 =====
    explain_parser = subparsers.add_parser(
        "explain",
        help="解释代码的功能和逻辑"
    )
    explain_parser.add_argument(
        "--code", "-c",
        required=True,
        help="要解释的 Python 代码"
    )
    explain_parser.add_argument(
        "--detail", "-d",
        choices=["low", "medium", "high"],
        default="medium",
        help="详细程度 (默认：medium)"
    )
    explain_parser.set_defaults(func=cmd_explain)

    # ===== generate 命令 =====
    gen_parser = subparsers.add_parser(
        "generate",
        help="根据需求生成代码"
    )
    gen_parser.add_argument(
        "--prompt", "-p",
        required=True,
        help="代码需求描述"
    )
    gen_parser.add_argument(
        "--style", "-s",
        choices=["pythonic", "verbose", "minimal"],
        default="pythonic",
        help="代码风格 (默认：pythonic)"
    )
    gen_parser.set_defaults(func=cmd_generate)

    # ===== fix 命令 =====
    fix_parser = subparsers.add_parser(
        "fix",
        help="分析并修复代码 bug"
    )
    fix_parser.add_argument(
        "--code", "-c",
        required=True,
        help="有问题的代码"
    )
    fix_parser.add_argument(
        "--error", "-e",
        default="",
        help="错误信息"
    )
    fix_parser.set_defaults(func=cmd_fix)

    # ===== test 命令 =====
    test_parser = subparsers.add_parser(
        "test",
        help="为代码生成单元测试"
    )
    test_parser.add_argument(
        "--code", "-c",
        required=True,
        help="要测试的代码"
    )
    test_parser.add_argument(
        "--framework", "-f",
        choices=["pytest", "unittest"],
        default="pytest",
        help="测试框架 (默认：pytest)"
    )
    test_parser.set_defaults(func=cmd_test)

    # 解析参数
    args = parser.parse_args()

    # 检查是否有命令
    if not args.command:
        parser.print_help()
        sys.exit(1)

    # 执行命令
    try:
        args.func(args)
    except ValueError as e:
        print(f"[ERROR] 配置错误：{e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[WARN] 操作已取消")
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] {type(e).__name__} - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
