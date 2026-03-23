output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.olek-aks-cluster.name
}

output "aks_resource_group" {
  value = azurerm_resource_group.olek-aks-rg.name
}
output "aks_login_command" {
  description = "Ready cmd to connect to cluster"
  value       = "az aks get-credentials --name ${azurerm_kubernetes_cluster.olek-aks-cluster.name} --resource-group ${azurerm_resource_group.olek-aks-rg.name} --overwrite-existing"
}