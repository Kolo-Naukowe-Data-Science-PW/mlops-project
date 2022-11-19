FROM continuumio/miniconda3

WORKDIR /app

COPY requirements.txt /app

RUN conda create -n env python=3.9 && conda run -n env pip install -r requirements.txt

COPY . . 

ENTRYPOINT [ "conda", "run", "-n", "env", "--no-capture-output", \
    "python", "api.py"]
