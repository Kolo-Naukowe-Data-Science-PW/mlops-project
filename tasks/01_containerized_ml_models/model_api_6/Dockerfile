FROM continuumio/anaconda3

COPY ./ / 

RUN conda env create --name ml-env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "ml-env", \
    "--no-capture-output", "flask", "--app", \
    "api_predict.py", "run", "--port", "5000"]
