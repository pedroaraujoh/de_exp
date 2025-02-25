import requests
import polars as pl

# URL da API
url = 'http://localhost:8000/download'  # Substitua pelo endereço correto

# Fazer a solicitação GET para a API
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Ler o conteúdo diretamente no Polars
    df = pl.read_csv(response.content)
    
    # Exibir o DataFrame
    print(df)
else:
    print(f'Erro ao baixar o arquivo: {response.status_code}')