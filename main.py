import asyncio
import os

from dotenv import load_dotenv
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client
from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

from config import MODEL_NAME, PROXY_CLIENT_NAME
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

proxy_client = get_proxy_client(PROXY_CLIENT_NAME)

llm = ChatOpenAI(proxy_model_name=MODEL_NAME, proxy_client=proxy_client)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/I756693/Documents/mcp_project/mcp/servers/math_server.py"],
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)
            
            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 99 + 27 * 3?. Just provide me the answer, no need to explain.")]})
            print(result["messages"][-1].content)
                

    

if __name__ == "__main__":
    asyncio.run(main())
