import asyncio
import os

from dotenv import load_dotenv
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client
from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from config import MODEL_NAME, PROXY_CLIENT_NAME
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

proxy_client = get_proxy_client(PROXY_CLIENT_NAME)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/I756693/Documents/mcp_project/mcp/servers/math_server.py"],
)

async def main():
    print("Hello from mcp!")

    

if __name__ == "__main__":
    asyncio.run(main())
