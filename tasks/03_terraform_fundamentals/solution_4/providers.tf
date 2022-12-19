provider "google" {
  project = var.gcp_project_id
  region  = "europe-central2"
  zone    = "europe-central2-a"
  credentials = file(var.gcp_credentials)
}
