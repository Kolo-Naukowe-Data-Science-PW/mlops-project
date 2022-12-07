FROM continuumio/anaconda3
ARG MODEL_DIR

COPY models/$MODEL_DIR/model.pkl .
COPY api.py requirements.txt /

ENV PYTHONPATH=/
ENV MODEL_PATH="model.pkl"

RUN conda create -n api_env python==3.9
RUN conda run -n api_env pip install \
    -r requirements.txt

ENTRYPOINT conda run -n api_env \
    flask --app api.py \
    run --host 0.0.0.0 --port 5000