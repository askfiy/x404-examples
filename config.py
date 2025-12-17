import os
from pydantic_settings import BaseSettings


class ServerEnv(BaseSettings):
    model_config = {
        "env_file": os.path.join(os.path.dirname(__file__), "env", "server.env"),
        "env_file_encoding": "utf-8",
    }
    # 收款钱包
    WALLET_ADDRESS: str = ""


class ClientEnv(BaseSettings):
    model_config = {
        "env_file": os.path.join(os.path.dirname(__file__), "env", "client.env"),
        "env_file_encoding": "utf-8",
    }
    RESOURCE_SERVER_URL: str = ""
    ENDPOINT_PATH: str = ""
    PRIVATE_KEY: str = ""


server_env = ServerEnv()
client_env = ClientEnv()
