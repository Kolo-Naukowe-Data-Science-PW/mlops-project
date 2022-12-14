terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.27.0"
    }
  }

  required_version = ">= 0.14"
}

provider "google" {
    region = var.gcp_zone
    project = var.gcp_project
}

# enables google api if not active
resource "google_project_service" "project" {
  project = var.gcp_project
  service = "iam.googleapis.com"

  timeouts {
    create = "30m"
    update = "40m"
  }

  disable_dependent_services = true
}

module "vm_deployment" {
  source = "../03_terraform_basics/vm_deployment"
  gcp_ec2_type = var.gcp_ec2_type
  gcp_zone = var.gcp_zone
  gcp_region = var.gcp_region
}

module "kubernetes_cluster_deployment" {
  source = "../03_terraform_basics/kubernetes_cluster_deployment"
  gcp_ec2_type = var.gcp_ec2_type
  gcp_region = var.gcp_region
  google_service_account = var.google_service_account
}