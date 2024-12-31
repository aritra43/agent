from crewai import Agent, Task, Process, Crew
from crewai import LLM
from tools import yt_tool

# Initialize the LLM
llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

# Create agents
marketer = Agent(
    role='Market Research Analyst',
    goal="Suggest how big is the demand for my product and suggest the widest possible marketplace",
    backstory="""You are good at understanding market demands and are specialized in evaluating market size and target audience. You are good at suggesting ways to appeal to the marketplace to introduce a new product in the best manner possible.""",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=[yt_tool],
)

technologist = Agent(
    role='Senior Technology Expert',
    goal='Suggest how technologically feasible the idea is in the current marketplace and also suggest ways of making the product more technologically sound and appealing.',
    backstory="""You are the expert in the realm of technology and understand the effectiveness of technology in the realm of product business. Your insights are crucial for product development and achieving market success. Your experience and guidance in the field of technology are required to launch the best fit product for the present market and to ensure the successful existence of the product in the market.""",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=[yt_tool],
)

business_consultant = Agent(
    role='Business Development Consultant',
    goal='Evaluate and suggest the business model, scalability of the business so that the business remains profitable and scalable in the long run.',
    backstory="""You are an experienced and leading business consultant in the market. Your insights for our business are required to produce a proper business plan and make the business scalable, which will ensure profitability in the long run. Your suggestions are required to manage the business components in a structured and proper manner to ensure the correct proceedings of the business in the marketplace.""",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=[yt_tool],
)
