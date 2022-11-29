if [ -x "$(command -v docker)" ]; then
    for dir in models/*/; do
        dir=$(basename "$dir")
        docker build -t mlops-$dir":"latest --build-arg model="$dir" "$PWD/models/." 
    done
    minikube start -p ingress-cluster
    eval $(minikube -p minikube docker-env)
    address=$(minikube ip -p ingress-cluster)
    echo "Aby połączyć się z serwerem wejdź pod adres: $address"
else
    echo "Install docker!"
fi

