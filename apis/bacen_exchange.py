import requests

url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='05-24-2022'&$format=json"

payload={}
headers = {
  'accept': 'application/json;odata.metadata=minimal',
  'Cookie': 'TS01d9825e=0198c2d64430855160404b690b35fb7fe1bb31317d1763e8ea9dadeafcc75e5e4eb8e46e80da91e38394ceeb1750446fc8da49f95c; dtCookie=78505100B138008A1CA7E84F550FE09A|cHRheHwx; BIGipServer~was-p_as3~was-p~pool_was-p_default_443=1020268972.47873.0000; JSESSIONID=0000aOA3oxjjUMisw1f8mnJuz9D:1cn7jtfnj; TS013694c2=0198c2d64430855160404b690b35fb7fe1bb31317d1763e8ea9dadeafcc75e5e4eb8e46e80da91e38394ceeb1750446fc8da49f95c'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
