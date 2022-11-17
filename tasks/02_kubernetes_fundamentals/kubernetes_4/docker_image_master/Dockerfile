FROM continuumio/anaconda3

COPY app.py requirements.txt ./

RUN conda env create --name ml-ops --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "ml-ops", "--no-capture-output", "python", "app.py" ]
