import requests
import uuid
import time
import json

api_url = 'https://2db3c4f0f443425e91076e90310bc461.apigw.ntruss.com/custom/v1/13111/71345557e5b12d3b42ffdbf516755f0c9c7f7c3bc51dd5cea5d888581fc4d9a7/infer'
secret_key = 'S3RtbGdXWUtDc0xlYW1ybGFrTGhEanlMWHdpbmRCTHM='

image_file = 'input.png'
output_file = 'output.json'

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo',
            'templateIds': [12333]
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}
payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

res = json.loads(response.text.encode('utf8'))
print(res)

with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(res, outfile, indent=4, ensure_ascii=False)
    
#########    
company = res['images'][0]['title']['inferText']
name = res['images'][0]['fields'][0]['inferText']
product = res['images'][0]['fields'][1]['inferText']
######

print('company : ',company)
print('name : ',name)
print('product : ',product)
