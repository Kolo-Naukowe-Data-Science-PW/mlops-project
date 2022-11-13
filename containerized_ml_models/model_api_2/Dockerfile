FROM continuumio/miniconda3

COPY api.py requirements.txt  model.pkl ./

RUN conda create -n myenv python=3.9 && \
    conda run -n myenv pip install -r requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "myenv", "flask", "--app", "api.py", "run"]