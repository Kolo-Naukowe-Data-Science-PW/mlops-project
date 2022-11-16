# Docker container with ML model
Docker container with an API that allows you to query the ML model saved in a pickle file.

## Running

<br />

### 1. With Docker

Go to containerized_ml_models/model_api_14 directory **(only if you are in the main project directory)**
```
cd containerized_ml_models/model_api_14
```
Build docker container
```
docker build -t ml-ops .
```
Run docker container
```
docker run -dp 5000:5000 ml-ops
```
Go to http://localhost:5000/ping to check if everything is OK.
On this page you should see
```
{"ping":"success"}
```
**HINT:**: To manage (start, delete, etc.) docker containers please use [Docker Desktop](https://www.docker.com/products/docker-desktop/) app.

<br />

### 2. Local environment (without docker / for development purpose)

Go to containerized_ml_models/model_api_14 directory **(only if you are in the main project directory)**
```
cd containerized_ml_models/model_api_14
```
Create conda environment
```
conda env create --name ml-ops --file requirements.txt
```

Run API using conda
```
conda run -n ml-ops --no-capture-output python api.py
```
Go to http://localhost:5000/ping to check if everything is OK.
On this page you should see
```
{"ping":"success"}
```

<br />

## API testing

In terminal send query to model in order to make a predicton

```
curl -X POST 127.0.0.1:5000/predict -d '[[1,2.65,3,4,5,6.124,7,8,9,10], [1,2,67,4,5,7.065,7,1,9,10]]'
```
