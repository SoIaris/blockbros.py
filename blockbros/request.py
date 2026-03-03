import requests
import hashlib
import json

from typing import Dict, Any, Optional

def sortStringify(obj, indent=None):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def getCRC(table: str, token: str):
    string = table
    if token != "":
        string += token

    crc = hashlib.md5((string).encode()).hexdigest()
    return crc
    
class Internal:
    @staticmethod
    def requestSend(route: str, data: Dict[str, Any], token: str = "", id: int = 0) -> requests.Response:
        """
            Handles sending requests to BlockBros.

            args:
                route (str): example: "gamer/follow/put"
                data: (dict): data should be the json data
                token: (Optional) (str): the account token you get when you login
                id: (Optional) (int): the long id. Example: (6529423364063232)
        """
        host = "block-bros.appspot.com"
        dataStr = sortStringify(data)
        crc = getCRC(dataStr, token)
        
        try:
            response = requests.post(
                f"https://{host}/{route}", 
                headers={
                    'Device-Language': 'en',
                    'CRC': crc,
                    'Authorization': f'{id}:{token}',
                    'Device-Platform': 'ios',
                    'Client-Version': '5',
                    'Master-Version': '537',
                    'Accept': 'application/json',
                    'Accept-Encoding': 'gzip, deflate',
                    'User-Agent': 'gzip',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json;charset=UTF-8',
                }, 
                data=dataStr
            )
            
            return response
        except Exception as e:
            print(f"Unexpected error while sending request: {e}")
            raise

if __name__ == "__main__": # testing 
    send = Internal.requestSend("auth/alt_login", {
        "gamer_id": "10",
        "password": "realpassword" 
    })
    print(send.text)