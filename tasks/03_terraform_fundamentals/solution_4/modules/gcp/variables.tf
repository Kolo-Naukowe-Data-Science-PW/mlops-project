variable "gcp_machine_type" {
  type = string
  description = "Name of the VM to create"
  default = "e2-micro"
}

variable "vm_instance_name" {
  type = string
  description = "Name of the VM instance"
  default = "mlops-test"
}
