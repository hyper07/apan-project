# APAN All-in-One Docker Stack

This project is an implementation of a stack based on Docker (docker-compose) using MongoDB, PostgreSQL, Neo4j, Node.js, Flask, Jupyter, and more.

## Features

- **MongoDB**: NoSQL database
- **PostgreSQL**: Relational database
- **NodeJS API**: Build DB structure and create API
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
- **Web Sample Form**: [http://localhost:5010/form](http://localhost:5010/form)

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

![select model](./app-streamlit/images/select_llm.png)

#### Download LLM Models

To download a model, use the following command:
```sh
docker exec -ti apan-ollama ollama pull <model-name>
```
For example:
```sh
docker exec -ti apan-ollama ollama pull llama3.2:1b
docker exec -ti apan-ollama ollama pull qwen2.5-coder
```
![download model](./app-streamlit/images/download_llm.png)


#### Select a Model in the WebUI

1. Open the Ollama WebUI at [http://localhost:38080](http://localhost:38080).
2. Navigate to the "Models" section.
3. Select the desired model from the list or upload a custom model.
4. Save the configuration and start using the selected model.

### Neo4j

- **Web Interface**: [http://localhost:7874](http://localhost:7874)
- **Bolt Protocol**: `bolt://localhost:7887`
- **Connection Details**:
  ```
  Username: neo4j
  Password: password
  ```

### Adminer

- **Web Interface**: [http://localhost:9080](http://localhost:9080)

### Mongo Express

- **Web Interface**: [http://localhost:8081](http://localhost:8081)

# HOW TO ACCESS DATABASE AND API
For detailed instructions on how to access and interact with the databases, 
refer to the [HowToUse.md guide](https://github.com/hyper07/apan-project/blob/main/files/work/HowToUse.md).

## Additional Information

- **Docker Network**: All services are connected via a custom Docker network `apan-net`.
- **Volumes**: Persistent data storage is managed using Docker volumes.

For more detailed information on each service, please refer to the respective documentation.