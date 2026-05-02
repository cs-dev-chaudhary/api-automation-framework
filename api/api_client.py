import requests
from config.config import Config
from config.logger import get_logger
import jsonschema

logger = get_logger("APIClient")

class APIClient:

    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout  = Config.TIMEOUT
        self.headers  = {"Content-Type":"application/json","X-API-Key":Config.API_KEY}
        logger.info(f"APIClient ready → {self.base_url}")

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url,headers=self.headers,timeout=self.timeout)
        logger.info(f"GET response: {response.status_code}")
        return response
    
    def post(self, endpoint, body):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending POST request to {url}")       
        response = requests.post(url, headers=self.headers, json=body, timeout=self.timeout)
        logger.info(f"POST response: {response.status_code}")
        return response
    
    def put(self, endpoint, body):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending PUT request to {url}")
        response = requests.put(url, headers=self.headers, json=body, timeout=self.timeout)
        logger.info(f"PUT response: {response.status_code}")
        return response
    
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending DELETE request to {url}")
        response = requests.delete(url, headers=self.headers, timeout=self.timeout)
        logger.info(f"DELETE response: {response.status_code}")
        return response 
    
    def validate_schema(self, data, schema):
        try:
            jsonschema.validate(instance=data, schema=schema)
            logger.info("Schema validation PASSED")
        except jsonschema.ValidationError as e:
            logger.error(f"Schema validation FAILED: {e.message}")
            raise AssertionError(f"Schema validation failed: {e.message}")
