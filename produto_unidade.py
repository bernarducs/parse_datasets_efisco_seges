"""produto_unidade.py

Script que transforma várias planilhas de 
'Produto_Unidade - NOVO.xlsx' em um arquivo CSV.
"""

import os
import pandas as pd

CWD = os.getcwd()
INPUTS = os.path.join(CWD, 'inputs')
OUTPUTS = os.path.join(CWD, 'outputs')
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

# produto unidade
sheets = ['Ant', 'Atual', 'Fut', '2008-2014']

dfs = list()
for sheet in sheets:
    df_ = pd.read_excel(
        f'{INPUTS}/Produto_Unidade - NOVO.xlsx',
        sheet_name=sheet,
        nrows=10
        )
    df_['planilha'] = sheet
    dfs.append(df_)

df = pd.\
        concat(dfs).\
        to_csv(
            f'{OUTPUTS}/produto_unidade.csv', 
            index=False,
            header=False,
            encoding='utf-8'
        )
    