
kubectl autoscale ml-model-deployment --min=1 --max=3 --cpu-percent=80
kubectl apply -f namespace.yaml -f services.yaml -f networking.yaml -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
