import socket
import sys

from loguru import logger

ip = '127.0.0.1'
porta = 5000


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	conectar(s)
	consumir(s)

	logger.warning('O Servidor foi encerrado!')
	
	s.close()


def conectar(s):
	try:
		logger.info('Conectando ao ip {} na porta {}'.format(ip, porta))
		s.bind((ip, porta))
	except Exception as e:
	   logger.error('Erro ao conectar com o ip {} na porta {}, {}'.format(ip, porta, e))
	   sys.exit()

	logger.success('Conectado com sucesso!')


def consumir(s):
	while True:
		data, addr = s.recvfrom(1024)
		logger.success('Mensagem recebida de {}, conteúdo: {}'.format(addr, data.decode('utf-8')))


if __name__ == '__main__':
	main()