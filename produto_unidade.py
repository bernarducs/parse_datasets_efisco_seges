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

INPUTS = os.path.join(
    ENV['INPUT_FOLDER_PROD_UNIDADE'], 
    'Produto_Unidade - NOVO.xlsx'
)
OUTPUTS = os.path.join(
    ENV['OUTPUT_FOLDER_PROD_UNIDADE'], 
    'produto_unidade.csv'
)
NEW_COLUMNS = [
    'exercicio',
	'oe_codigo',
	'oe_nome',
	'orgao_codigo',
	'orgao_nome',
	'uo_codigo',
	'uo_sigla',
	'uo_tpo_adm',
	'uo_esfera_orcamentária',
	'funcao_codigo',
	'funcao_nome',
	'subfuncao_codigo',
	'subfuncao_nome',
	'programa_codigo',
	'programa_nome',
	'programa_tipo',
	'programa_objetivo',
	'acao_codigo',
	'acao_nome',
	'acao_tipo',
	'acao_finalidade',
	'subacao_codigo',
	'subacao_nome',
	'subacao_prioridade',
	'subacao_situacao',
	'produto_nome',
	'unidade_nome',
	'tipo_localizacao',
	'localizacao',
	'meta_1o_ano',
	'meta_2o_ano',
	'meta_3o_ano',
	'meta_4o_ano',
	'programa_tipo_alteracao',
	'programa_justificativa_alteracao',
	'acao_tipo_alteracao',
	'acao_justificativa_alteracao',
	'subacao_tipo_alteracao',
	'subacao_justificativa_alteracao',
	'conservacao_patrimonial',
	'cod_ibge_mun'
]
DELETE_COLS = [
    'subfuncao_codigo',
	'subfuncao_nome',
	'meta_1o_ano',
	'meta_2o_ano',
	'meta_3o_ano',
	'meta_4o_ano',
	'programa_tipo_alteracao',
	'programa_justificativa_alteracao',
	'acao_tipo_alteracao',
	'acao_justificativa_alteracao',
	'subacao_tipo_alteracao',
	'subacao_justificativa_alteracao',
	'produto_nome',
	'unidade_nome',
	'tipo_localizacao'
]

logging.info('----Transformando arquivo Produto_Unidade_xslx .')

# produto unidade
sheets = ['Ant', 'Atual', 'Fut', '2008-2014']

dfs = list()
for sheet in sheets:
    df_ = pd.read_excel(
        INPUTS,
        sheet_name=sheet,
        # nrows=1000
        )
    df_.columns = NEW_COLUMNS
    df_['planilha'] = sheet
    dfs.append(df_)

pd.\
	concat(dfs).\
	query('exercicio > 2010').\
	drop(DELETE_COLS, axis=1).\
    drop_duplicates().\
	to_csv(
		OUTPUTS, 
		index=False,
		sep=';',
		encoding='utf-8'
	)

logging.info(
    f"Arquivo produto_unidade.csv em {ENV['OUTPUT_FOLDER_PROD_UNIDADE']}"
)
