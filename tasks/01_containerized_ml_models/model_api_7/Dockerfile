FROM continuumio/anaconda3

COPY app.py model.pkl requirements.txt /

RUN conda create --name env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "env" ,"--no-capture-output", "python", "app.py"]