resource "google_compute_address" "static" {
    name = "address"
    region = var.gcp_region
}

resource "google_compute_instance" "default" {
    name = "test"
    machine_type = var.gcp_ec2_type
    zone = var.gcp_zone
    tags = ["allow-http"]

    boot_disk {
    initialize_params {
        image = "windows-server-2019-dc-core-for-containers-v20200609"
        labels = {
        my_label = "test-1"
            }
        }
    }

    network_interface {
      network = "default"

      access_config {
        nat_ip = google_compute_address.static.address
      }
    }
}