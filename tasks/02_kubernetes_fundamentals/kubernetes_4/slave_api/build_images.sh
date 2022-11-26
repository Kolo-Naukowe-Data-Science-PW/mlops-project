#!/bin/sh

# Execute script inside slave_api directory

echo "Building model_api_decision_tree"
sudo docker build -t azoz01/mlops-project:model-api-decision-tree --build-arg MODEL_DIR=decision_tree .
echo "Building model_api_logistic"
sudo docker build -t azoz01/mlops-project:model-api-logistic --build-arg MODEL_DIR=logistic .
echo "Building model_api_rf"
sudo docker build -t azoz01/mlops-project:model-api-rf --build-arg  MODEL_DIR=rf .

# Afterwards required docker push for all built images in order
# to have them published