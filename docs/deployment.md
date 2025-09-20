# Deployment Guide

## Deploying to Dedalus Labs

### Prerequisites

1. **Dedalus Account**: Sign up at [Dedalus Labs](https://dedalus.ai/)
2. **API Key**: Get your Black Forest Labs API key from [api.bfl.ai](https://api.bfl.ai/)
3. **Project Structure**: Ensure your project follows the required structure

### Required Project Structure

Your project must have the following structure for Dedalus deployment:

```
flux-mcp-main/
├── main.py                 # Entry point (required)
├── pyproject.toml          # Package configuration (required)
├── src/
│   └── main.py            # MCP server implementation (required)
├── config/
│   └── .env.example       # Environment template
├── docs/                  # Documentation (optional)
├── examples/              # Usage examples (optional)
└── scripts/               # Deployment scripts (optional)
```

### Deployment Steps

#### 1. Set Environment Variables

In the Dedalus UI, set the following environment variables:

- `BFL_API_KEY`: Your Black Forest Labs API key (required)

Optional environment variables:
- `FLUX_MODEL`: Default model to use (default: "flux-pro-1.1")
- `DEFAULT_ASPECT_RATIO`: Default aspect ratio (default: "16:9")
- `DEFAULT_WIDTH`: Default width (default: 1024)
- `DEFAULT_HEIGHT`: Default height (default: 1024)
- `DEFAULT_SAFETY_TOLERANCE`: Default safety tolerance (default: 6)

#### 2. Deploy the Server

```bash
dedalus deploy . --name "flux-image-generator"
```

#### 3. Verify Deployment

After deployment, test your server:

```bash
# Test the deployment
dedalus test flux-image-generator
```

### How Dedalus Runs Your Server

1. **Dependency Installation**: Dedalus runs `uv sync` to install dependencies from `pyproject.toml`
2. **Server Startup**: Dedalus runs `uv run main` to start your MCP server
3. **Container Environment**: Your server runs in a containerized environment at `/app`
4. **Environment Variables**: All environment variables are available to your server

### Production Considerations

#### Rate Limiting

The server includes built-in rate limiting to protect your API key:
- 10 requests per minute per user
- Automatic retry with exponential backoff
- Graceful error handling

#### Error Handling

- All API errors are caught and returned as structured responses
- Timeout handling for long-running generations
- Automatic retry for transient failures

#### Monitoring

- Log all generation requests and responses
- Track API usage and costs
- Monitor error rates and performance

### Environment Configuration

#### Required Variables

```bash
BFL_API_KEY=your_black_forest_labs_api_key
```

#### Optional Variables

```bash
# Model configuration
FLUX_MODEL=flux-pro-1.1
DEFAULT_ASPECT_RATIO=16:9
DEFAULT_WIDTH=1024
DEFAULT_HEIGHT=1024
DEFAULT_SAFETY_TOLERANCE=6

# Server configuration
LOG_LEVEL=INFO
MAX_CONCURRENT_REQUESTS=5
REQUEST_TIMEOUT=180
```

### Security Best Practices

1. **API Key Protection**
   - Never commit API keys to version control
   - Use environment variables for all sensitive data
   - Rotate API keys regularly

2. **Input Validation**
   - Validate all input parameters
   - Sanitize prompts to prevent injection attacks
   - Implement rate limiting

3. **Error Handling**
   - Don't expose sensitive information in error messages
   - Log errors securely
   - Implement proper error codes

### Scaling Considerations

#### Horizontal Scaling

- Dedalus automatically handles horizontal scaling
- Each instance can handle multiple concurrent requests
- Load balancing is handled by the platform

#### Vertical Scaling

- Adjust container resources in Dedalus UI
- Monitor memory and CPU usage
- Scale based on request volume

#### Cost Optimization

- Monitor API usage and costs
- Implement caching for repeated requests
- Use appropriate model sizes for your use case

### Troubleshooting Deployment

#### Common Issues

1. **Build Failures**
   - Check `pyproject.toml` syntax
   - Verify all dependencies are available
   - Review build logs in Dedalus UI

2. **Runtime Errors**
   - Check environment variables are set correctly
   - Verify API key is valid and has credits
   - Review server logs for error details

3. **Performance Issues**
   - Monitor request latency
   - Check API rate limits
   - Optimize prompt complexity

#### Debugging

1. **Local Testing**
   ```bash
   # Test locally before deployment
   uv run main
   ```

2. **Log Analysis**
   - Check Dedalus logs for error details
   - Monitor API response times
   - Track error rates and patterns

3. **Health Checks**
   - Implement health check endpoints
   - Monitor server availability
   - Set up alerts for failures

### Maintenance

#### Regular Tasks

1. **Update Dependencies**
   - Keep dependencies up to date
   - Test updates in staging environment
   - Monitor for security vulnerabilities

2. **Monitor Usage**
   - Track API costs and usage
   - Monitor performance metrics
   - Review error logs

3. **Backup Configuration**
   - Export environment variables
   - Document configuration changes
   - Maintain deployment scripts

### Support

- **Dedalus Documentation**: [docs.dedalus.ai](https://docs.dedalus.ai/)
- **Black Forest Labs API**: [api.bfl.ai/docs](https://api.bfl.ai/docs)
- **MCP Protocol**: [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
