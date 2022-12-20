resource "google_compute_router" "router" {
  name = "router"
  region = var.gcp_region
  network = google_compute_network.main.id
}