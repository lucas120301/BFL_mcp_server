# API Reference

## Flux MCP Server API

The Flux MCP Server provides a single tool for AI-powered image generation using Black Forest Labs' Flux models.

## Tools

### `flux_generate`

Generates images from text prompts using Flux AI models.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | - | Text description of the image to generate |
| `model` | string | No | "flux-pro-1.1" | Flux model to use for generation |
| `aspect_ratio` | string | No | "16:9" | Image aspect ratio (e.g., "16:9", "1:1", "4:3") |
| `width` | integer | No | 1024 | Image width in pixels (used when aspect_ratio is not specified) |
| `height` | integer | No | 1024 | Image height in pixels (used when aspect_ratio is not specified) |
| `raw` | boolean | No | false | Use raw mode for more creative/unfiltered outputs |
| `safety_tolerance` | integer | No | 6 | Safety filter level (0-10, higher = more restrictive) |
| `prompt_upsampling` | boolean | No | false | Enhance prompt quality automatically |

#### Supported Models

- `flux-pro-1.1`: Latest Flux Pro model (recommended for best quality)
- `flux-dev`: Development model (may have experimental features)
- `flux-schnell`: Fast generation model (faster but potentially lower quality)

#### Supported Aspect Ratios

- `1:1` - Square (1024x1024)
- `16:9` - Widescreen (1024x576)
- `9:16` - Portrait (576x1024)
- `4:3` - Standard (1024x768)
- `3:4` - Portrait standard (768x1024)
- `21:9` - Ultra-wide (1024x439)
- `9:21` - Ultra-tall (439x1024)

#### Response Format

**Success Response:**
```json
{
  "status": "success",
  "image": "https://api.bfl.ai/v1/get_result?id=...",
  "meta": {
    "request_id": "req_123456789",
    "model": "flux-pro-1.1",
    "result": {
      "sample": "https://api.bfl.ai/v1/get_result?id=...",
      "status": "Ready"
    }
  }
}
```

**Error Response:**
```json
{
  "status": "error",
  "message": "Error description"
}
```

#### Example Usage

**Basic Image Generation:**
```python
result = await flux_generate(
    prompt="A serene mountain landscape at sunset"
)
```

**Custom Parameters:**
```python
result = await flux_generate(
    prompt="A futuristic cityscape with flying cars",
    model="flux-pro-1.1",
    aspect_ratio="16:9",
    safety_tolerance=4,
    prompt_upsampling=True
)
```

**Square Image:**
```python
result = await flux_generate(
    prompt="A portrait of a cat wearing a space helmet",
    aspect_ratio="1:1",
    raw=True
)
```

**Custom Dimensions:**
```python
result = await flux_generate(
    prompt="A detailed architectural drawing",
    width=1920,
    height=1080,
    safety_tolerance=8
)
```

## Error Codes

| Error | Description | Solution |
|-------|-------------|----------|
| `BFL_API_KEY not set` | API key environment variable is missing | Set the `BFL_API_KEY` environment variable |
| `Generation failed` | The image generation request failed | Check your prompt and try again |
| `Request timeout` | The generation took too long | Try a simpler prompt or different model |
| `Invalid model` | The specified model is not available | Use a supported model name |
| `Invalid aspect ratio` | The aspect ratio format is incorrect | Use a supported aspect ratio format |
| `API rate limit exceeded` | Too many requests in a short time | Wait before making another request |

## Rate Limits

- **Requests per minute**: 10 requests per minute per user
- **Concurrent requests**: Up to 5 concurrent requests
- **Request timeout**: 180 seconds maximum per request

## Best Practices

### Prompt Engineering

1. **Be Specific**: Include details about style, composition, lighting, and mood
2. **Use Descriptive Language**: "A majestic mountain peak" vs "mountain"
3. **Include Style References**: "in the style of Van Gogh" or "photorealistic"
4. **Specify Quality**: "high resolution", "detailed", "professional photography"

### Parameter Selection

1. **Model Choice**:
   - Use `flux-pro-1.1` for best quality
   - Use `flux-schnell` for faster generation
   - Use `flux-dev` for experimental features

2. **Aspect Ratio**:
   - Use `16:9` for landscapes and general use
   - Use `1:1` for social media and portraits
   - Use `9:16` for mobile/vertical content

3. **Safety Tolerance**:
   - Use 6-8 for general content
   - Use 4-5 for creative/artistic content
   - Use 8-10 for family-friendly content

### Performance Optimization

1. **Prompt Length**: Keep prompts concise but descriptive (50-200 words)
2. **Complexity**: Simpler prompts generate faster
3. **Retry Logic**: Implement exponential backoff for failed requests
4. **Caching**: Cache results for identical prompts when possible

## Integration Examples

### Python Client

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def generate_image(prompt: str):
    async with stdio_client(StdioServerParameters(
        command="uv",
        args=["run", "main"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            result = await session.call_tool(
                "flux_generate",
                {"prompt": prompt}
            )
            return result

# Usage
result = asyncio.run(generate_image("A beautiful sunset"))
print(result)
```

### JavaScript/TypeScript Client

```typescript
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';

async function generateImage(prompt: string) {
  const transport = new StdioClientTransport({
    command: 'uv',
    args: ['run', 'main']
  });
  
  const client = new Client({
    name: 'flux-client',
    version: '1.0.0'
  }, {
    capabilities: {}
  });
  
  await client.connect(transport);
  
  const result = await client.callTool('flux_generate', {
    prompt: prompt
  });
  
  return result;
}
```

## Troubleshooting

### Common Issues

1. **Slow Generation**
   - Complex prompts take longer to process
   - Try simplifying your prompt
   - Use `flux-schnell` model for faster generation

2. **Quality Issues**
   - Use more descriptive prompts
   - Enable `prompt_upsampling`
   - Try different aspect ratios

3. **Safety Filter Triggered**
   - Adjust `safety_tolerance` parameter
   - Reword your prompt to be more appropriate
   - Use `raw=true` for creative content (with caution)

4. **API Errors**
   - Check your API key is valid and has credits
   - Verify your internet connection
   - Check Black Forest Labs API status

### Debug Mode

Enable debug logging by setting the environment variable:
```bash
LOG_LEVEL=DEBUG
```

This will provide detailed information about:
- Request/response details
- API call timing
- Error stack traces
- Performance metrics
