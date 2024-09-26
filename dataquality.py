import numpy as np 
import pandas as pd 

#TODO: implementar a escolha do tipo de arquivo no construtor

class DataQuality:
    def __init__(self, dataset) -> None:
        self.dataset = pd.read_csv(dataset)
        
    def __repr__(self):
        return f"""{self.dataset.info()}"""
    
    def descricao(self):
        return self.dataset.describe()
    def colunas(self):
        return self.dataset.index()
    
    def dados_faltantes(self):
        return self.dataset.isnull().sum()
   