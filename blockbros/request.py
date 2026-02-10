import requests
import hashlib
import json
from typing import Dict, Any, Optional

def sortStringify(obj: Dict[str, Any], indent: Optional[int] = None) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

class Internal:
    @staticmethod
    def requestSend(route: str, data: Dict[str, Any], token: str = "", id: int = 0) -> requests.Response:
        """
            Handle sending requests to BlockBros.
        """
        host = "block-bros.appspot.com"
        dataStr = sortStringify(data)
        crc = hashlib.md5(dataStr.encode()).hexdigest()

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