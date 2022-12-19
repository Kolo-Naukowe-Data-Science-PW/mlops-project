resource "google_container_cluster" "primary" {
  name               = "mlops-test-k8s"
  location           = var.k8s_region
  initial_node_count = 1
  enable_autopilot   = false
  node_config {
    # preemptible  = true
    machine_type = "e2-micro"
    disk_size_gb = 30
    disk_type = "pd-standard"

  }
}
