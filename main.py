# -*- coding: utf-8 -*-
import argparse
import config

print(config.server_env.WALLET_ADDRESS)

from src.server import run_server
from src.client import run_client


def main():
    parser = argparse.ArgumentParser(description="x402 示例程序")
    parser.add_argument("--server", action="store_true", help="启动x402服务器")
    parser.add_argument("--client", action="store_true", help="运行x402客户端")

    args = parser.parse_args()

    if args.server:
        run_server()
    elif args.client:
        run_client()
    else:
        print("🤖 x402 示例程序")
        print("\n使用方法:")
        print("  uv run main.py --server   # 启动服务器")
        print("  uv run main.py --client   # 运行客户端")
        print("\n或者:")
        print("  python main.py --server   # 启动服务器")
        print("  python main.py --client   # 运行客户端")


if __name__ == "__main__":
    main()
