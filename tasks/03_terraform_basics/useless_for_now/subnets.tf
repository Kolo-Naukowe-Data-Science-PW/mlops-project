resource "google_compute_subnetwork" "private" {
    name = "private"
    ip_cidr_range = "10.0.0.0/18"
    region = var.gcp_region
    network = google_compute_network.main.id
    private_ip_google_access = true
    
    secondary_ip_range = [ {
      ip_cidr_range = "10.48.0.0/14",
      range_name = "k8s-pod-range"
    } , {
        ip_cidr_range = "10.52.0.0/20",
        range_name = "k8s-service-range"
    }]
}