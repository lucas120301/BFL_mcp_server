# Flux MCP Server

An MCP (Model Context Protocol) server for AI-powered image generation using Black Forest Labs' Flux models. Built for seamless integration with AI agents and compatible with Dedalus Labs deployment.

## Features

- **AI Image Generation**: Generate high-quality images using state-of-the-art Flux models
- **Multiple Models**: Support for different Flux model variants (flux-pro-1.1, flux-dev, flux-schnell)
- **Flexible Parameters**: Customizable aspect ratios, dimensions, and safety settings
- **MCP Integration**: Seamless integration with MCP-compatible AI agents
- **Dedalus Ready**: Optimized for deployment on Dedalus Labs platform
- **Rate Limiting**: Built-in protection for API keys and usage limits

## Quick Start

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- Black Forest Labs API key from [api.bfl.ai](https://api.bfl.ai/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd flux-mcp-main
   ```

2. **Install dependencies:**
   ```bash
   # Install uv package manager
   brew install uv  # or pip install uv
   
   # Install dependencies
   uv sync --no-dev
   ```

3. **Configure API key:**
   ```bash
   # Set environment variable
   export BFL_API_KEY="your_api_key_here"
   
   # Or create .env file
   cp config/.env.example config/.env
   # Edit config/.env and add your API key
   ```

4. **Run the server:**
   ```bash
   uv run main
   ```

## Available Tools

### `flux_generate`

Generate images using Flux AI models.

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

## Deployment

### Deploy to Dedalus Labs

1. **Set Environment Variables in Dedalus UI:**
   - `BFL_API_KEY`: Your Black Forest Labs API key (required)

2. **Deploy:**
   ```bash
   dedalus deploy . --name "flux-image-generator"
   ```

3. **Test:**
   ```bash
   dedalus test flux-image-generator
   ```

### Local Development

```bash
# Test locally
./scripts/test-local.sh

# Deploy to Dedalus
./scripts/deploy.sh
```

## Project Structure

```
flux-mcp-main/
├── main.py                 # Entry point (required by Dedalus)
├── pyproject.toml          # Package configuration
├── src/
│   ├── main.py            # MCP server implementation
│   └── flux_adapter.py    # Black Forest Labs API adapter
├── config/
│   └── .env.example       # Environment template
├── docs/                  # Documentation
│   ├── getting-started.md
│   ├── deployment.md
│   └── api-reference.md
├── examples/              # Usage examples
│   ├── basic-usage.py
│   ├── creative-prompts.py
│   └── README.md
├── scripts/               # Deployment scripts
│   ├── deploy.sh
│   └── test-local.sh
└── tests/                 # Test files
    └── image_generation.py
```

## Documentation

- [Getting Started Guide](docs/getting-started.md)
- [Deployment Guide](docs/deployment.md)
- [API Reference](docs/api-reference.md)
- [Examples](examples/README.md)

## Examples

Check out the [examples](examples/) directory for:

- [Basic Usage](examples/basic-usage.py) - Simple image generation
- [Creative Prompts](examples/creative-prompts.py) - Advanced prompt techniques

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Black Forest Labs](https://api.bfl.ai/) for the Flux AI models
- [Model Context Protocol](https://modelcontextprotocol.io/) for the MCP specification
- [Dedalus Labs](https://dedalus.ai/) for the deployment platform
