from crewai import Crew,Process
from agents import marketer,technologist,business_consultant
from tasks import marketing,technical,business_planning

crew = Crew(
    agents=[marketer, technologist, business_consultant],
    tasks=[marketing, technical, business_planning],
    verbose=2,
    process=Process.sequential,
)
result = crew.kickoff()
print("########################")
print(result)