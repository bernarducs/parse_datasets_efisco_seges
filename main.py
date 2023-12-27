import os
import fire
import logging
from dotenv import dotenv_values
from scripts import execucao, produto_unidade


def main(file_path='.env'):

    ENV = dotenv_values(os.path.join(file_path, '.env'))
    
    logging.basicConfig(
        filename=os.path.join(ENV['LOG_FOLDER'], 'app_seges.txt'), 
        level=logging.INFO, 
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

    logging.info('----Transformando arquivo Execucao_Painel_QVW_BIINtegrado.')
    execucao(ENV)
    logging.info(f"Arquivo execucao.csv em {ENV['OUTPUT_FOLDER_EXECUCAO']}")

    logging.info('----Transformando arquivo Produto_Unidade_xslx .')
    produto_unidade(ENV)
    logging.info(f"Arquivo execucao.csv em {ENV['OUTPUT_FOLDER_PROD_UNIDADE']}")


if __name__ == '__main__':
  fire.Fire(main)
