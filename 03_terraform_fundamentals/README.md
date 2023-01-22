### Cześć, kolejne zadanie dotyczące terraforma i tworzenia infrastruktury chmurowej 😀

---

### Google Cloud

Do tego zadania proponuję, żebyście założyli sobie konta na GCP. Każdy nowy użytkownik dostaje na start $300, więc nie trzeba wydawać ani grosza, żeby pouczyć się pracy z chmurą. Żeby przetestować czy wasz kod działa (tworzy zasoby) wystarczy postawienie infrastruktury na pare sekund/minut, więc $300 może wam starczyć nawet na pare miesięcy zabawy. **Pilnujcie tylko, żeby nie zostawiać włączych VMek, klastrów itp na pare dni, bo wtedy skurczy wam się budżet ://**

Jeżeli nigdy nie używaliście GCP albo innych chmur to najpierw zróbcie research na ten temat.

---

### Zadanie

Tak jak ostatnio powiedziełem zadanie na stage. Zróbcie tyle ile będziecie chcieli i mogli. W checkliscie zaznaczajcie jak wam idzie ✅

- **Stage 1 (research)**
Poczytajcie, pooglądajcie albo popytajcie na temat terraforma tak, żebyscie oswoili się z narzędziem i zrozumieli dlaczego się z tego korzysta i jak.

- **Stage 2 (simple definition)**
Spróbujcie stworzyć definicję terraforma, która stworzy wam na GCP jedna maszyne wirtualną (wybierzcie najtańszą możliwą 😉). Na tym etapie wystarczy wam jeden plik `main.tf`. Oswójcie się z poleceniami `terraform init`, `terraform plan`, `terraform apply`, ... deployując definicję VMki na GCP.

- **Stage 3 (variables)**
Zparametryzujcie definicję ze *stage 2* dodając zmienne i plik `variables.tf`.

- **Stage 4 (modules)**
Spróbujcie podzielić waszą definicję na terraformowe moduły. Możecie zdeployować też klaster kubernetesa, żeby mieć 2 moduły (VMs, k8s).

- **Stage 5 (pipeline)**
Wywoływanie komend terraforma możemy automatyzować tworząc pipeline'y. Spróbujcie przygotować pipeline na githuba (github workflows), który będzie deployował definicję przychowywaną w repo.

---

### Github

Pliki ze swoim rozwiązaniem dodajcie w folderze 
`03_terraform_fundamentals/solution_<number w tasku na trello>`

Tak jak zawsze polecam używać gita i naszego repo podczas pracy, zwłaszcza w zespole.

---

**Zachęcam, żebyście pytali albo prosili o pomoc mnie (@matined) lub inne osoby z projektu, jeżeli macie problem, którego nie potraficie rozwiązać!**
