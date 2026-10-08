from typing import Any

from app.config import settings


class MCPClient:

    def __init__(self) -> None:
        self.server_url = settings.mcp_server_url

    async def list_tools(self) -> list[dict[str, Any]]:
        """
        Return tools exposed by the MCP server.

        This method will be connected to the MCP SDK.
        """

        # TODO:
        # Connect to MCP server and call list_tools()

        return []

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> Any:

        """
        Execute an MCP tool.
        """

        # TODO:
        # MCP SDK tool invocation goes here.

        raise NotImplementedError(
            "MCP tool invocation has not been configured yet."
        )


mcp_client = MCPClient()