import socket

def conectar(host,port):
    '''Enviar uma mensagem ao serviço localizado em host:port'''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Conectado!")
    except Exception as E:
        print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    conectar('127.0.0.1', 12000)
