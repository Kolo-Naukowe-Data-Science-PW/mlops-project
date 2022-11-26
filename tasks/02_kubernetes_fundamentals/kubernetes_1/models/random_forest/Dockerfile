FROM continuumio/anaconda3

COPY random_forest_api.py random_forest_model.pkl requirements.txt ./

RUN conda create --name env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "env", "--no-capture-output", "python", "random_forest_api.py"]