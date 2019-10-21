import pandas as pd
import numpy as np
import os

class MakeRawDataset():
    def __init__(self):
        self.train_path = os.path.join('./data/raw/training_files')
        self.test_path = os.path.join('./data/raw/test_files')

    def load_dataset(self,main_path,subject,session):
        subject_path =  os.path.join(main_path,subject)
        session_path =  os.path.join(subject_path,session)
        df = pd.read_csv(session_path)
        columns = list(df.columns.values)
        df['subject'] = subject
        df['session'] = session
        df = df[['subject', 'session']+columns]
        return df

    def load_subjects(self,path):
        subjects_folders = [f for f in os.listdir(path)]

        return subjects_folders

    def load_sessions(self,subject,folder_path):
        sessions_path = [f for f in os.listdir(os.path.join(folder_path,subject))]

        return sessions_path

    def create_dataframe(self,mode='train'):
        if mode == 'train':
            path = self.train_path
        elif mode == 'test':
            path = self.test_path
        else:
            print('Plese select a mode for the function, train or test')
            return
        subjects_list = self.load_subjects(path)
        self.df = None
        for subject in subjects_list:
            sessions_list = self.load_sessions(subject,path)
            for session in sessions_list:
                if self.df is None:
                    df = self.load_dataset(path,subject,session)
                else:
                    df = df.append(self.load_dataset(path,subject,session))
        return df
