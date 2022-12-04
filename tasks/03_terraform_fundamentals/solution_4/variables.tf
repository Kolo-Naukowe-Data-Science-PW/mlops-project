variable "gcp_creadentials" {
  type = string
  description = "Location of service account for GCP"
}

variable "gcp_project_id" {
  type = string
  description = "GCP project id"
}

variable "gcp_region" {
  type = string
  description = "Region of the GCP project"
}

variable "gke_cluster_name" {
  type = string
  description = "Name of a cluster working on GCP"
}

variable "gke_zone" {
  type = list(string)
  description = "List of zones for the project cluster"
}

variable "gke_regional" {
  type = bool
  default = false
  description = "Create regional cluster or no"
}

variable "gke_service_account" {
  type = string
  description = "Name of GKE Service account"
}