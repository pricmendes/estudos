print("\n*-*-*-*-* Exemplo de importação de módulos de terceiros: *-*-*-*-*\n")

# é necessário instalar via pip - será utilizado a biblioteca requests para este exemplo 

import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retorno o status {response.status_code}\n")
