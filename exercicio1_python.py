def exibir_primeiras_senhas():
        # Abre o arquivo no modo de leitura
    with open('darkweb2017-top100.txt', 'r') as arquivo:
            # Lê todas as linhas do arquivo
        senhas = arquivo.readlines()
            
            # Exibe as 10 primeiras senhas
        for i in range(10):
                print(senhas[i])
                
    

# Chama a função para exibir as senhas
exibir_primeiras_senhas()
