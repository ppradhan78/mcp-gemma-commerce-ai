from typing import Any

from app.llm.gemma_client import gemma_client
from app.mcp.mcp_client import mcp_client


class CommerceAgent:

    def __init__(self) -> None:

        self.llm = gemma_client
        self.mcp = mcp_client

    async def run(
        self,
        user_message: str,
    ) -> dict[str, Any]:

        """
        Process a user request.

        Current flow:

        User
          |
          v
        Gemma
          |
          v
        Agent
          |
          v
        MCP tools
          |
          v
        Final answer
        """

        prompt = self._build_prompt(user_message)

        response = self.llm.generate(prompt)

        return {
            "response": response,
            "tool_calls": [],
        }

    def _build_prompt(
        self,
        user_message: str,
    ) -> str:

        return f"""
You are an enterprise commerce AI assistant.

You can answer questions about:

- Customers
- Orders
- Products
- Categories
- Suppliers
- Shippers
- Employees
- Sales

The enterprise data is exposed through MCP tools.

User request:

{user_message}

Provide a clear and concise answer.
""".strip()


commerce_agent = CommerceAgent()