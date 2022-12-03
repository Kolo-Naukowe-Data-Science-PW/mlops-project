FROM continuumio/anaconda3

COPY model.pkl api.py requirements.txt /

RUN conda env create --name ml-env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "ml-env", "--no-capture-output", "python", "api.py" ]
