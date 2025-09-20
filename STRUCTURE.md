# Project Structure

This document explains the structure of the Flux MCP Server project and how it's organized for Dedalus Labs deployment.

## Directory Structure

```
flux-mcp-main/
├── main.py                 # Entry point (required by Dedalus)
├── pyproject.toml          # Package configuration with dependencies
├── README.md              # Project documentation
├── STRUCTURE.md           # This file - project structure documentation
├── LICENSE                # MIT license
├── src/                   # Source code
│   ├── main.py           # MCP server implementation
│   └── flux_adapter.py   # Black Forest Labs API adapter
├── config/               # Configuration files
│   └── .env.example      # Environment variables template
├── docs/                 # Documentation
│   ├── getting-started.md
│   ├── deployment.md
│   └── api-reference.md
├── examples/             # Usage examples
│   ├── basic-usage.py
│   ├── creative-prompts.py
│   └── README.md
├── scripts/              # Deployment and utility scripts
│   ├── deploy.sh
│   └── test-local.sh
└── tests/                # Test files
    └── image_generation.py
```

## File Descriptions

### Core Files

#### `main.py` (Root)
- **Purpose**: Entry point that Dedalus Labs expects
- **Content**: Simple import and run of the MCP server
- **Required by**: Dedalus Labs deployment system

#### `pyproject.toml`
- **Purpose**: Package configuration and dependencies
- **Content**: Project metadata, dependencies, build configuration
- **Required by**: uv package manager and Dedalus Labs

#### `src/main.py`
- **Purpose**: Actual MCP server implementation
- **Content**: FastMCP server setup, tool definitions, business logic
- **Imports**: flux_adapter.py for API interactions

#### `src/flux_adapter.py`
- **Purpose**: Black Forest Labs API integration
- **Content**: API client, request handling, polling logic
- **Features**: Async support, error handling, retry logic

### Configuration

#### `config/.env.example`
- **Purpose**: Template for environment variables
- **Content**: API key configuration and optional settings
- **Usage**: Copy to `.env` and fill in actual values

### Documentation

#### `docs/getting-started.md`
- **Purpose**: Quick start guide for users
- **Content**: Installation, configuration, basic usage

#### `docs/deployment.md`
- **Purpose**: Dedalus Labs deployment guide
- **Content**: Deployment steps, environment setup, troubleshooting

#### `docs/api-reference.md`
- **Purpose**: Complete API documentation
- **Content**: Tool parameters, response formats, examples

### Examples

#### `examples/basic-usage.py`
- **Purpose**: Basic usage demonstration
- **Content**: Simple image generation examples

#### `examples/creative-prompts.py`
- **Purpose**: Advanced prompt techniques
- **Content**: Creative styles, character concepts, environments

#### `examples/README.md`
- **Purpose**: Examples documentation
- **Content**: How to run examples, customization tips

### Scripts

#### `scripts/deploy.sh`
- **Purpose**: Automated deployment to Dedalus Labs
- **Content**: Deployment commands, environment checks

#### `scripts/test-local.sh`
- **Purpose**: Local testing and development
- **Content**: Dependency installation, local server startup

### Tests

#### `tests/image_generation.py`
- **Purpose**: Test image generation functionality
- **Content**: Unit tests for the MCP server

## Dedalus Labs Requirements

### Required Structure

Dedalus Labs expects the following structure:

1. **`main.py` in root**: Entry point that runs `uv run main`
2. **`pyproject.toml`**: Package configuration with dependencies
3. **`src/main.py`**: The actual MCP server code
4. **Environment variables**: Set in Dedalus UI, not in files

### How Dedalus Runs the Server

1. **Installation**: Runs `uv sync` to install dependencies from `pyproject.toml`
2. **Startup**: Runs `uv run main` to start the server
3. **Environment**: Server runs in `/app` directory in container
4. **Variables**: Environment variables are injected by the platform

### Deployment Process

```bash
# 1. Set environment variables in Dedalus UI
BFL_API_KEY=your_api_key_here

# 2. Deploy
dedalus deploy . --name "flux-image-generator"

# 3. Dedalus automatically:
#    - Installs dependencies with uv sync
#    - Runs uv run main
#    - Provides environment variables
```

## Development Workflow

### Local Development

1. **Setup**:
   ```bash
   uv sync --no-dev
   cp config/.env.example config/.env
   # Edit config/.env with your API key
   ```

2. **Test**:
   ```bash
   ./scripts/test-local.sh
   ```

3. **Run Examples**:
   ```bash
   python examples/basic-usage.py
   ```

### Deployment

1. **Test Locally**:
   ```bash
   ./scripts/test-local.sh
   ```

2. **Deploy**:
   ```bash
   ./scripts/deploy.sh
   ```

3. **Verify**:
   ```bash
   dedalus test flux-image-generator
   ```

## Key Design Decisions

### MCP Server Architecture

- **FastMCP**: Used for easy MCP server creation
- **Async Support**: All operations are async for better performance
- **Error Handling**: Comprehensive error handling and user-friendly messages

### API Integration

- **Adapter Pattern**: Separate adapter for Black Forest Labs API
- **Retry Logic**: Automatic retry for transient failures
- **Polling**: Handles async image generation with polling

### Configuration Management

- **Environment Variables**: All configuration via environment variables
- **Local Development**: Support for `.env` files during development
- **Production**: Environment variables injected by Dedalus

### Documentation

- **Comprehensive**: Complete documentation for all aspects
- **Examples**: Working examples for common use cases
- **Deployment**: Step-by-step deployment guide

## Security Considerations

### API Key Protection

- **Environment Variables**: API keys never stored in code
- **Template Files**: `.env.example` provides template without secrets
- **Rate Limiting**: Built-in protection against abuse

### Input Validation

- **Parameter Validation**: All inputs validated before API calls
- **Error Handling**: Safe error messages without sensitive information
- **Safety Filters**: Configurable content filtering

## Performance Optimization

### Async Operations

- **Non-blocking**: All operations are async
- **Concurrent Requests**: Support for multiple concurrent generations
- **Efficient Polling**: Optimized polling for API responses

### Caching

- **Response Caching**: Cache identical requests when possible
- **Metadata Storage**: Store generation metadata for debugging

## Monitoring and Logging

### Logging

- **Structured Logging**: JSON-formatted logs for easy parsing
- **Error Tracking**: Comprehensive error logging
- **Performance Metrics**: Track generation times and success rates

### Health Checks

- **API Health**: Monitor Black Forest Labs API availability
- **Server Health**: Health check endpoints for monitoring
- **Metrics**: Track usage and performance metrics

## Future Enhancements

### Planned Features

- **Batch Generation**: Support for generating multiple images at once
- **Image Variations**: Generate variations of existing images
- **Style Transfer**: Apply artistic styles to generated images
- **Image Editing**: Basic image editing capabilities

### Scalability

- **Horizontal Scaling**: Support for multiple server instances
- **Load Balancing**: Distribute requests across instances
- **Caching Layer**: Redis-based caching for better performance

## Contributing

When contributing to this project:

1. **Follow Structure**: Maintain the existing directory structure
2. **Documentation**: Update relevant documentation files
3. **Examples**: Add examples for new features
4. **Tests**: Include tests for new functionality
5. **Scripts**: Update deployment scripts if needed

## Support

For questions about the project structure:

- Check the [Deployment Guide](docs/deployment.md)
- Review the [API Reference](docs/api-reference.md)
- Look at the [Examples](examples/README.md)
- Open an issue for specific questions
