from datetime import datetime
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

class Transform:

    def convert_json_format(self, original_json):
        if isinstance(original_json, str):
            original_json = json.loads(original_json)
        transformed_json = {
            "id": original_json["productId"],
            "name": original_json["productName"],
            "description": original_json["productDescription"],
            "pricing": {
                "amount": original_json["price"],
                "currency": original_json["currency"]
            },
            "availability": {
                "quantity": original_json["stockQuantity"],
                "timestamp": datetime.utcnow().isoformat() + "Z"
            },
            "category": original_json["category"]
        }
        return transformed_json
    
    
    def send_to_api(self, message):
        base_url = os.environ.get('URL_API')
        endpoint = os.environ.get('ENDPOINT_API')
        url = f"{base_url}{endpoint}"
        headers = {'Content-Type': 'application/json'}
        message = self.convert_json_format(message)
        try:
            response = requests.post(url, data=json.dumps(message), headers=headers)
            response.raise_for_status()
            print(f"Message sent to API: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to API: {e}")
