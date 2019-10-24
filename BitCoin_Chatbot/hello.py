import requests

#url = "https://www.naver.com"
#response = requests.post(url, verify=False)
 
#print("status code :", response.status_code)

r = requests.get('https://api.github.com/events')

r = requests.post('https://httpbin.org/post', data = {'key':'value'})

r = requests.put('https://httpbin.org/put', data = {'key':'value'})

r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')

r = requests.options('https://httpbin.org/get')

payload = {'key1':'value1', 'key2':['value2', 'value3']}

r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

r = requests.get('http://api.github.com/events')
r.text

r.encoding
r.encoding = 'ISO-8859-1'