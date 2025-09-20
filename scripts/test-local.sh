#!/bin/bash

# Local Testing Script for Flux MCP Server
# This script helps test the server locally before deployment

set -e

echo "🧪 Flux MCP Server Local Testing"
echo "================================="

# Check if we're in the right directory
if [ ! -f "main.py" ] || [ ! -f "pyproject.toml" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install fastmcp python-dotenv requests pydantic

# Load environment variables from config/.env if it exists
if [ -f "config/.env" ]; then
    echo "📋 Loading environment variables from config/.env..."
    export $(grep -v '^#' config/.env | xargs)
fi

# Check for API key
if [ -z "$BFL_API_KEY" ]; then
    echo "⚠️  BFL_API_KEY not set. Please set it:"
    echo "   export BFL_API_KEY='your_api_key_here'"
    echo ""
    echo "Or create a .env file in the config/ directory:"
    echo "   cp config/.env.example config/.env"
    echo "   # Edit config/.env and add your API key"
    exit 1
fi

echo "🧪 Running tests..."
if [ -d "tests" ]; then
    # Install test dependencies
    echo "📦 Installing test dependencies..."
    pip install pytest pytest-asyncio
    python -m pytest tests/ -v
else
    echo "⚠️  No tests directory found. Skipping tests."
fi

echo "🚀 Starting server locally..."
echo "   Press Ctrl+C to stop"
echo ""

# Start the server
python main.py
