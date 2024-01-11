import os
import fire
from constants import PROJECT_DIR
from logging_config import logger
from scripts import execucao, produto_unidade

def main(input_folder=None):
    if input_folder is None:
        input_folder = os.path.join(PROJECT_DIR, 'datasets/inputs')

    logger.info('----Transformando arquivo Execucao_Painel_QVW_BIINtegrado.')
    execucao(input_folder)

    logger.info('----Transformando arquivo Produto_Unidade_xslx .')
    produto_unidade(input_folder)


if __name__ == '__main__':
  fire.Fire(main)
