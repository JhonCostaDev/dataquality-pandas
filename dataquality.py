import numpy as np 
import pandas as pd 

#TODO: implementar a escolha do tipo de arquivo no construtor

class DataQuality:
    def __init__(self, dataset) -> None:
        #self.dataset = pd.read_csv(dataset)
        self.dataset = dataset
        self.dataframe = self.carragar_dataset()
        #self.delimitador = delimitador <-----APLICAR DELIMITADOR
        self.resumo = self.show()
        #self.categoricas = self.separar_colunas()
        
    def carragar_dataset(self):
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
    def separar_colunas(self):
        categoricas = self.dataframe.select_dtypes(include=['number']).columns
    
    
    ###########################################
    def descricao(self):
        return self.dataframe.describe()
    
    def colunas(self):
        return self.dataframe.index()
    
    def dados_faltantes(self):
        return self.dataframe.isnull().sum()
    
    ######
    
    def __repr__(self):
        return f"""
    {self.descricao()}
    """
    
    def show(self): # essa função exibirá o resumo do dataset
        #pass
        self.descricao()
   