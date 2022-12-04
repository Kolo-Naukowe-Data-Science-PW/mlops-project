provider "google" {
  credentials = file(var.gcp_creadentials)
  project = var.gcp_project_id
  region = var.gcp_region
}

data "google_client_config" "default" {
}

data "google_container_cluster" "my_cluster" {
  name = var.gke_cluster_name
}

provider "kubernetes" {
  host  = "https://${data.google_container_cluster.my_cluster.endpoint}"
  token = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(
    data.google_container_cluster.my_cluster.master_auth[0].cluster_ca_certificate,
  )
}