variable "google_service_account" {
    type = string
    description = "IAM_SERVICE_ACCOUNT"
}

variable gcp_region {
    type = string
    description = "Gcp server"
    default = "europe-central2"
}

variable gcp_ec2_type {
    type = string
    description = "VM type"
    default = "e2-micro"
}