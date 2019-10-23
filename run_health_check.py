import argparse

from healthcheck import HealthCheck

def usage():
    return """
        python run_health_check <url>
    """

def print_result_to_console(request):
    for i, val in enumerate(request):
        print("""
    ================================

    "status_code": {},
    "executed_time": {},
    "response_time": {},
    "body": "Not Yet Implemented"

    ================================
            """.format(val.get("status_code"), val.get("executed_time"), val.get("response_time")))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="The URL to trigger", required=True)
    parser.add_argument("-t", "--thread", type=int, help="Amount of concurrent Thread", default=5)
    parser.add_argument("-r", "--randomize", help="add random delay to call", default=False)

    args = parser.parse_args()

    healthCheck = HealthCheck(
                    endpoint=args.url,
                    thread=args.thread,
                    randomize=args.randomize)

    healthCheck.test_endpoint()
    print_result_to_console(healthCheck.request)

    # ToDo: output objects a JSON file else print on console

