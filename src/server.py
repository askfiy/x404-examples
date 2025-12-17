from typing import Any
from fastapi import FastAPI

from x402.fastapi.middleware import require_payment

from config import server_env

assert server_env.WALLET_ADDRESS, "没有配置收款钱包"

app = FastAPI()

app.middleware("http")(
    require_payment(
        path="/news",
        price="$0.001",
        pay_to_address=server_env.WALLET_ADDRESS,
        network="base-sepolia",
    )
)

# network = "base-sepolia" 测试
# network = "base-mainnet" 真实
# network = "ethereum-sepolia" 以太坊测试
# network = "ethereum-mainnet" 以太坊真实


@app.get("/news")
async def get_news() -> dict[str, Any]:
    return {"news": [f"新闻:{i + 1}" for i in range(5)]}


def run_server():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run_server()
