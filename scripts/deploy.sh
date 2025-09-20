#!/bin/bash

# Flux MCP Server Deployment Script
# This script helps deploy the Flux MCP Server to Dedalus Labs

set -e

echo "🚀 Flux MCP Server Deployment Script"
echo "====================================="

# Check if dedalus CLI is installed
if ! command -v dedalus &> /dev/null; then
    echo "❌ Dedalus CLI not found. Please install it first:"
    echo "   https://docs.dedalus.ai/getting-started/installation"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "main.py" ] || [ ! -f "pyproject.toml" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Get deployment name
read -p "Enter deployment name (default: flux-image-generator): " DEPLOY_NAME
DEPLOY_NAME=${DEPLOY_NAME:-flux-image-generator}

echo "📦 Deploying to Dedalus Labs..."
echo "   Name: $DEPLOY_NAME"

# Deploy to Dedalus
dedalus deploy . --name "$DEPLOY_NAME"

echo "✅ Deployment completed successfully!"
echo ""
echo "🔧 Next steps:"
echo "1. Set your BFL_API_KEY environment variable in the Dedalus UI"
echo "2. Test your deployment: dedalus test $DEPLOY_NAME"
echo "3. Check logs: dedalus logs $DEPLOY_NAME"
echo ""
echo "📚 Documentation: https://docs.dedalus.ai/"
