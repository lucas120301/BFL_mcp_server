# Getting Started with Flux MCP Server

## Overview

The Flux MCP Server provides AI-powered image generation capabilities using Black Forest Labs' Flux models. This server integrates with MCP (Model Context Protocol) to enable AI agents to generate high-quality images from text prompts.

## Features

- **AI Image Generation**: Generate images using state-of-the-art Flux models
- **Multiple Models**: Support for different Flux model variants
- **Flexible Parameters**: Customizable aspect ratios, dimensions, and safety settings
- **MCP Integration**: Seamless integration with MCP-compatible AI agents

## Quick Start

### 1. Get Your API Key

1. Visit [Black Forest Labs API](https://api.bfl.ai/)
2. Sign up for an account
3. Generate an API key
4. Copy your API key

### 2. Configure Environment

Set your API key as an environment variable:

```bash
export BFL_API_KEY="your_api_key_here"
```

Or create a `.env` file in the `config/` directory:

```bash
cp config/.env.example config/.env
# Edit config/.env and add your API key
```

### 3. Install Dependencies

```bash
# Install uv package manager
brew install uv  # or pip install uv

# Install dependencies
uv sync --no-dev
```

### 4. Run the Server

```bash
uv run main
```

## Available Tools

### `flux_generate`

Generate images using Flux models.

**Parameters:**
- `prompt` (string, required): Text description of the image to generate
- `model` (string, optional): Flux model to use (default: "flux-pro-1.1")
- `aspect_ratio` (string, optional): Image aspect ratio (default: "16:9")
- `width` (int, optional): Image width in pixels (default: 1024)
- `height` (int, optional): Image height in pixels (default: 1024)
- `raw` (bool, optional): Use raw mode for more creative outputs (default: false)
- `safety_tolerance` (int, optional): Safety filter level 0-10 (default: 6)
- `prompt_upsampling` (bool, optional): Enhance prompt quality (default: false)

**Returns:**
- `status`: "success" or "error"
- `image`: URL to the generated image (on success)
- `meta`: Metadata about the generation (on success)
- `message`: Error message (on error)

## Example Usage

```python
# Generate a simple image
result = await flux_generate(
    prompt="A beautiful sunset over mountains",
    aspect_ratio="16:9"
)

# Generate with custom parameters
result = await flux_generate(
    prompt="A futuristic cityscape at night",
    model="flux-pro-1.1",
    width=1920,
    height=1080,
    safety_tolerance=4,
    prompt_upsampling=True
)
```

## Supported Models

- `flux-pro-1.1`: Latest Flux Pro model (recommended)
- `flux-dev`: Development model
- `flux-schnell`: Fast generation model

## Aspect Ratios

Common aspect ratios supported:
- `1:1` - Square
- `16:9` - Widescreen
- `9:16` - Portrait
- `4:3` - Standard
- `3:4` - Portrait standard

## Safety and Guidelines

- The `safety_tolerance` parameter controls content filtering (0-10)
- Higher values are more restrictive
- Use appropriate prompts that comply with Black Forest Labs' usage policies
- Generated images are subject to the API provider's terms of service

## Troubleshooting

### Common Issues

1. **API Key Not Set**
   - Ensure `BFL_API_KEY` environment variable is set
   - Check that your API key is valid and active

2. **Generation Timeout**
   - Complex prompts may take longer to process
   - Try simplifying your prompt or using a different model

3. **Safety Filter Triggered**
   - Adjust `safety_tolerance` parameter
   - Modify your prompt to be more appropriate

### Getting Help

- Check the [Black Forest Labs API Documentation](https://api.bfl.ai/docs)
- Review error messages in the response
- Ensure your API key has sufficient credits

## Next Steps

- Explore the examples in the `examples/` directory
- Check out the deployment guide for production setup
- Review the API documentation for advanced features
