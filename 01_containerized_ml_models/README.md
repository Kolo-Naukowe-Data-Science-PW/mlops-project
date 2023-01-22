### Narzędzia i technologie z którymi warto się zapoznać:

- docker -> [tutorial](https://docs.docker.com/get-started/02_our_app/)
- conda -> [getting-started](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- flask API -> [python tutorial](https://pythonbasics.org/flask-rest-api/)
- pickle -> [python tutorial](https://pythonarray.com/how-to-pickle-unpickle-tutorial/)

To formatowania kodu w pythonie ogarnijcie sobie te 2 narzędzia:

- flake8
- black

---

### Zadanie

Mając do dyspozycji plik `model.pkl` zawierający obiekt pythonowy (model) z metodą:

```python
.predict(input: NDArray[(Any, 10), float]) -> NDArray[(Any, 1), float]
```

```python
# Example call:

model.predict([[1,2.65,3,4,5,6.124,7,8,9,10], [1,2,67,4,5,7.065,7,1,9,10]])

# Output: array([175.65822, 175.65822], dtype=float32)

```

należy stworzyć dockerowy kontener zawierający API pozwalające na odpytanie modelu.

API powinno obsługiwać 2 metody:

- `GET` na endpointcie `/ping` zwracające jsona `{"ping": "success"}`
- `POST` na endpointcie `/predict` zwracające jsona `{"Result": "<predykcja>"}`

```bash
# przykladowe zapytanie:

curl -X POST <address>:<port> -d '[[1,2.65,3,4,5,6.124,7,8,9,10], [1,2,67,4,5,7.065,7,1,9,10]]`
```

**Ważne:** Załadowany model z pickla potrzebuje biblioteki `xgboost`, dodajcie ją do swoich requirements.txt

---

### Git

Zróbcie sobie na githubie feature brancha zgodnie z [gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). Rozwiązanie dadajcie w folderze zgodnie z taką strukturą:

```
mlops-project
├── 01_containerized_ml_models
│   ├── <folder z waszym rozwiazaniem>
|   |   ├── Dockerfile
|   |   ├── model.pkl
|   |   ├── requirements.txt
|   |   └── api.py
|   |
|
```

## Jeżeli macie jakiegolwiek pytania lub potrzebujecie pomocy w jakiejkowiek części zadania piszcie na discordzie lub do mnie prywatnie, nie ma głupich pytań ;)
