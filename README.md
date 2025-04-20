# Balena Embed

A lightweight FastAPI server for generating 384-dimensional dense vector embeddings from text using the MiniLM-L6 model (`all-MiniLM-L6-v2`). Useful for semantic search, text similarity, and other NLP tasks.

## Features

- Simple REST API for text embedding
- Fast inference with Sentence Transformers
- Docker and direct Python support
- Returns embeddings as JSON arrays
- Handles invalid input with clear error messages

## Installation

### Using Docker

1. Build the Docker image:
   ```sh
   docker build -t balena-embed .
   ```
2. Run the server:
   ```sh
   docker run -p 6700:6700 balena-embed
   ```

### Direct Installation 

1. Install Python 3.11 (or 3.11 slim) and pip if not already installed.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start the server:
   ```sh
   python embed_server.py
   ```

## Usage

Send a POST request to `http://localhost:6700/embed` with JSON body:

```json
{ 
    "text": "your text here" 
}
```

The response will be a JSON object with a 384-dimensional embedding vector:

```json
{ 
    "embedding": [0.123, ...] 
}
```

## Error Handling

- If the `text` field is missing or not a string, the server returns a 422 error with details.
- If the model fails to generate an embedding, a 500 error is returned.

## Requirements

- Python 3.11 or 3.11 slim
- pip (for direct install)
- Docker (for containerized install)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the GPL 3.0 License. See the [LICENSE](./LICENSE) file for details.