import requests
import asyncio
import concurrent.futures
import time
from time import gmtime, strftime


class HealthCheck:
    def __init__(self):
        self.request = []
        self.num_request = 5

    def test_endpoint(self, endpoint):
        # ToDo: add delay to simulate user coming in
        # ToDo: randomise delay
        async def per_request(loop, executor, endpoint):
            start_execute_time = strftime("%H:%M:%S", gmtime())
            start = time.clock()

            response = await loop.run_in_executor(executor, requests.get, endpoint)

            request_time = time.clock() - start
            summarize_response = {
                "status_code": response.status_code,
                "executed_time": start_execute_time,
                "response_time": request_time,
                "body": "Not Yet Implemented"
            }

            print(summarize_response)

            self.request.append(summarize_response)
            return response

        async def main():
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_request) as executor:
                inner_loop = asyncio.get_event_loop()
                futures = [
                    per_request(inner_loop, executor, endpoint)
                    for i in range(self.num_request)
                ]

                response = await asyncio.gather(*futures)
                return response


        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
