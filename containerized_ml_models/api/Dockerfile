FROM continuumio/anaconda3

COPY . containerized_ml_models/api

RUN conda create -n api_env python==3.9
RUN conda run -n api_env pip install -r containerized_ml_models/api/requirements.txt

ENTRYPOINT [ \
    "conda", "run", \
    "-n", "api_env", \
    "flask", "--app", "containerized_ml_models/api/api.py", \
    "run", \
    "--port", "8080" \
    ]