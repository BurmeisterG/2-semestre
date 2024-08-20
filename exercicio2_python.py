import requests

def testar_subdominios(url_base):
    
        # Abre o arquivo de subdomínios que eu baixei e deixi na mesma pasta, no modo de leitura ("r")
        with open('subdomains-top1million-5000.txt', 'r') as arquivo:
            subdominios = arquivo.readlines()
            
            # Fazendo um "range" para pegar somente os 20 primeiros subdominios do arquivo
            for i in range(20):
                subdominio = subdominios[i].strip()
                
                # Forma a URL completa
                url_completa = f"http://{subdominio}.{url_base}"
                
                try:
                    # Faz a requisição GET
                    response = requests.get(url_completa)
                    
                    # Exibe o status code da resposta
                    print(f"Subdomínio: {subdominio}.{url_base} - Status Code: {response.status_code}")
                
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao conectar com {subdominio}.{url_base}: {e}")
    


# Exemplo de chamada da função
testar_subdominios('example.com')

