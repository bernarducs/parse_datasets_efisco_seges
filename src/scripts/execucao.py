"""produto_unidade.py

Script que transforma várias planilhas de 
'Produto_Unidade - NOVO.xlsx' em um arquivo CSV.
"""
import os
import pandas as pd
from constants import PROJECT_DIR

def execucao(input_folder):
    
    INPUTS = os.path.join(input_folder, 'Execucao_Painel_QVW_BIINtegrado.csv')
    OUTPUTS = os.path.join(PROJECT_DIR, 'datasets/outputs/execucao.csv')
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
            query('CGD == ["4+5", "3-ODC"]').\
            groupby(GRPBY_COLS, as_index=False)[COLS[-5:]].sum()

    df.\
    rename(
        {old: new for old, new in zip(df.columns, NEW_COLS)},
        axis='columns'
    ).\
    to_csv(
        OUTPUTS,
        sep=';',
        index=False,
        encoding='utf-8',
    )
