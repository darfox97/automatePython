import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s - %(message)s')

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    # for i in range(1, n + 1):
    for i in range(n + 1):

        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')

# LOGGING LEVELS:
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
# Currently it shows all the levels because the parameter level in logging.basicConfig is set as DEBUG.

# DISABLING LOGGING:
logging.disable(logging.CRITICAL)  # Deshabilita los logging críticos.
logging.disable()  # It will disable all messages after it,

# LOGGING TO A FILE:
# Añadiendo el parámetro filename en basicConfig, los logging se mostrarán en un archivo en vez de la consola.
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,format='%(asctime)s -  %(levelname)s -  %(message)s')
