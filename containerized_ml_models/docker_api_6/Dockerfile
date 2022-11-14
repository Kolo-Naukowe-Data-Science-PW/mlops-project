FROM continuumio/anaconda3

COPY ./ / 

RUN conda env create --name ml-env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "ml-env", \
    "--no-capture-output", "python", "api_predict.py" ]