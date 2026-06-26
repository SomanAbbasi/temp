from fastmcp import FastMCP

# Create server
mcp = FastMCP("Demo Server")


# Tool example
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Resource example
@mcp.resource("greeting://hello")
def greeting():
    return "Hello from FastMCP!"


if __name__ == "__main__":
    mcp.run()