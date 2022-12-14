provider "google" {
  project = var.gcp_project
  region = var.gcp_zone
}

terraform {
  backend "gcs" {
    bucket = "tf-first-version"
    prefix = "terraform/state"
  }
}