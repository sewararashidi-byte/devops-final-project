terraform {
  required_version = ">= 1.0.0"
}

resource "local_file" "project_info" {
  filename = "${path.module}/infrastructure.txt"
  content  = "Terraform created this file to simulate infrastructure for my DevOps final project."
}