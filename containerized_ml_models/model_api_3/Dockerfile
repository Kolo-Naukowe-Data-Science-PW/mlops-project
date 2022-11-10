FROM continuumio/anaconda3

COPY model.pkl model.pkl
COPY  api.py api.py
COPY requirements.txt requirements.txt

RUN conda env create --name virtual-env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "virtual-env", "--no-capture-output", "python", "api.py" ]