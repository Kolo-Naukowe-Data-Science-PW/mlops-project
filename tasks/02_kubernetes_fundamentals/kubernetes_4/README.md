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

<br />

## Voting classifier (slave)

### **Specs**
There are 3 services exposed on port `5000` under static IP addresses:
1. `decision-tree-model-api` - `10.96.1.1`
2. `logistic-model-api` - `10.96.1.2`
3. `rf-model-api` - `10.96.1.3`

Each of service have 2 endpoints:
1. `/ping` - GET
2. `/predict` - POST

### **Image build**
In order to build images enclosing slave models you need to:
1. Be in proper directory
```
cd tasks/02_kubernetes_fundamentals/kubernetes_4/slave_api
```
2. Add execute permissions to bash script
```
chmod +x ./build_images.sh
```
3. Run build script
```
./build_images.sh
```

### **Running kubernetes services**
1. Be in proer directory
```
cd tasks/02_kubernetes_fundamentals/kubernetes_4
```
2.  Apply changes to kubernetes cluster
```
sudo kubectl apply -f k8s/dev/
```
### **Testing**
You need to connect to minikube cluster using `minikube ssh` and then you can use curl to send requests to particular services.
Test request
```
curl -X POST <IP_ADDRESS>/predict --data '{"Alcohol": 14.23, "Malic.acid": 1.71, "Ash": 2.43, "Acl": 15.6, "Mg": 127, "Phenols": 2.8, "Flavanoids": 3.06, "Nonflavanoid.phenols": 0.28, "Proanth": 2.29, "Color.int": 5.64, "Hue": 1.04, "OD": 3.92, "Proline": 1065}' -H "Content-type: application/json"
```
