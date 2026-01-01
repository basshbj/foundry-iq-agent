# Building an AI Agent with Foundry IQ

#### Reference links
- [](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval?view=foundry&tabs=search%2Cpython)
- [](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-knowledge-base?tabs=rbac&pivots=python)
- [](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-pipeline)


## What is Foundry IQ
- Separates the agent logic and the domain knowledege (separete layer?)
  - This enable RAG and grounding at scale
- You create a knowledge base that represents a complete domain of knowledge
  - The agent call the knowledge base to ground their answers.

Benefits
- Can update the knowledge base without modifying the agent
- Avoid duplicated configurations. The knowledge base is shared a cross all the agents (abstraction layer)

## How Foundry IQ works
- Powered by Azure AI Search
  - Knowledge source: what to retrieve
  - Knowledge base: how to retrieve
- Supports:
  - Answer synthesis: pre-generetes an answer
  - Extractive data output: returns the data as it is

## How Foudry Agent Services uses Knowledge Bases
- Called via MCP tool
  - At Runtime, only call the knowledge base (not data source)
- The Agent synthesizes the final answer
- The Knowledge base handles the retrieval

## Foundry IQ - Agentic Retrieval
![](https://learn.microsoft.com/en-us/azure/search/media/agentic-retrieval/end-to-end-pipeline.svg)


## Notes
- Semantic Ranker needs to be enabled in Azure AI Search