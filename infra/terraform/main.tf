terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
    }
  }
}
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}
resource "azurerm_resource_group" "olek-aks-rg" {
  name     = "olek-aks-rg"
  location = "North Europe" 
}

resource "azurerm_kubernetes_cluster" "olek-aks-cluster" {
  name                = "olek-aks-cluster"
  location            = azurerm_resource_group.olek-aks-rg.location
  resource_group_name = azurerm_resource_group.olek-aks-rg.name
  dns_prefix          = "olek-aks-cluster"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_B2s" 
    
    
    auto_scaling_enabled = true
    min_count           = 2
    max_count           = 3
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Dev"
  }
}