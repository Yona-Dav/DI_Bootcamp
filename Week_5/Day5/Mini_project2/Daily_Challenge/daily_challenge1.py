import time
import requests

def time_to_load(url):
    start_time = time.time()
    response = requests.get(url)
    stop_time = time.time()
    print(f'The amount of time it takes a webpage to load is {stop_time - start_time} seconds')


time_to_load('https://developers.google.com/youtube/iframe_api_reference')

