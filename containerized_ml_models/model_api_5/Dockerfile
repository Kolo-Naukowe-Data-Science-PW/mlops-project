FROM continuumio/anaconda3

COPY model.pkl requirements.txt api.py /

RUN conda create --name mlopsenv --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "mlopsenv" ,"--no-capture-output", "python", "api.py"]