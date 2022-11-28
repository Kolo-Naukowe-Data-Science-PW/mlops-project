FROM continuumio/miniconda3

COPY api.py model.pkl requirements.txt ./

RUN conda config --add channels conda-forge
RUN conda env create --name virtual_env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "virtual_env", "python", "api.py" ]