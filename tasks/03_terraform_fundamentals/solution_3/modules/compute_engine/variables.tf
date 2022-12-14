variable "machine_type" {
  default     = "f1-micro"
  description = "(Required) The machine type to create."
}
variable "vm_name" {
  default     = "vm"
  description = "(Required) A  unique name for the resource, required by GCE. Changing this forces a new resource to be created."
}
variable "os_image" {
  default     = "debian-cloud/debian-11"
  description = "(Optional) The image from which to initialize this disk."
}