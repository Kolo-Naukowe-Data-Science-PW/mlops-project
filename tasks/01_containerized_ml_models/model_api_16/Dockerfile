FROM continuumio/miniconda3

COPY api.py model.pkl requirements.txt ./

<<<<<<< HEAD
RUN conda create --name virtual_env && \
    conda run -n virtual_env pip install -r requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "virtual_env", "python", "api.py" ]
=======
RUN conda config --add channels conda-forge
RUN conda env create --name virtual_env --file requirements.txt

ENTRYPOINT [ "conda", "run", "-n", "virtual_env", "python", "api.py" ]
>>>>>>> 8895743 (ingress not working + how to set an ingress controller while running kubernetes via docker-desktop not minikube)
