from crewai import Task 
from agents import marketer,technologist,business_consultant
# Create tasks
# Create the Task instance for marketing
marketing = Task(
    description="""Analyze the market for the product of new-edge sneakers and also find the largest target audience which can be approached for selling the products in the market. Write a detailed report on the given points which should contain at least 10 bullet points and generate the report for the business owner.""",
    agent=[marketer],  # This should be a list of Agent instances
    expected_output="A detailed market analysis report.",  # Provide the expected output
    output_file='market-plan.md',  # Provide the output file name
)

# Create the Task instance
technical = Task(
    description="""Analyze all possible technological ways to make the sneaker marketing website and make the business more scalable. Generate a report consisting of at least 10 bullet points that will be generated for the business owner for his/her use in the near future for deciding the technological stack that will be used for the product development website.""",
    agent=[technologist],  # This should be a list of Agent instances
    expected_output="A detailed technological analysis report.",  # Provide the expected output
    output_file='technical-plan.md',  # Provide the output file name
)

# Create the Task instance for business planning
business_planning = Task(
    description="""Analyze the present sneaker market and take into consideration the works of other agents, then produce a business plan that will be best suited for launching the product, so that the business remains viable, scalable, and profitable in the long run.""",
    agent=[business_consultant],  # This should be a list of Agent instances
    expected_output="A comprehensive business plan report.",  # Provide the expected output
    output_file='business-plan.md',  # Provide the output file name
)
