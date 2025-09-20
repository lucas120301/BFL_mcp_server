from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
from typing import Optional
from pathlib import Path

# Import flux_adapter with absolute import
try:
    from .flux_adapter import FluxAdapter
except ImportError:
    # Fallback for deployment environments
    from flux_adapter import FluxAdapter


# Load environment variables from config/.env file (for local development)
# In deployment, environment variables are provided by the platform
try:
    config_dir = Path(__file__).parent.parent / "config"
    if (config_dir / ".env").exists():
        load_dotenv(config_dir / ".env")
except Exception:
    # Ignore errors in deployment environments
    pass

# Create an MCP server
mcp = FastMCP("FluxImageGenerator")


@mcp.tool()
async def flux_generate(
    prompt: str,
    model: str = "flux-pro-1.1",
    aspect_ratio: Optional[str] = "16:9",
    width: int = 1024,
    height: int = 1024,
    raw: bool = False,
    safety_tolerance: int = 6,
    prompt_upsampling: bool = False
) -> dict:
    """
    Generate images using Black Forest Labs' Flux models.
    
    Args:
        prompt: Text description of the image to generate
        model: Flux model to use (default: flux-pro-1.1)
        aspect_ratio: Image aspect ratio (default: 16:9)
        width: Image width in pixels (used when aspect_ratio is not specified)
        height: Image height in pixels (used when aspect_ratio is not specified)
        raw: Use raw mode for more creative outputs (default: False)
        safety_tolerance: Safety filter level 0-10 (default: 6)
        prompt_upsampling: Enhance prompt quality (default: False)
    
    Returns:
        dict: Response with status, image URL, and metadata
    """
    api_key = os.getenv("BFL_API_KEY")
    if not api_key:
        return {"status": "error", "message": "BFL_API_KEY not set"}
    
    try:
        adapter = FluxAdapter(
            model=model,
            use_raw_mode=raw,
            api_key=api_key,
            aspect_ratio=aspect_ratio,
            width=width,
            height=height,
            safety_tolerance=safety_tolerance,
            prompt_upsampling=prompt_upsampling,
        )
        image_url, meta = await adapter.generate(prompt)
        return {"status": "success", "image": image_url, "meta": meta}
    except Exception as e:
        # Log the full error for debugging
        import traceback
        error_details = traceback.format_exc()
        return {
            "status": "error", 
            "message": str(e),
            "error_type": type(e).__name__,
            "traceback": error_details
        }
    

if __name__ == "__main__":
    mcp.run()