import socket
import sys

from loguru import logger


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip, porta = get_info()
    executar(ip, porta, s)

    s.close()
    
    logger.warning('O Client foi encerrado!')


def get_info():
    logger.info('Digite o IP de destino: ')
    ip = input()

    logger.info('Digite a porta de destino: ')
    porta = int(input())

    return ip, porta


def executar(ip, porta, s):
    while True:
        logger.info('Digite a mensagem: ')
        msg = input()

        try:
            s.sendto(bytes(msg, 'utf-8'), (ip, porta))
        except Exception as e:
            logger.error('Erro enviar a mensagem para o ip {} na porta {}, {}'.format(ip, porta, e))
            logger.warning('Encerrando Client...')
            sys.exit()


if __name__ == '__main__':
    main()