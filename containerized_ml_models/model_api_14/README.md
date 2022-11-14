To test api.py locally (without using Docker) run:

First terminal:
```
python -m flask --app api run
```

Second terminal:
```
curl -X POST 127.0.0.1:5000/predict -d '[[1,2.65,3,4,5,6.124,7,8,9,10], [1,2,67,4,5,7.065,7,1,9,10]]'
```