FROM continuumio/miniconda3

COPY api.py model.pkl requirements.txt ./

RUN conda create --name virtual_env 
RUN conda run -n virtual_env pip install -r requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "virtual_env", "python", "api.py" ]