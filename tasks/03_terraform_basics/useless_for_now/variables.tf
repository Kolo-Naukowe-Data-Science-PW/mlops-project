variable gcp_zone {
    type = string
    description = "Gcp server"
    default = "europe-central2-a"
}

variable gcp_region {
    type = string
    description = "Gcp server"
    default = "europe-central2"
}

variable  gcp_project {
    type = string
    description = "Project to use"
}

variable  gcp_project_str_for_kubernetes {
    type = string
    description = "Special project to use id for kubernetes"
}

variable gcp_ec2_type {
    type = string
    description = "VM type"
    default = "e2-micro"
}