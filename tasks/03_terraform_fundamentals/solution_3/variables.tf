variable "project_id" {
    type = string
    description = "(Requiered) Project ID on GCP."
}
variable "credentials_file_name" {
    default = "credentials.json"
    description = "(Required) Name of the credentials file."
}
variable "service_account" {
  description = "(Required)) The email to the service account to be used by the Node VMs."
}