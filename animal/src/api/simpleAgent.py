from fastapi import APIRouter, Depends
from beeai_framework.agents.react.agent import ReActAgent
from beeai_framework.agents.react.types import ReActAgentRunOutput
from beeai_framework.backend.chat import ChatModel
from beeai_framework.errors import FrameworkError
from beeai_framework.memory.unconstrained_memory import UnconstrainedMemory
from beeai_framework.tools.search.duckduckgo import DuckDuckGoSearchTool
from beeai_framework.tools.weather.openmeteo import OpenMeteoTool
from beeai_framework.tools.search.wikipedia import WikipediaTool

#Uncomment this line if you want to run the llm with a watsonx account
#from animal.src.connectors.WatsonxModel import WatsonxModel


agent = APIRouter()
#Uncomment this line if you want to run the llm with a watsonx account
#wx_model = WatsonxModel()

@agent.get("/agent/simple")
async def simple_agent():
    #Uncomment this line if you want to run the llm with a watsonx account
    #llm = wx_model.llm

    #Comment out this line if you want to run the llm with a watsonx account
    llm = ChatModel.from_name("ollama:granite3.1-dense:8b")

    agent = ReActAgent(
        llm=llm, tools=[WikipediaTool(), OpenMeteoTool(), DuckDuckGoSearchTool(max_results=3)], memory=UnconstrainedMemory()
    )

    #Change the question to test
    output: ReActAgentRunOutput = await agent.run("Which beaches in Spain can I go to with my dog?").on(
        "update", lambda data, event: print(f"Agent({data.update.key}) 🤖 : ", data.update.parsed_value)
    )

    print("Agent 🤖 : ", output.result.text)

    return "Agent 🤖 : ", output.result.text
