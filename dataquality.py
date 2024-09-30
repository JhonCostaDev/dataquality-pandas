import numpy as np 
import pandas as pd


#TODO: implementar a escolha do tipo de arquivo no construtor

class DataQuality:
    def __init__(self, dataset) -> None:
        #self.dataset = pd.read_csv(dataset)
        self.dataset = dataset
        self.dataframe = self.carregar_dataset()
        #self.delimitador = delimitador <-----APLICAR DELIMITADOR
        #self.resumo = self.show()
        #self.categoricas = self.separar_colunas()
        
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
    
    # separar colunas categoricas de colunas numéricas
    
    
    
    ###########################################
    def descricao(self):
        return self.dataframe.describe()
    
    def colunas_categoricas(self):
        categoricas = self.dataframe.select_dtypes(exclude='number')
        return categoricas
    
    def colunas_numericas(self):
        numericas = self.dataframe.select_dtypes(include='number')
        return numericas
    
    def nulos_por_coluna(self):
        return self.dataframe.isnull().sum()
    
    ######
    
    def __repr__(self):
        return f"""
#################################
        RESUMO DO DATASET
#################################

    Nº de linhas: {self.dataframe.shape[0]}
    Nº de colunas: {self.dataframe.shape[1]}
    Total valores únicos: {self.dataframe.nunique().sum()}
    Total de Valores nulos: {self.dataframe.isnull().sum().sum()}
    
#################################
    DADOS NULOS por coluna:
{self.nulos_por_coluna()}


##################################
    RESUMO DAS COLUNAS NUMÉRICAS
{self.colunas_numericas().describe()}
"""
    
    def show(self): # essa função exibirá o resumo do dataset
        pass
        
