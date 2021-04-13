import socket
import json
from datetime import datetime

PORT = 12000  

# Estado do servidor com todos os clientes que já se conectaram 
users = {'service' : 'Meu serviço de conexões', 
         'inicio'  : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
         'usuarios':[]} 

def adicionarCnx(addr):
    '''Adicionar a nova conexão ao banco de dados'''
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    users['usuarios'].append({'addr' : addr, 'time': now})


def iniciar(port):
    '''Inicializa o servidor. Para toda solicitação, o servidor envia as
    informações de todos os clientes que já utilizaram o serviço. O formato de
    saída é JSON'''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port)) # Selecionar o endereco e porta
        s.listen() # Escutar solicitacoes
        while True:
            try:
                # Aceitar uma conexão
                conn, addr = s.accept()
                print("Novo cliente")
                # Adicionar a nova conexão ao "banco de dados"
                adicionarCnx(addr)
                # Enviar as informações
                with conn:
                    conn.send(str.encode(json.dumps(users)))
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))


if __name__ == "__main__":
    iniciar(12000)
