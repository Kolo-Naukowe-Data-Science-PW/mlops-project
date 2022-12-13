provider "google" {
    project = var.project_id
    credentials = "${file(var.credentials_file_name)}"
    region  = "us-west1"
    zone  = "us-west1-c"
}

module "compute_engine" {
    source = "./modules/compute_engine"
}

module "k8s_cluster" {
    source = "./modules/k8s_cluster"
    service_account = var.service_account
}