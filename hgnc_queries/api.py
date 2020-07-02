import json
import sys

import requests

URL = "http://rest.genenames.org"


def get_api_response(full_url):
    """ send request to HGNC and get json response """

    try:
        response = requests.get(
            full_url,
            headers={"Accept": "application/json"}
        )
    except Exception as e:
        print("Something wrong: {}".format(e))
        sys.exit(-1)
    else:
        data = json.loads(response.content.decode("utf-8"))

    return data
