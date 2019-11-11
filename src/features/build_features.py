import pandas as pd
import numpy as np

class FeatureExtractor():
    def __init__(self,df_path,mode='train'):
        self.df = pd.read_csv(df_path)
        self.mode = mode
