# Backend Server for my Master's Thesis

This backend server is built using FastAPI and serves as a critical component of my Master's thesis project. Its primary purpose is to facilitate the retrieval of similar vectors from the Qdrant database cluster.

# Running the server

To get the server up and running, you'll need to provide certain environment parameters. By default, these parameters are retrieved from the Pydantic configuration class named Settings. Here's a glimpse of what these default parameters look like:

```python
class Settings(BaseSettings):
    QDRANT_CLUSTER_HOST: str = "localhost"
    QDRANT_CLUSTER_PORT: int = 6333
```

The QDRANT_CLUSTER_HOST parameter is set to "localhost," indicating that the server is configured to communicate with a Qdrant cluster running on the same machine. The QDRANT_CLUSTER_PORT is set to the default port number for Qdrant.

To start the server, execute the following command in your terminal:

```bash
uvicorn main:app
```
