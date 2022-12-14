resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "test-node-pool"
  location   = var.gcp_region
  cluster    = google_container_cluster.primary.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = var.gcp_ec2_type
  }
}