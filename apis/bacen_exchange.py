import requests

url = r"\"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?%40moeda='USD'&%40dataInicial='05-19-2022'&%40dataFinalCotacao='05-20-2022'&%24format=json\" -H  \"accept: application/json;odata.metadata=minimal\""

payload={}
headers = {
  'Cookie': 'TS01d9825e=0198c2d644685419e8d718bda30bd7fb8ced1bb2ab10bd25f985d165fd4bf845b798f748e95cb371fdd51b29f9024630217f87bfe4; dtCookie=BD0F6C6B9627F42D46BCB6B832C83755|cHRheHwx; JSESSIONID=0000KtB8Ck892N6lC5vp-Wrwdqc:1dof85j5r; TS013694c2=0198c2d644685419e8d718bda30bd7fb8ced1bb2ab10bd25f985d165fd4bf845b798f748e95cb371fdd51b29f9024630217f87bfe4'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
