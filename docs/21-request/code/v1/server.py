import socket
HOST = '127.0.0.1'

def iniciar(port):
    '''Inicia un serviço na porta port'''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port)) # Selecionar o endereço e porta
        s.listen() # Escutar solicitações
    
        # accept espera por uma nova conexão
        # Quando um cliente se conectar, accept retorna :
        # - um socket (con) para se comunicar com o cliente
        # - o endereco do cliente
        conn, addr = s.accept()
    
        with conn:
            # Por enquanto o servidor imprime uma mensagem e encerra a conexão
            print(f'Nova conexão com o cliente {addr}')

if __name__ == "__main__":
    iniciar(12000)
