Property Service for Sky Server

1. Install Sky  with `pip install "skypilot-nightly[aws]"`

2. setup your aws command line

3. run `sky check`

4. run `sky serve up property_service.yaml`
This will take about 10 minutes to deploy  it can be monitored through the controllers logs.
e.g. `sky serve logs sky-service-0af4  --controller`

5. in the `test_serve.py` in the root folder, change the End_point variable to the endpoint given by skyserve and run it to test success.
