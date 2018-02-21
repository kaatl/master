import urllib3
from google import google
num_page = 1
search_results = google.search("Arbeidstilsynet")

from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'https://www.vg.no/nyheter/i/Rxry1d/penger-for-rusbehandling-havnet-paa-kontoen-til-styremedlem'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)
print soup
#print search_results[2].description
