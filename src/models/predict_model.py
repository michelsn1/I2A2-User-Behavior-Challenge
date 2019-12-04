import numpy as np
import pandas as pd
import xgboost as xgb
from src.features import main_preprocess

class Predict_label(object):
    """docstring for Predict_label."""

    def __init__(self,raw_data_path,sample_submission_path):
        self.model = xgb.Booster()
        self.model.load_model('./models/basic_XGB_model_1.model')

        self.df_raw = pd.read_csv(raw_data_path)
        self.df_raw['target']=self.df_raw['subject']

        self.df_sample_sub = pd.read_csv(sample_submission_path)


    def create_subject_dataset(self):

        df_subjects = []
        for subject in self.df_raw['subject'].unique():
            df_sub=self.df_raw[self.df_raw['subject']==subject].reset_index()
            df_sub['timestamp']= df_sub['timestamp'] - df_sub.loc[0,'timestamp']
            df_subjects.append(main_preprocess.process_files(df_sub,subject,1,train_notebook=False))

        df_subjects=pd.concat(df_subjects)
        for i in ['direction_of_movement', 'num_points', 'num_critical_points', 'n_from', 'n_to']:
            df_subjects[i]=df_subjects[i].astype(int)

        return df_subjects

    def predict(self,df_subjects):

        predictions={}
        i=0
        for subject in df_subjects.target.unique():
            df_sub = df_subjects[df_subjects['target']==subject].reset_index(drop=True)
            d_matrix =  xgb.DMatrix(data=df_sub.iloc[:,:-1])
            preds = self.model.predict(d_matrix)
            y_pred = np.asarray([np.argmax(line) for line in preds])
            count = np.bincount(y_pred)
            predictions[i]={
                'id' : subject,
                'predictions': y_pred,
                'label': np.argmax(count),
                'count' : count
            }
            i+=1

        df_pred=pd.DataFrame.from_dict(predictions,orient='Index')
        df_final= self.df_sample_sub
        for session in df_pred.id:
            df_final.loc[df_final['id']==session,'label']=df_pred.loc[df_pred['id']==session,'label'].values[0]

        return df_final

    def start(self,output_path='./Submissions/submission.csv'):

        df_subjects=self.create_subject_dataset()
        df_final = self.predict(df_subjects)

        df_final.to_csv(output_path,index=False)
        print('Predições salvas com sucesso em: %s'%output_path)
