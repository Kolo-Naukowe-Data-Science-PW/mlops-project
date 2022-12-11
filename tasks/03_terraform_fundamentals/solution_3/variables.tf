variable "machine_type" {
    default = "f1-micro"
    description = "(Required) The machine type to create."
}
variable "vm_name" {
    default = "vm"
    description = "(Required) A  unique name for the resource, required by GCE. Changing this forces a new resource to be created."
}
# variable "zone" {
#     default = "europe-north1-c"
#     description = "(Optional) The zone that the machine should be created in. If it is not provided, the provider zone is used."
# }
variable "os_image" {
    default = "debian-cloud/debian-11"
    description = "(Optional) The image from which to initialize this disk."
}
variable "project_id" {
    type = string
    description = "(Requiered) Project ID on GCP."
}
variable "credentials_file_name" {
    default = "credentials.json"
    description = "(Required) Name of the credentials file."
}