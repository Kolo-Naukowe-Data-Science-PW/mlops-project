variable gcp_zone {
    type = string
    description = "Gcp server"
    default = "europe-central2-a"
}

variable  gcp_project {
    type = string
    description = "Project to use"
}

variable gcp_ec2_type {
    type = string
    description = "VM type"
    default = "e2-micro"
}

variable "google_service_account" {
    type = string
    description = "IAM_SERVICE_ACCOUNT"
}

variable gcp_region {
    type = string
    description = "Gcp server"
    default = "europe-central2"
}
