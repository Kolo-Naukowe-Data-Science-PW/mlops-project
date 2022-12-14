variable "client_email" {}

resource "google_container_cluster" "primary" {
  name     = var.name
  location = var.location

  remove_default_node_pool = true
  initial_node_count       = 1
}
resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-node-pool"
  location   = var.location
  cluster    = google_container_cluster.primary.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "e2-medium"

    service_account = var.client_email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}