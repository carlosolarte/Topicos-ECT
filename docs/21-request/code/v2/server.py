import socket

HOST = '127.0.0.1'  

def iniciar(port):
    '''Aceitar um cliente, enviar e receber uma mensagem '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port)) # Selecionar o endereço
        s.listen() # Escutar solicitações
    
        conn, addr = s.accept()
        try:
            with conn:
                #Note o uso do b na string (strings binarias)
                conn.send(b'Oi, sou o servidor')
    
                #recebe até 1024 bytes do cliente
                msg = conn.recv(1024)
                # Decode: converte uma string binaria para uma string ASCII
                print(f'Mensagem recebida: {msg.decode()}')
    
                print('Fim do servidor ')
        except Exception as E:
            print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    iniciar(12000)
