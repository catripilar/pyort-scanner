import socket
from termcolor import colored
S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = input('destinatário:')
pi = input('portas iniciais:');pf = input('portas finais:')
try:
    for port in range(int(pi),int(pf)):
            scan = S.connect_ex((ip,port))
            if scan == 0:print(colored('Porta '+str(port)+' ok.',color='green'))
            else:print(colored('Porta '+str(port)+' em conflito ou não convencional.',color='red'))
    print('fim de curço')
except:print('informações fornecidas em conflito.Tente novamente')     
