resource "google_compute_firewall" "allow_http" {
    name = "allow-http-rule"
    network = "default"

    allow {
        ports = ["80"]
        protocol = "tcp"
    }

    target_tags = ["allow-http"]
    source_tags = ["web"]

    priority = 1000
}

output "public_ip_address" {
    value = google_compute_address.static.address  
}