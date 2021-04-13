import socket

def iniciar(host,port):
    '''Iniciar conexão, receber uma mensagem e enviar uma mensagem'''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Conectado!")
            #Receber até 1024 bytes do servidor
            msg = s.recv(1024)
            print(f'Mensagem recebida: {msg.decode()}')
            # Enviar uma mensagem ao servidor
            s.send(b'Ola... sou o cliente ')
    
    except Exception as E:
        print(f'Erro na conexão...{E}')
        
if __name__ == "__main__":
    iniciar('127.0.0.1',12000)
