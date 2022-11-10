FROM continuumio/anaconda3

RUN mkdir model_api
COPY . model_api/containerized_ml_models/api
WORKDIR /model_api
RUN conda create -n api_env python==3.9
RUN conda run -n api_env pip install \
    -r containerized_ml_models/api/requirements.txt

ENV PYTHONPATH="/model_api/"
ENTRYPOINT [ \
    "conda", "run", \
    "-n", "api_env", \
    "flask", "--app", "containerized_ml_models/api/api.py", \
    "run", \
    "--port", "8080" \
    ]