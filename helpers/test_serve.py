import requests

Endpoint = "http://0.0.0.0:8080"

import helpers.sample_request as sample_request

import pandas as pd

for test in sample_request.tests:
    response = requests.post(Endpoint + "/service", json=test)
    print()
    print("-------------------------------------------------")
    print("Testing " + test["service_name"])
    print("---------------------------------------------")

    try:
        if response.json() != {}:
            print(pd.DataFrame(response.json()))
    except:
        pass
