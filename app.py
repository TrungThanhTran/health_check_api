import streamlit as st

import json
import requests
from requests.exceptions import ConnectTimeout

import time
def _call_json_api(api_url, json_data):
        start = time.time()
        try:
            response = requests.post(api_url, json=json_data, timeout=60)
        except ConnectTimeout:
            print('Request has timed out')

        print('time request = ', time.time()-start)
        print(response)
        return response.json()

json_data = {
    "file_name":"health_check_api.mp3"
    }

api_endpoint = st.text_input('api endpoint', 'cap')
button = st.button("send api")
if button:
    if api_endpoint == 'capturia':
        api_url = f"https://{api_endpoint}.io/api/v1/transcribe/file"
        with st.spinner("waiting for proccessing..."):
            response = _call_json_api(api_url, json_data)
            st.write(response)
    else:
        st.warning('please enter api_endpoint')
