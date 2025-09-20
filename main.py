#!/usr/bin/env python3
"""
Main entry point for the Flux MCP Server.
This is what Dedalus runs when deploying the server.
"""

from src.main import mcp

if __name__ == "__main__":
    mcp.run()
