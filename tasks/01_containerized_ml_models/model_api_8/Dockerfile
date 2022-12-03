FROM continuumio/miniconda3

COPY model.pkl requirements.txt api.py ./

EXPOSE 8000

RUN conda update -n base conda && \
    conda create -n venv python=3.9 && \
    conda run -n venv pip install -r requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "venv", "python", "-m", "api" ]
