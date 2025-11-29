from langgraph.graph import StateGraph,START,END
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI



 
from langgraph.prebuilt import ToolNode

from langgraph.prebuilt import tools_condition


from custom_tools import tools

from dotenv import load_dotenv
load_dotenv()

#st.sessions_state
CONFIG={'configurable':{'thread_id':'thread-1'}}

# genai.configure(api_key="YOUR_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # or gemini-1.5-pro
    temperature=0.3
)

llm_with_tools=llm.bind_tools(tools=tools)

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
    


def chat_node(state: ChatState):
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)   # ✔ tool detection happens here
    return {"messages": [response]}

def tool_calling_llm(state:ChatState):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}



#checkpointer
checkpointer=InMemorySaver()



graph=StateGraph(ChatState)
# graph.add_node("chat_node",chat_node)
graph.add_node("tool_calling_llm",tool_calling_llm)
graph.add_node("tools",ToolNode(tools))



#edges
graph.add_edge(START,"tool_calling_llm")
graph.add_conditional_edges(
    "tool_calling_llm",
    tools_condition,
   
)

graph.add_edge("tools","tool_calling_llm")




chatbot=graph.compile(checkpointer=checkpointer)

# messages=chatbot.invoke({"messages":" hii ! my name is Afzal and tell me what is the latest research on quantum computing? "},config=CONFIG)
# for m in messages['messages']:
#     res=m.pretty_print()
#     print(res)
