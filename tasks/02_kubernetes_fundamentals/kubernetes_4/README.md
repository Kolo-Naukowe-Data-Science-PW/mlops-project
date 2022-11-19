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

### **Testing**
You need to run api image:
```
docker run -p 5000:5000 <image name (can be found in script)>
```
Test request
```
curl -X POST http://127.0.0.1:5000/predict --data '{"Alcohol": 14.23, "Malic.acid": 1.71, "Ash": 2.43, "Acl": 15.6, "Mg": 127, "Phenols": 2.8, "Flavanoids": 3.06, "Nonflavanoid.phenols": 0.28, "Proanth": 2.29, "Color.int": 5.64, "Hue": 1.04, "OD": 3.92, "Proline": 1065}' -H "Content-type: application/json"
```

**Warning**: As for now deployment as kubernetes service doesn't work.
