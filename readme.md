# 1. Create service principal

```
az ad sp create-for-rbac --name myServicePrincipalName
```

Save result JSON, use in `local.settings.json`.

# 2. Configure local Azure function

* AZURE_CLIENT_ID: The app (client) id
* AZURE_CLIENT_SECRET: The app password
* AZURE_TENANT_ID: The tenant the AAD app was created in
* AZURE_STORAGE_RESOURCE_NAME: The Azure storage account name
* AZURE_STORAGE_CONTAINER_NAME: Existing container name in storage account - should have at least 1 blob uploaded

# 3. Configure Azure Blob Storage IAM

1. In Azure portal, add service principal as IAM identity with **Storage Blob Data Contributor role**. 

# 4. Run function in local debug

1. Use Postman or cURL for 'http://localhost:7071/api/list
2. Returns JSON as list of blobs in container

    ```json
    ["README.md"]
    ```