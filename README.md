## MLOps on Google Cloud

We are to create an automated MLOps workflow following all state-of-the-art practices and technologies. What's more, get to know with gitflow and working with cloud resources.

<img src="img/mlops.png">

#### Tools and technologies:

<a href="https://www.python.org/"><img src="img/icons/python.svg" height=30px>**python**</a> &nbsp;&nbsp;&nbsp;
<a href="https://cloud.google.com/"><img src="img/icons/gcp.svg" height=30px>**GCP**</a> &nbsp;&nbsp;&nbsp;
<a href="https://www.kubeflow.org//"><img src="img/icons/kubeflow.svg" height=30px>**kubeflow**</a> &nbsp;&nbsp;&nbsp;
<a href="https://kubernetes.io/"><img src="img/icons/kubernetes.svg" height=30px>**kubernetes**</a> &nbsp;&nbsp;&nbsp;
<a href="https://www.docker.com/"><img src="img/icons/docker.svg" height=30px>**docker**</a> &nbsp;&nbsp;&nbsp;
<a href="https://git-scm.com/"><img src="img/icons/git.svg" height=30px>**git**</a> &nbsp;&nbsp;&nbsp;

### Branch policies

We use gitflow workflow for managing git branches. If you're not familliar with gitflow please follow [this](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) tutorial. Additionally, all PRs are checked by a linting workflow using [flake8](https://flake8.pycqa.org/en/latest/) and [black](https://black.readthedocs.io/en/stable/).

<img src="img/gitflow.svg">

### Workflows

Currently used workflows (github actions):
- `Lint` for code quality checking, automaticallly triggered for PRs
- `Provisioning` for environment provisioning, automatically triggered for pushes to *main* branch
