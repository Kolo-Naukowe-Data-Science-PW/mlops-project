provider "google" {
  project = var.project
}

module "vm" {
  source    = "../infrastructure/vm"
  vm_region = "us-central1-a"
  vm_type   = "e2-micro"
}

module "k8s" {
  source     = "../infrastructure/k8s"
  k8s_region = "us-central1-a"
}
