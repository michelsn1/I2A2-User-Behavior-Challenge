import pandas as pd
import numpy as np
import os

class MakeRawDataset():
    def __init__(self):
        self.train_path = os.path.join('./data/raw/train_files')
        self.test_path = os.path.join('./data/raw/test_files')

    def load_dataset(self,main_path,subject):
        subject_path =  os.path.join(main_path,subject)
        df = pd.read_csv(subject_path,dtype={'timestamp':np.float64})

        df.columns = df.columns.str.replace(' ', '')
        df.rename(columns = {"Unnamed:0" : "index"}, inplace = True)
        df['subject'] = subject.replace('.csv','')

        df = df[['index','subject','timestamp','x','y']]

        df = df[df.timestamp.apply(
                                    lambda x: str(x)[3].isnumeric()
                                    )].reset_index(drop=True)


        df.timestamp = df.timestamp.astype(float)
        df.x = df.x.astype(np.int32)
        df.y = df.y.astype(np.int32)

        df = df.sort_values(by=['timestamp'],ascending=[True]).reset_index(drop=True)
        return df

    def load_subjects(self,path):
        subjects_folders = [f for f in os.listdir(path)]
        return subjects_folders

    def subjects_code(self,df):

        df['target']=0
        df['target']=np.where(df['subject']=='Subject_4',1,df['target'])
        df['target']=np.where(df['subject']=='Subject_5',2,df['target'])
        df['target']=np.where(df['subject']=='Subject_9',3,df['target'])
        return df



    def create_dataframe(self,mode='train'):
        if mode == 'train':
            path = self.train_path
        elif mode == 'test':
            path = self.test_path
        else:
            print('Plese select a mode for the function, train or test')
            return

        subjects_list = self.load_subjects(path)
        df = None

        for subject in subjects_list:
            if df is None:
                df = self.load_dataset(path,subject)
            else:
                df = df.append(self.load_dataset(path,subject))

        if mode =='train':
            df = self.subjects_code(df)
        return df
