import requests
import asyncio
import concurrent.futures
import time
from random import randrange
from time import gmtime, strftime

# Todo: add that cool graph thing (Not important)
class HealthCheck:
    def __init__(self, endpoint=None, thread=0, randomize=False):
        self.endpoint=endpoint
        self.request=[]
        self.num_request=thread
        self.randomize=randomize


    @staticmethod
    def __validate_and_convert_url(endpoint):
        if not endpoint.startswith("http://") or not endpoint.startswith("https://"):
            return "https://" + endpoint


    def test_endpoint(self):
        async def per_request(request_loop, executor, endpoint, randomize):
            if randomize:
                await asyncio.sleep(randrange(10))

            start_execute_time = strftime("%H:%M:%S", gmtime())
            start = time.clock()

            response = await request_loop.run_in_executor(executor, requests.get, endpoint)

            request_time = time.clock() - start
            summarize_response = {
                "status_code": response.status_code,
                "executed_time": start_execute_time,
                "response_time": request_time,
                "body": "Not Yet Implemented"
            }

            self.request.append(summarize_response)
            return response

        async def main(endpoint, num_request, randomize):
            with concurrent.futures.ThreadPoolExecutor(max_workers=num_request) as executor:
                inner_loop = asyncio.get_event_loop()
                futures = [
                    per_request(inner_loop, executor, endpoint, randomize)
                    for i in range(num_request)
                ]

                response = await asyncio.gather(*futures)
                return response


        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(self.endpoint, self.num_request, self.randomize))
