resource "google_container_cluster" "primary" {
  name               = "terraform-test-k8s"
  location           = var.gcp_region
  remove_default_node_pool = true
  initial_node_count       = 1
}