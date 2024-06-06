# ReasoningAgent

The files in this repository should be sufficient to deploy and test the reasoning agent

## Dependencies:
* pdf search tool
* web search tool
* swagger code gen cloud function
are deployed and their information populated in the .env file according to the environment.

# Files:
* .env – contains all the variables to be populated accordring to environment
* reasoningEngineCodeRefactorGithubv4.ipynb – Reasoning Engine deployment notebook - run each cell in turn
* Naresh-TMF-ReasoningEngine-Client-Demov2.ipynb – Reasoning Engine client notebook
* Naresh-TMF-Hackathon-User-Guide.ipynb – Hackathon user guide notebook

# Necessary Permissions for use:
Role: DTW2024_Hackathon_Participant_Role (custom role, we could have any name here)
Permission:
* aiplatform.reasoningEngines.get
* aiplatform.reasoningEngines.list
* aiplatform.reasoningEngines.query
* aiplatform.reasoningEngines.update
* discoveryengine.dataStores.completeQuery
