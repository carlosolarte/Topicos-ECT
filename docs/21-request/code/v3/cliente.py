import socket
import json

PORT = 12000     
HOST = '127.0.0.1'

    
def receberLista(conn):
    '''Receber a lista de produtos utilizando o socket conn'''
    dados= conn.recv(2048)
    L = json.loads(dados.decode())
    return L

def iniciar(host, port):
    '''Estabelecer a conexão e receber a lista (JSON)'''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Conectado!")
    
            L = receberLista(s)
            print(L)
    
            print('Fim do cliente')
    
    except Exception as E:
        print(f'Erro na conexao...{E}')
    
if __name__ == "__main__":
    iniciar(HOST, PORT)
