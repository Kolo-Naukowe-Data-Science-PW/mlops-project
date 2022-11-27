kubectl autoscale ml-model-deployment --min=1 --max=3 --cpu-percent=80
kubectl apply -f namespace.yaml -f model-1.yaml -f model-2.yaml -f networking.yaml -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
kubectl delete all --all -n mlops
kubectl config set-context --current --namespace=mlops