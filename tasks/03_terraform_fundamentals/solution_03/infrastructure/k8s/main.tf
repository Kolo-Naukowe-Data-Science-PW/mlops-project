
resource "google_container_cluster" "primary" {
  name               = "terraform-test-k8s"
  location           = var.k8s_region
  initial_node_count = 1
  enable_autopilot   = false
}
