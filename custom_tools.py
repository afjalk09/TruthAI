from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper

from langchain_community.tools import DuckDuckGoSearchRun
# from langchain_community.tools.tavily_search import TavilySearchResults

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

from image_tool import analyze_image_tool
# from langgraph_backend import llm

from dotenv import load_dotenv
load_dotenv()
#ArxivQueryRun for Search scientific papers
api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=2,doc_content_chars_max=500)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv,description="Query arxiv papers")
# print(arxiv.name)

# result=arxiv.invoke("Attention all you need")
# print(result)


#WikipediaQueryRun for Retrieve Wikipedia articles

api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=500)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

# wiki.name


#DuckDuckGoSearchRun for web search agent
duckduckgo = DuckDuckGoSearchRun(
    name="duckduckgo_search",
    description="Search the web using DuckDuckGo"
)

# print(duckduckgo.name)
# print(duckduckgo.invoke("Latest news on NVIDIA AI chips"))

#for webSearch agent
tavily=TavilySearch()

# res=tavily.invoke("provide me recent trending news in india")
# print(res)

# @tool


tools=[arxiv,wiki,duckduckgo]





