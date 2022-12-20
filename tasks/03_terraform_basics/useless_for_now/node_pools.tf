 resource "google_service_account" "kubernetes" {
   account_id = "kubernetes"
 }

 resource "google_container_node_pool" "general" {
   name = "general"
   cluster = google_container_cluster.primary.id
   node_count = 1

   management {
     auto_repair = true
     auto_upgrade = true
   }

   node_config {
     preemptible = false
     machine_type = var.gcp_ec2_type

     labels = {
        role = "general"
     }

     service_account = google_service_account.kubernetes.email
     oauth_scopes = [ "https://www.googleapis.com/auth/cloud-platform" ]

   }
 }
 resource "google_container_node_pool" "spot" {
    name = "spot"
    cluster = google_container_cluster.primary.id

    management {
      auto_repair = true
      auto_upgrade = true
    }

    autoscaling {
      min_node_count = 0
      max_node_count = 6
    }

    node_config {
      preemptible = true
      machine_type = var.gcp_ec2_type
    

      labels = {
          team = "mlops"
      } 

      taint {
          key = "instance_type"
          value = "spot"
          effect = "NO_SCHEDULE"
      }
      service_account = google_service_account.kubernetes.email
      oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
    }
 }
 resource "google_project_iam_member" "allow_image_pull" {
  project = var.gcp_project
  role   = "roles/artifactregistry.reader"
  member = "serviceAccount:${google_service_account.kubernetes.email}"
}
