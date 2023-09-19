#!/bin/bash
# Upload code to ESP32 via REST API
# Reference: https://docs.circuitpython.org/en/latest/docs/workflows.html#file-rest-api
# **Note:** Requires setting $ESP32_PASS environment variable

# Get device info
curl -v -u :$ESP32_PASS -L 'http://circuitpython.local/cp/version.json' | jq

# List libraries
# curl -v -u :$ESP32_PASS -H "Accept: application/json" -L --location-trusted http://circuitpython.local/fs/lib/ | jq

# Delete existing file(s)
# curl -v -u :$ESP32_PASS -X DELETE -L --location-trusted http://circuitpython.local/fs/code.py

# Upload settings
# curl -v -u :$ESP32_PASS -T settings.toml -L --location-trusted http://circuitpython.local/fs/settings.toml

# Upload new script
curl -v -u :$ESP32_PASS -T main.py -L --location-trusted http://circuitpython.local/fs/main.py