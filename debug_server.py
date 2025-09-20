#!/usr/bin/env python3
"""
Debug script to test the MCP server locally and identify issues.
"""

import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
config_dir = Path(__file__).parent / "config"
if (config_dir / ".env").exists():
    load_dotenv(config_dir / ".env")

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Test if all imports work correctly."""
    print("🔍 Testing imports...")
    
    try:
        from mcp.server.fastmcp import FastMCP
        print("✅ FastMCP import successful")
    except Exception as e:
        print(f"❌ FastMCP import failed: {e}")
        return False
    
    try:
        from flux_adapter import FluxAdapter
        print("✅ FluxAdapter import successful")
    except Exception as e:
        print(f"❌ FluxAdapter import failed: {e}")
        return False
    
    return True

def test_environment():
    """Test environment variables."""
    print("\n🔍 Testing environment...")
    
    api_key = os.getenv("BFL_API_KEY")
    if api_key:
        print(f"✅ BFL_API_KEY found: {api_key[:8]}...")
        return True
    else:
        print("❌ BFL_API_KEY not found")
        return False

def test_server_creation():
    """Test MCP server creation."""
    print("\n🔍 Testing MCP server creation...")
    
    try:
        from mcp.server.fastmcp import FastMCP
        mcp = FastMCP("FluxImageGenerator")
        print("✅ MCP server created successfully")
        return True
    except Exception as e:
        print(f"❌ MCP server creation failed: {e}")
        return False

async def test_flux_function():
    """Test the flux_generate function directly."""
    print("\n🔍 Testing flux_generate function...")
    
    try:
        # Import the function
        sys.path.insert(0, str(Path(__file__).parent / "src"))
        
        # Create a simple test
        from flux_adapter import FluxAdapter
        
        api_key = os.getenv("BFL_API_KEY")
        if not api_key:
            print("❌ No API key available for testing")
            return False
        
        adapter = FluxAdapter(
            model="flux-pro-1.1",
            use_raw_mode=False,
            api_key=api_key,
            aspect_ratio="1:1",
            safety_tolerance=6
        )
        
        print("✅ FluxAdapter created successfully")
        return True
        
    except Exception as e:
        print(f"❌ FluxAdapter test failed: {e}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return False

def main():
    """Run all tests."""
    print("🧪 Flux MCP Server Debug Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_environment,
        test_server_creation,
        test_flux_function
    ]
    
    results = []
    for test in tests:
        if asyncio.iscoroutinefunction(test):
            result = asyncio.run(test())
        else:
            result = test()
        results.append(result)
    
    print("\n📊 Test Results:")
    print("=" * 20)
    
    test_names = ["Imports", "Environment", "Server Creation", "Flux Function"]
    for name, result in zip(test_names, results):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name}: {status}")
    
    if all(results):
        print("\n🎉 All tests passed! Server should work.")
    else:
        print("\n💥 Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()
