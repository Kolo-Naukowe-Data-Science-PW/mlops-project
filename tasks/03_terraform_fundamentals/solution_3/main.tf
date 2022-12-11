provider "google" {
    project = var.project_id
    credentials = "${file(var.credentials_file_name)}"
    region  = "us-west1"
    zone  = "us-west1-c"
}
resource "google_compute_instance" "vm_instance" {
    name = var.vm_name
    machine_type = var.machine_type

    tags = ["dev"]

    boot_disk {
      initialize_params {
        image = var.os_image
      }
    }
    network_interface {
      network = "default"
      access_config {
      }
    }
}