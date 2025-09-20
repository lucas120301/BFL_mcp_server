# Flux MCP Server Examples

This directory contains example scripts demonstrating how to use the Flux MCP Server for AI image generation.

## Examples

### 1. Basic Usage (`basic-usage.py`)

Demonstrates fundamental usage of the Flux MCP Server:

- Simple image generation
- Multiple image generation with different parameters
- Advanced parameter usage
- Error handling

**Run:**
```bash
python examples/basic-usage.py
```

### 2. Creative Prompts (`creative-prompts.py`)

Shows various creative prompt techniques and styles:

- Artistic styles (Van Gogh, photorealistic, fantasy, minimalist)
- Character concept art
- Environment concept art
- Creative prompt engineering tips

**Run:**
```bash
python examples/creative-prompts.py
```

## Prerequisites

Before running the examples, make sure you have:

1. **Installed dependencies:**
   ```bash
   uv sync --no-dev
   ```

2. **Set your API key:**
   ```bash
   export BFL_API_KEY="your_api_key_here"
   ```
   
   Or create a `.env` file:
   ```bash
   cp config/.env.example config/.env
   # Edit config/.env and add your API key
   ```

3. **MCP client library:**
   ```bash
   pip install mcp
   ```

## Running Examples

### Option 1: Run Individual Examples

```bash
# Basic usage
python examples/basic-usage.py

# Creative prompts
python examples/creative-prompts.py
```

### Option 2: Run All Examples

```bash
# Run all examples
for example in examples/*.py; do
    if [[ "$example" != "examples/README.md" ]]; then
        echo "Running $example..."
        python "$example"
        echo ""
    fi
done
```

## Example Output

When you run the examples, you'll see output like:

```
🚀 Flux MCP Server Examples
===========================

1. Basic Image Generation
------------------------------
🎨 Generating image: 'A beautiful sunset over mountains'
📋 Result:
{
  "content": [
    {
      "type": "text",
      "text": "{\"status\": \"success\", \"image\": \"https://api.bfl.ai/v1/get_result?id=...\", \"meta\": {...}}"
    }
  ]
}
✅ Image generated successfully!
🖼️  Image URL: https://api.bfl.ai/v1/get_result?id=...
```

## Customizing Examples

You can modify the examples to:

1. **Change prompts:** Edit the `prompt` parameter in the examples
2. **Adjust parameters:** Modify `aspect_ratio`, `safety_tolerance`, etc.
3. **Add new examples:** Create new Python files following the same pattern

## Troubleshooting

### Common Issues

1. **"BFL_API_KEY not set"**
   - Make sure you've set your API key as an environment variable
   - Or create a `.env` file in the `config/` directory

2. **"Connection refused"**
   - Make sure the MCP server is running
   - Check that you're in the correct directory

3. **"Module not found"**
   - Install the MCP client: `pip install mcp`
   - Make sure all dependencies are installed: `uv sync --no-dev`

### Getting Help

- Check the [API Reference](../docs/api-reference.md)
- Review the [Getting Started Guide](../docs/getting-started.md)
- Look at the [Deployment Guide](../docs/deployment.md)

## Contributing

Feel free to add your own examples! When creating new examples:

1. Follow the existing naming convention
2. Include proper error handling
3. Add descriptive comments
4. Update this README with your new example

## License

These examples are part of the Flux MCP Server project and are licensed under the same terms.
