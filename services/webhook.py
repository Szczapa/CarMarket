import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.getenv("WEBHOOK_URL")
if webhook_url is None:
    raise ValueError("L'url du webhook est introuvable")


class WebhookManager:
    @staticmethod
    def productWebhook(data):
        information = [
            {
                "color": "11206535",
                "title": "Demande commande de Produit",
                "fields": [
                    {"name": "Nom du produit :", "value": data["name"], "inline": False},
                    # {"name": "Client :", "value": "value", "inline": False},
                    {"name": "Prix :", "value": data["price"], "inline": False},
                ],
                "footer": {
                    "text": datetime.now().strftime("%d/%m/%Y [%X]")
                }
            }
        ]

        data = {
            "embeds": information
        }

        # Headers
        headers = {
            'Content-Type': 'application/json'
        }

        # Performing the POST request
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        if response.status_code != 204:
            raise ValueError(
                f"Request to Discord returned an error {response.status_code}, the response is:\n{response.text}")
        return response.status_code

