import numpy as np 
import pandas as pd
from IPython.display import display, Markdown


#TODO: implementar a escolha do tipo de arquivo no construtor

class DataQuality:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.dataframe = self.carregar_dataset()
        
        
    def carregar_dataset(self):
        if self.dataset.endswith('.csv'):
            return pd.read_csv(self.dataset)
        elif self.dataset.endswith('.xls') or self.dataset.endswith('.xlsx'):
            return pd.read_excel(self.dataset)
        elif self.dataset.endswith('.parquet'):
            return pd.read_parquet(self.dataset)
        elif self.dataset.endswith('.txt'):
            return pd.read_csv(self.dataset)
    
    ###########################################
    
    
    def descricao_geral(self):
        display(Markdown("# Descrição geral do dataset"))
        linhas, colunas = self.dataframe.shape
        
        display("Números de Linhas", linhas)
        display("Números de Colunas", colunas)
    
    def exibir_cabecalho(self):
        display(Markdown("# 5 Primeiras Linhas do Dataset"))
        display(self.dataframe.head())
        
    def exibir_rodape(self):
        display(Markdown("# 5 Linhas finais do Dataset"))
        display(self.dataframe.tail())
        
    
    ###########################################
    def colunas_categoricas(self):
        categoricas = self.dataframe.select_dtypes(exclude='number')
        display(Markdown("# Colunas categóricas do dataset"))
        display(categoricas)
        
    def descricao_categoricas(self):
        for coluna in self.dataframe:
            resumo = self.dataframe[coluna].value_counts().reset_index()
            display(coluna)
            display(resumo)
            display('--------------------------')
    
    def colunas_numericas(self):
        numericas = self.dataframe.select_dtypes(include='number')
        display(Markdown("# Colunas numéricas do dataset"))
        display(numericas)
        
    def descricao_numericas(self):
        display(Markdown("# Detalhamento das colunas  numéricas do dataset"))
        numericas = numericas = self.dataframe.select_dtypes(include='number')
        display(numericas.describe())
    
    def nulos_por_coluna(self):
        
        display(Markdown("# Quantidade de dados nulos ou faltantes."))
        display(self.dataframe.isnull().sum().reset_index())
        
    def dados_duplicados(self):
        display(Markdown("## Dados Duplicados no Dataset"))
        saida = f'{self.dataframe.duplicated().sum()}'
        display(saida)
    
    def valores_unicos(self):
        display(Markdown("## Valores Únicos no Dataset"))
        saida = f'{self.dataframe.nunique().sum()}'
        display(saida)
    
    def show(self): # essa função exibirá o resumo do 
        self.descricao_geral()
        self.exibir_cabecalho()
        self.exibir_rodape()
        self.colunas_categoricas()
        self.colunas_numericas()
        self.nulos_por_coluna()
        self.descricao_numericas()
        self.valores_unicos()
        self.dados_duplicados()
    
    
    def __repr__(self):
        return f"""
#################################
        RESUMO DO DATASET
#################################

    Nº de linhas: {self.dataframe.shape[0]}
    Nº de colunas: {self.dataframe.shape[1]}
    Total valores únicos: {self.dataframe.nunique().sum()}
    Total de valores faltando ou nulos: {self.dataframe.isnull().sum().sum()}
    

"""
    
        
