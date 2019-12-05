import pandas as pd
import numpy as np
import os

class MakeRawDataset():
    def __init__(self):
        self.train_path = os.path.join('./data/raw/training_files')
        self.test_path = os.path.join('./data/raw/test_files')

    def load_dataset(self,main_path,subject,session):
        subject_path =  os.path.join(main_path,subject,session)
        df = pd.read_csv(subject_path,dtype={'timestamp':np.float64})

        df.columns = df.columns.str.replace(' ', '')
        df.rename(columns = {"Unnamed:0" : "index"}, inplace = True)
        df['subject'] = subject.replace('.csv','')

        df = df[['index','subject','timestamp','x','y']]

        df = df[df.timestamp.apply(
                                    lambda x: str(x)[3].isnumeric()
                                    )].reset_index(drop=True)


        df.timestamp = df.timestamp.astype(float)
        df.x = df.x.astype(np.int64)
        df.y = df.y.astype(np.int64)

        df = df.sort_values(by=['timestamp'],ascending=[True]).reset_index(drop=True)
        return df

    def load_subjects(self,path):
        subjects_folders = [f for f in os.listdir(path) if not os.path.isfile(f)]
        return subjects_folders

    def load_sessions(self,path,subject):
        full_path = os.path.join(path,subject)
        sessions_list = [f for f in os.listdir(full_path)]
        return sessions_list

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
            session_list=self.load_sessions(path,subject)
            for session in session_list:
                if df is None:
                    df = self.load_dataset(path,subject,session)
                else:
                    df = df.append(self.load_dataset(path,subject,session))
        if mode =='train':
            df = self.subjects_code(df)
        return df
