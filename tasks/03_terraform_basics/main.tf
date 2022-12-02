terraform {
    required_providers {
        google = {
        source = "hashicorp/google"
        version = "3.5.0"
        }
    }
}

variable gcp_zone {
    type = string
    description = "Gcp server"
    default = "europe-central2-a"
}

variable  gcp_project {
    type = string
    description = "Project to use"
    default = "luminous-byway-370313"
}

variable gcp_ec2_type {
    type = string
    description = "VM type"
    default = "e2-micro"
}

provider "google" {
    region = var.gcp_zone
    project = var.gcp_project
}

resource "google_compute_address" "static" {
    name = "address"
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
        my_label = "test"
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

resource "google_compute_firewall" "allow_http" {
    name = "allow-http-rule"
    network = "default"

    allow {
        ports = ["80"]
        protocol = "tcp"
    }

    target_tags = ["allow-http"]

    priority = 1000
}

output "public_ip_address" {
    value = google_compute_address.static.address  
}