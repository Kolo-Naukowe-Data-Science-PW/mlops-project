if [ -x "$(command -v docker)" ]; then
    for dir in models/*/; do
        dir=$(basename "$dir")
        docker build -t mlops-$dir":"latest --build-arg model="$dir" "$PWD/models/." 
    done
else
    echo "Install docker!"
fi