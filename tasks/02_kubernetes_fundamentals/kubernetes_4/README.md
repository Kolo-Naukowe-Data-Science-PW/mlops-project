# Kubernetes with ML model

Kubernetes cluster with voting classifier.

<br />

## Voting classifier (master)

<br />

### **Running (for development purpose)**

<br />

Go to directory with voting classifier (master) files **(only if you are in the main project directory)**
```
cd tasks/02_kubernetes_fundamentals/kubernetes_4/docker_image_master
```
Add execute permission to prepared bash script
```
chmod +x ./dev_build_and_run.sh
```
Build and run docker container
```
./dev_build_and_run.sh
```
Go to http://localhost:5000/ping to check if everything is OK.
On this page you should see
```
{"ping":"success"}
```
**HINT:**: To manage (start, delete, etc.) docker containers please use [Docker Desktop](https://www.docker.com/products/docker-desktop/) app.

<br />

### **Testing**

In terminal send query to make a predicton

```
curl -X POST 127.0.0.1:5000/predict -d '{"probabilities": [0.1, 0.5, 0.4]}'
```