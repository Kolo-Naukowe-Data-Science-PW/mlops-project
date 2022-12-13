variable "location" {
  default = "us-central1-a"
  description = "(Optional) Location of the cluster."
}
variable "name" {
  default = "my-gke-cluster"
  description = "(Optional) Name of the cluster."
  type = string
}
variable "name_node_pool" {
  default = "my-node-pool"
  description = "(Optional) Name of the node pool."
  type = string
} 
variable "display_name" {
  default = "Tempdisplayname"
  description = "(Required) The display name for the service account. Can be updated without creating a new resource.."
}
