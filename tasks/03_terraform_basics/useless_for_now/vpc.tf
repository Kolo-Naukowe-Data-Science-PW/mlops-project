resource "google_project_service" "compute" {
    service = "compute.googleapis.com"  
}

resource "google_project_service" "container" {
    service = "container.googleapis.com"  
}

resource "google_compute_network" "main" {
  name = "main"
  routing_mode = "REGIONAL"
  auto_create_subnetworks = false
  mtu = 1460
  delete_default_routes_on_create = false

  depends_on = [
    google_project_service.compute,
    google_project_service.container
  ]
}