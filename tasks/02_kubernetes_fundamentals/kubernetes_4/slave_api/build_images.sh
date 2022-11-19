#!/bin/sh

# Execute script inside slave_api directory

echo "Building model_api_decision_tree"
sudo docker build -t models/model-api-decision-tree --build-arg MODEL_DIR=decision_tree .
echo "Building model_api_logistic"
sudo docker build -t models/model-api-logistic --build-arg MODEL_DIR=logistic .
echo "Building model_api_rf"
sudo docker build -t models/model-api-rf --build-arg  MODEL_DIR=rf .