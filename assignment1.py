print("Write a Python 3 program that uses the Requests module to make the following HTTP requests: \n")

import requests

print("A: A Google search for the "'"term Tim Berners-Lee"'" \n")

getResponce = requests.get("https://google.com/search?q=tim+berners-lee");
print("\t")
print("The content (body) of the response:  \n" + str(getResponce.content))
print("\t")
print("The status code of the response:  \n" + str(getResponce))
print("\t")
print("The response headers:  \n" + str(getResponce.headers))
print("\t")

print("B: A POST request to a website that does not accept POST requests. \n")
print("\t")
url = 'https://stackoverflow.com/questions/'
myobj = {'key': 'value'}
getPostResponce = requests.post(url, json = myobj)
print("\t")
print("The content (body) of the response:  \n" + str(getPostResponce.content))
print("\t")
print("The status code of the response:  \n" + str(getPostResponce))
print("\t")
print("The response headers:  \n" + str(getPostResponce.headers))
print("\t")

print("C: A request to a URL that does not exist.\n")

try:
    getInvalidResponce = requests.get("http://fake-goof.com");
except requests.exceptions.RequestException as error:
    print("Handel Exception:  \n" + str(error))

print("\t")

print("Can you find two requests with extremely different roundtrip times? .\n")

response = requests.get("https://finance.yahoo.com/")
print("Responce time in taken to load yahoo finance website %s in seconds" %(str(response.elapsed.total_seconds())))

response = requests.get("https://protrader.com.au")
print("Responce time in taken to load pro trader finance website %s in seconds \n" %(str(response.elapsed.total_seconds())))

print("Lastly, what does the timing imply for systems that scrape the web?")

print("There might be long running process and would eventualy get into dead lock; So we might have to plan consider multithreading scalling up the resources.\n")

