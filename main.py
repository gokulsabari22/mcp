import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from mcp import ClientSession, StdioServerParameters
from mcp.server.stdio import studio_client

load_dotenv()


async def main():
    print("Hello from mcp!")


if __name__ == "__main__":
    asyncio.run(main())
