import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

multipart_data = MultipartEncoder(
    fields = {
        'json' : '123123123',
        'file' : ('frame.jpg', open('test.jpg', 'rb'), 'text/plain')
    }
)

response = requests.post('http://212.19.138.141/ksk/upload.php', data=multipart_data, headers={'Content-Type': multipart_data.content_type})
f = open('output.txt', 'w')
f.write(response.content.decode('utf-8'))
f.close()