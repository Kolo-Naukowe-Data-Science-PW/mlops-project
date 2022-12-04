FROM continuumio/miniconda3

WORKDIR /app

ARG model

ENV MODEL=${model}

COPY pod_api.py ${MODEL}/${MODEL}.pkl requirements.txt ./

RUN conda create -n env python=3.9 && \
    conda run -n env pip install -r requirements.txt

ENTRYPOINT conda run -n env --no-capture-output \
    python pod_api.py $MODEL
