#!/usr/bin/env python3
"""
Creative prompts example for the Flux MCP Server.
This example shows various creative prompt techniques and styles.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def generate_creative_images():
    """Generate images using various creative prompt techniques."""
    
    creative_prompts = [
        {
            "name": "Artistic Style",
            "prompt": "A majestic mountain landscape painted in the style of Van Gogh, with swirling brushstrokes and vibrant colors, oil painting",
            "aspect_ratio": "16:9"
        },
        {
            "name": "Photorealistic",
            "prompt": "Professional photography of a golden retriever playing in a field of wildflowers, shallow depth of field, natural lighting, high resolution",
            "aspect_ratio": "4:3"
        },
        {
            "name": "Fantasy Art",
            "prompt": "A mystical forest with glowing mushrooms and fairy lights, magical atmosphere, fantasy art style, detailed digital painting",
            "aspect_ratio": "16:9"
        },
        {
            "name": "Minimalist",
            "prompt": "Minimalist geometric design, clean lines, monochromatic color scheme, modern art style, simple and elegant",
            "aspect_ratio": "1:1"
        },
        {
            "name": "Vintage Style",
            "prompt": "A 1950s diner interior with neon signs, retro aesthetic, film photography style, warm lighting, nostalgic atmosphere",
            "aspect_ratio": "16:9"
        },
        {
            "name": "Abstract Art",
            "prompt": "Abstract expressionist painting with bold colors and dynamic brushstrokes, emotional and energetic, contemporary art",
            "aspect_ratio": "1:1"
        }
    ]
    
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            for i, prompt_data in enumerate(creative_prompts, 1):
                print(f"\n🎨 {i}. {prompt_data['name']}")
                print(f"   Prompt: {prompt_data['prompt']}")
                print(f"   Aspect Ratio: {prompt_data['aspect_ratio']}")
                
                result = await session.call_tool(
                    "flux_generate",
                    {
                        "prompt": prompt_data["prompt"],
                        "aspect_ratio": prompt_data["aspect_ratio"],
                        "safety_tolerance": 5,  # Slightly more permissive for creative content
                        "prompt_upsampling": True
                    }
                )
                
                if result.get("content") and result["content"][0].get("text"):
                    response_data = json.loads(result["content"][0]["text"])
                    if response_data.get("status") == "success":
                        print(f"   ✅ Generated successfully!")
                        print(f"   🖼️  Image URL: {response_data['image']}")
                    else:
                        print(f"   ❌ Error: {response_data.get('message')}")
                
                # Small delay between requests
                await asyncio.sleep(1)


async def generate_character_concepts():
    """Generate character concept art with different styles."""
    
    character_prompts = [
        {
            "name": "Sci-Fi Character",
            "prompt": "Character concept art of a cyberpunk warrior, futuristic armor, neon lights, digital art style, detailed character design",
            "aspect_ratio": "3:4"
        },
        {
            "name": "Fantasy Character",
            "prompt": "Fantasy character concept art of an elven mage, flowing robes, magical aura, fantasy art style, detailed character design",
            "aspect_ratio": "3:4"
        },
        {
            "name": "Steampunk Character",
            "prompt": "Steampunk character concept art, Victorian era clothing with mechanical elements, brass and copper colors, detailed character design",
            "aspect_ratio": "3:4"
        }
    ]
    
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🎭 Character Concept Art Examples")
            print("=" * 40)
            
            for i, prompt_data in enumerate(character_prompts, 1):
                print(f"\n{i}. {prompt_data['name']}")
                print(f"   Prompt: {prompt_data['prompt']}")
                
                result = await session.call_tool(
                    "flux_generate",
                    {
                        "prompt": prompt_data["prompt"],
                        "aspect_ratio": prompt_data["aspect_ratio"],
                        "safety_tolerance": 6,
                        "prompt_upsampling": True
                    }
                )
                
                if result.get("content") and result["content"][0].get("text"):
                    response_data = json.loads(result["content"][0]["text"])
                    if response_data.get("status") == "success":
                        print(f"   ✅ Character generated successfully!")
                        print(f"   🖼️  Image URL: {response_data['image']}")
                    else:
                        print(f"   ❌ Error: {response_data.get('message')}")
                
                await asyncio.sleep(1)


async def generate_environment_concepts():
    """Generate environment concept art."""
    
    environment_prompts = [
        {
            "name": "Post-Apocalyptic City",
            "prompt": "Post-apocalyptic cityscape, overgrown with vegetation, abandoned buildings, dramatic lighting, concept art style",
            "aspect_ratio": "16:9"
        },
        {
            "name": "Underwater Palace",
            "prompt": "Underwater palace with coral and sea creatures, magical underwater lighting, fantasy environment concept art",
            "aspect_ratio": "16:9"
        },
        {
            "name": "Space Station Interior",
            "prompt": "Interior of a massive space station, futuristic technology, clean and sterile environment, sci-fi concept art",
            "aspect_ratio": "16:9"
        }
    ]
    
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            print("\n🌍 Environment Concept Art Examples")
            print("=" * 40)
            
            for i, prompt_data in enumerate(environment_prompts, 1):
                print(f"\n{i}. {prompt_data['name']}")
                print(f"   Prompt: {prompt_data['prompt']}")
                
                result = await session.call_tool(
                    "flux_generate",
                    {
                        "prompt": prompt_data["prompt"],
                        "aspect_ratio": prompt_data["aspect_ratio"],
                        "safety_tolerance": 6,
                        "prompt_upsampling": True
                    }
                )
                
                if result.get("content") and result["content"][0].get("text"):
                    response_data = json.loads(result["content"][0]["text"])
                    if response_data.get("status") == "success":
                        print(f"   ✅ Environment generated successfully!")
                        print(f"   🖼️  Image URL: {response_data['image']}")
                    else:
                        print(f"   ❌ Error: {response_data.get('message')}")
                
                await asyncio.sleep(1)


async def main():
    """Run all creative examples."""
    print("🎨 Flux MCP Server - Creative Prompts Examples")
    print("=" * 50)
    
    try:
        # Creative styles
        print("\n1. Creative Art Styles")
        print("-" * 25)
        await generate_creative_images()
        
        # Character concepts
        await generate_character_concepts()
        
        # Environment concepts
        await generate_environment_concepts()
        
        print("\n✅ All creative examples completed successfully!")
        print("\n💡 Tips for better prompts:")
        print("   - Be specific about style and medium")
        print("   - Include lighting and mood descriptions")
        print("   - Mention technical details (resolution, depth of field)")
        print("   - Use art style references (Van Gogh, digital art, etc.)")
        print("   - Experiment with different aspect ratios")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Make sure the server is running and your BFL_API_KEY is set.")


if __name__ == "__main__":
    asyncio.run(main())
