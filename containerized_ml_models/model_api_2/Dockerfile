FROM continuumio/miniconda3

COPY api.py requirements.txt  model.pkl ./

RUN conda create -n myenv python=3.9 && \
    conda run -n myenv pip install -r requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "myenv","--no-capture-output", \
    "flask", "--app", "api.py", \
    "run", "-h", "0.0.0.0", "-p", "5000"]