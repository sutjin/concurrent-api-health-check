import argparse

from healthcheck import HealthCheck

def usage():
    return """
        python run_health_check <url>
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="The URL to trigger", required=True)

    args = parser.parse_args()

    healthCheck = HealthCheck()

    healthCheck.test_endpoint(args.url)

