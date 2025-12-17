# -*- coding: utf-8 -*-
from eth_account import Account
from x402.clients import x402_requests, decode_x_payment_response
from config import client_env


def run_client():
    print("🤖 x402 客户端测试")

    # 创建账户
    account = Account.from_key(client_env.PRIVATE_KEY)
    print(f"客户端地址: {account.address}")

    # 创建x402会话（自动处理支付）
    session = x402_requests(account)

    # 发起请求
    try:
        url = f"{client_env.RESOURCE_SERVER_URL}{client_env.ENDPOINT_PATH}"
        print(f"请求: {url}")

        response = session.get(url)

        print(f"状态码: {response.status_code}")
        print(f"内容: {response.content.decode()}")

        # 显示详细的支付信息
        print("\n" + "="*50)
        print("💳 支付详情")
        print("="*50)

        # 检查所有相关头部
        payment_headers = [h for h in response.headers if 'payment' in h.lower() or 'x402' in h.lower()]
        for header in payment_headers:
            print(f"{header}: {response.headers[header]}")

        # 解码支付响应
        if "X-Payment-Response" in response.headers:
            payment = decode_x_payment_response(response.headers["X-Payment-Response"])
            print(f"\n📋 解码的支付信息:")
            print(f"  ✅ 支付成功: {payment.get('success', False)}")
            print(f"  🔗 交易哈希: {payment.get('transaction', 'N/A')}")
            print(f"  🌐 网络: {payment.get('network', 'N/A')}")
            print(f"  👤 付款方: {payment.get('payer', 'N/A')}")

            # 提供区块链浏览器链接
            tx_hash = payment.get('transaction')
            if tx_hash and tx_hash != 'N/A':
                print(f"  🔍 查看交易: https://sepolia.basescan.org/tx/{tx_hash}")

        print("="*50)

    except Exception as e:
        print(f"错误: {e}")
        if "Connection" in str(e):
            print("请先启动: python src/server.py")


if __name__ == "__main__":
    run_client()
