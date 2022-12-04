if [ -x "$(command -v docker)" ]; then
    cd "$(dirname "$0")" && cd ..
    for dir in models/*/; do
        dir=$(basename "$dir")
        docker build -t mlops-$dir":"latest --build-arg model="$dir" "$PWD/models/." 
    done
    kubectl apply -f k8s-specifications
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.0/deploy/static/provider/cloud/deploy.yaml
else
    echo "Install docker!"
fi

