## Deployowanie modeli na Kubernetesie

---

Do eksperymentowania z kubernetesem proponuję używać single-node'owego kubernetesa z docker desktop, są też alternatywy takie jak minikube czy microk8s, ale nie polecam ich na początek. [Tutorial](https://birthday.play-with-docker.com/kubernetes-docker-desktop/ "‌")

Kubernetes ma bardzo dobrą dokumentację, więc też polecam sobie poczytać i używać do rozwiązywania problemów :) [Docs](https://kubernetes.io/docs/home/ "‌")

---

### **Zadanie**

- **Stage 1 (research):**
  Zróbcie porządny research o kubernetesie, poczytajcie, pooglądajcie na yt, co lubicie. Nie nauczycie się kubernetesa po jednym zadaniu, ale fajnie jakbyście dobrze zrozumieli podstawy.
- **Stage 2 (basic deployment):**
  Przygotujcie min. 2 obrazy dockerowe z modelami ML i API oraz manifesty tworzące dla kazdego modelu:
  - deployment z paroma replikami poda z modelem
  - serwisy pozwalające na odpytanie modelu
- **Stage 3 (networking):**
  Przygotujcie dodatkowo manifest tworzący gateway przekierowujący ruch z jednego API to odpowiednich modeli, np.:
  - `<ip>:<port>/predict/<nazwa-modelu>` zwraca predykcję z modelu z danego modelu
  - `<ip>:<port>/ping/<nazwa-modelu>` zwraca healthcheck z danego modelu
    Analogicznie do pierwszego zadania z samym dockerem, wykorzystajcie tamte obrazy.
- **Stage 4 (python)**
  Przygotujcie skrypt pythonowy, który będzie ten deployment wykonywał za was.

Liczę na waszą kreatywność, jeżeli będziecie mieli czas to możecie trochę się pobawić.

---

Umieście swoje rozwiązanie w folderze `mlops-project/tasks/02_kubernetes_fundamentals/kubernetes_<numer taska>` tak, żeby stworzyć taką strukturę repo:

```
mlops-project
├── 01_containerized_ml_models
|   ├── model_api_1
|   |   ├── Dockerfile
|   |   ├── model.pkl
|   |   ├── requirements.txt
|   |   └── api.py
|   ├── model_api_2
|   ├── model_api_3
|   ├── model_api_4
|   ...
|
├── 02_kubernetes_fundamentals
|   ├── kubernetes_1
|   ├── kubernetes_2
|   ├── kubernetes_3
|   ├── kubernetes_4
|   └── kubernetes_5
...
```

---

### Organizacja pracy

To zadanie wykonujecie w grupach, więc dogadajcie się między sobą jak dokładnie będzie to wyglądać. Jednak pracujcie na githubie, możecie pracować na jednym wspólnym branchu lub mieć jednego wspólnego i dodatkowo każdy swojego.

Zaznaczajcie w checkliście poniżej gdzie jesteście :smile:

Jeżeli potrzebujecie pomocy, nie bójcie się pytać albo prosić, powodzenia!
