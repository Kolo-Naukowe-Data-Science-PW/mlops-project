resource "google_compute_instance" "vm" {
  name         = "terraform-test-vm"
  machine_type = var.vm_type
  zone         = var.vm_region

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 30
      type  = "pd-standard"
    }
  }

  network_interface {
    network = "default"
  }

}
