Cześć, to zadanie polega na wytrenowaniu kilkudziesięciu modeli :anguished: Dzięki użyciu **mlflow tracking** będziecie mogli w wygodny sposób zapisać:

- parametry treningów
- metryki modeli
- artefakty z wytrenowanymi modelami

---

### Dataset

Do stworzenia modeli wykorzystajcie zbiór dotyczący samobójstw, który znajdziecie tutaj: [https://www.kaggle.com/datasets/omkargowda/suicide-rates-overview-1985-to-2021](https://www.kaggle.com/datasets/omkargowda/suicide-rates-overview-1985-to-2021 "smartCard-inline")

Co dokładnie wasz model na przywidzieć możecie wybrać sami, może być to np. płeć.

---

### Zadanie

Przygotujcie program napisany w pythonie, który wczyta i przetworzy dane, a następnie wytrenuje 3 różne modele z różnymi hyperparametrami.

Hyperparametry, metryki oraz model otrzymany w każdym treningu zalogujcie używająć mlflow, tak, żeby po wszystkim wyniki były widocznie w UI mlflowa.

Dobór modeli oraz hyperparametrów pozostawiam wam, ale proponuję wykorzystać proste modele, które nie będą trenowały się więcej niż parenaście sekund. W tym zadaniu nie jest dla nas najważniejsza jakość predykcji :wink:

---

### Do sprawdzenia:

- Tracking: [https://mlflow.org/docs/latest/tracking.html](https://mlflow.org/docs/latest/tracking.html "smartCard-inline")
- Logging: [https://mlflow.org/docs/latest/tracking.html#logging-functions](https://mlflow.org/docs/latest/tracking.html#logging-functions "smartCard-inline")
- UI: [https://mlflow.org/docs/latest/tracking.html#tracking-ui](https://mlflow.org/docs/latest/tracking.html#tracking-ui "smartCard-inline")
- [https://towardsdatascience.com/experiment-tracking-with-mlflow-in-10-minutes-f7c2128b8f2c](https://towardsdatascience.com/experiment-tracking-with-mlflow-in-10-minutes-f7c2128b8f2c "‌")

---

**Jeżeli mielibyście większe problemy z którąś częścią lub ogólne pytania to śmiało piszcie do mnie albo na kanale discord!**
