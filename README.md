# APAN All-in-One Docker Stack

This project is an implementation of a stack based on Docker (docker-compose) using MongoDB, PostgreSQL, Express JS (Node.js), Flask, Jupyter, and more.

## Features

- **MongoDB**: NoSQL database
- **PostgreSQL**: Relational database
- **Express JS (Node.js)**: Web framework for Node.js
- **Flask**: Micro web framework for Python
- **Jupyter**: Interactive computing environment
- **Streamlit**: Web app framework for Machine Learning and Data Science
- **Ollama**: AI model hosting and management
- **Ollama WebUI**: Web interface for managing AI models
- **Neo4j**: Graph database (newly added)

## Building & Running

```sh
# Clone the repository
git clone https://github.com/hyper07/apan-project.git

# Move to the project directory
cd apan-project/

# Build and run the containers
docker-compose up -d

# Stop and remove the containers
docker-compose down
```

## Accessing Services

### MongoDB

- **Connection String**:
  ```python
  from pymongo import MongoClient
  client = MongoClient('mongodb://admin:PassW0rd@apan-mongo:27017/')
  ```

### PostgreSQL

- **Web Interface (PgAdmin)**: [http://localhost:5080](http://localhost:5080)
- **Connection Details**:
  ```
  Hostname: apan-postgres
  Port: 5432
  Database: db
  Username: admin
  Password: PassW0rd
  ```

### Jupyter

- **Web Interface**: [http://localhost:8899](http://localhost:8899)

### Flask App

- **Web Interface**: [http://localhost:5010](http://localhost:5010)

### Streamlit App

- **Web Interface**: [http://localhost:18501](http://localhost:18501)

### Ollama

- **API Endpoint**: [http://localhost:37869](http://localhost:37869)

# Download the Ollama model
```sh
docker exec -ti apan-ollama ollama pull llama3.2:1b
# or 
docker exec -ti apan-ollama ollama pull qwen2.5-coder
```

### Ollama WebUI

- **Web Interface**: [http://localhost:38080](http://localhost:38080)

### Neo4j

- **Web Interface**: [http://localhost:7474](http://localhost:7474)
- **Bolt Protocol**: `bolt://localhost:7687`
- **Connection Details**:
  ```
  Username: neo4j
  Password: password
  ```

## Additional Information

- **Docker Network**: All services are connected via a custom Docker network `apan-net`.
- **Volumes**: Persistent data storage is managed using Docker volumes.

For more detailed information on each service, please refer to the respective documentation.