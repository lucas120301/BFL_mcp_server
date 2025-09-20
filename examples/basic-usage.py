#!/usr/bin/env python3
"""
Basic usage example for the Flux MCP Server.
This example shows how to use the server to generate images.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def generate_image_example():
    """Example of generating an image using the Flux MCP Server."""
    
    # Connect to the MCP server
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # Generate a simple image
            print("🎨 Generating image: 'A beautiful sunset over mountains'")
            result = await session.call_tool(
                "flux_generate",
                {
                    "prompt": "A beautiful sunset over mountains",
                    "aspect_ratio": "16:9"
                }
            )
            
            print("📋 Result:")
            print(json.dumps(result, indent=2))
            
            if result.get("content") and result["content"][0].get("text"):
                response_data = json.loads(result["content"][0]["text"])
                if response_data.get("status") == "success":
                    print(f"✅ Image generated successfully!")
                    print(f"🖼️  Image URL: {response_data['image']}")
                else:
                    print(f"❌ Error: {response_data.get('message')}")


async def generate_multiple_images():
    """Example of generating multiple images with different parameters."""
    
    prompts = [
        "A serene lake with mountains in the background",
        "A futuristic cityscape at night with neon lights",
        "A cute cat wearing a space helmet"
    ]
    
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            for i, prompt in enumerate(prompts, 1):
                print(f"\n🎨 Generating image {i}: '{prompt}'")
                
                result = await session.call_tool(
                    "flux_generate",
                    {
                        "prompt": prompt,
                        "aspect_ratio": "1:1" if i == 3 else "16:9",  # Square for the cat
                        "safety_tolerance": 6,
                        "prompt_upsampling": True
                    }
                )
                
                if result.get("content") and result["content"][0].get("text"):
                    response_data = json.loads(result["content"][0]["text"])
                    if response_data.get("status") == "success":
                        print(f"✅ Image {i} generated successfully!")
                        print(f"🖼️  Image URL: {response_data['image']}")
                    else:
                        print(f"❌ Error generating image {i}: {response_data.get('message')}")


async def advanced_parameters_example():
    """Example using advanced parameters for image generation."""
    
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("🎨 Generating image with advanced parameters...")
            
            result = await session.call_tool(
                "flux_generate",
                {
                    "prompt": "A detailed architectural drawing of a modern house, professional blueprint style, high resolution",
                    "model": "flux-pro-1.1",
                    "width": 1920,
                    "height": 1080,
                    "safety_tolerance": 4,
                    "prompt_upsampling": True,
                    "raw": False
                }
            )
            
            if result.get("content") and result["content"][0].get("text"):
                response_data = json.loads(result["content"][0]["text"])
                if response_data.get("status") == "success":
                    print("✅ Advanced image generated successfully!")
                    print(f"🖼️  Image URL: {response_data['image']}")
                    print(f"📊 Metadata: {json.dumps(response_data['meta'], indent=2)}")
                else:
                    print(f"❌ Error: {response_data.get('message')}")


async def main():
    """Run all examples."""
    print("🚀 Flux MCP Server Examples")
    print("===========================")
    
    try:
        # Basic example
        print("\n1. Basic Image Generation")
        print("-" * 30)
        await generate_image_example()
        
        # Multiple images example
        print("\n2. Multiple Images Generation")
        print("-" * 35)
        await generate_multiple_images()
        
        # Advanced parameters example
        print("\n3. Advanced Parameters")
        print("-" * 25)
        await advanced_parameters_example()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Make sure the server is running and your BFL_API_KEY is set.")


if __name__ == "__main__":
    asyncio.run(main())
