#!/bin/sh

# Execute script inside slave_api directory

echo "Building model_api_decision_tree"
sudo docker build -t azoz01/mlops-project:model-api-decision-tree --build-arg MODEL_DIR=decision_tree .
sudo docker push azoz01/mlops-project:model-api-decision-tree
echo "Building model_api_logistic"
sudo docker build -t azoz01/mlops-project:model-api-logistic --build-arg MODEL_DIR=logistic .
sudo docker push azoz01/mlops-project:model-api-logistic
echo "Building model_api_rf"
sudo docker build -t azoz01/mlops-project:model-api-rf --build-arg  MODEL_DIR=rf .
sudo docker push azoz01/mlops-project:model-api-rf