"""produto_unidade.py

Script que transforma várias planilhas de 
'Produto_Unidade - NOVO.xlsx' em um arquivo CSV.
"""

import os
import logging
import pandas as pd
from dotenv import dotenv_values


ENV = dotenv_values('.env')

logging.basicConfig(
    filename=os.path.join(ENV['LOG_FOLDER'], 'app_seges.txt'), 
    level=logging.INFO, 
    format='%(asctime)s:%(levelname)s:%(message)s'
)

logging.info('----Transformando arquivo Execucao_Painel_QVW_BIINtegrado.')

INPUTS = os.path.join(
    ENV['INPUT_FOLDER_EXECUCAO'], 
    'Execucao_Painel_QVW_BIINtegrado.csv'
)
OUTPUTS = os.path.join(
    ENV['OUTPUT_FOLDER_EXECUCAO'], 
    'execucao.csv'
)
COLS = [
    'ANO',
    'MÊS',
    'UO_COD',
    'FUNÇÃO_COD',
    'AÇÃO_COD',
    'SUBAÇÃO_COD',
    'FNT',
    'GD',
    'CGD',
    'FONTE_FLUXO',
    'CGF2',
    'MÊS2',
    'CHAVEPAS',
    'Valor_Liquidado',
    'Valor_Pago_SRestos',
    'Valor_Empenhado',
    'Valor_Prog_Financeira',
    'Valor_Dotação_Autorizada'
]
GRPBY_COLS = [
    'ANO',
    'MÊS',
    'UO_COD',
    'FUNÇÃO_COD',
    'AÇÃO_COD',
    'SUBAÇÃO_COD',
    'FNT',
    'GD',
    'CGD',
    'FONTE_FLUXO',
    'CGF2',
    'MÊS2',
    'CHAVEPAS',
]
NEW_COLS = [
    'ANO',
    'MES',
    'UO_COD',
    'FUNCAO_COD',
    'ACAO_COD',
    'SUBACAO_COD',
    'FNT',
    'GD',
    'CGD',
    'FONTE_FLUXO',
    'CGF2',
    'MES2',
    'CHAVEPAS',
    'Valor_Liquidado',
    'Valor_Pago_SRestos',
    'Valor_Empenhado',
    'Valor_Prog_Financeira',
    'Valor_Dotacao_Autorizada'
]

df = pd.\
        read_csv(INPUTS, sep=';', decimal=',', usecols=COLS).\
        query('CGD == ["4+5", "3-ODC"]')

df.columns = NEW_COLS
df.to_csv(
    OUTPUTS,
    sep=';',
    index=False,
    encoding='utf-8',
)

logging.info(f"Arquivo execucao.csv em {ENV['OUTPUT_FOLDER']}")
