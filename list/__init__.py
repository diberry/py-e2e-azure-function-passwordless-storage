import logging
import os, uuid
import json
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:

        storage_account_name = os.environ['AZURE_STORAGE_RESOURCE_NAME']
        container_name = os.environ['AZURE_STORAGE_CONTAINER_NAME']

        logging.info(storage_account_name)
        logging.info(container_name)

        account_url = f"https://{storage_account_name}.blob.core.windows.net"

        # Local development: credential created from environment variables in local.settings.json
        # Cloud runtime: credential is retrieved from the environment
        default_credential = DefaultAzureCredential()

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=default_credential)

        # list blobs in the container
        container_client = blob_service_client.get_container_client(container_name)
        blob_list = container_client.list_blobs()

        # array to hold the blob names
        blob_names = []

        for blob in blob_list:
            blob_names.append(blob.name)
            logging.info(blob.name)

        return func.HttpResponse(
            json.dumps(blob_names),
            status_code=200
        )
    except Exception as e:
        logging.info(e)

        return func.HttpResponse(
                f"!! This HTTP triggered function executed unsuccessfully. \n\t {e} ",
                status_code=500
        )
