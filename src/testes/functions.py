import os
import pandas as pd
import numpy as np

def test_raw_dataset(modo,subject):

    path = './data/raw/'
    if modo == 'train':
        main_df_path = os.path.join(path,'train_data.csv')
        modo_path = os.path.join(path,'train_files')
    elif modo =='test':
        main_df_path = os.path.join(path,'test_data.csv')
        modo_path = os.path.join(path,'test_files')
    subject_path = os.path.join(modo_path,subject+'.csv')


    main_df = pd.read_csv(main_df_path)
    main_df = main_df[(main_df['subject']==subject)].reset_index(drop=True)
    if modo =='train':
        main_df = main_df.drop(['subject','target'],axis=1)
    elif modo == 'test':
        main_df = main_df.drop(['subject'],axis=1)
    main_df = main_df.sort_values(by=['index'],
                                        ascending=[True]
                                        ).reset_index(drop=True)

    original_df = pd.read_csv(subject_path)
    original_df.columns = original_df.columns.str.replace(' ', '')
    original_df.rename(columns = {"Unnamed:0" : "index"}, inplace = True)
    original_df=original_df[original_df.timestamp.apply(
                    lambda x: str(x)[3].isnumeric())].reset_index(drop=True
                    )
    original_df.timestamp = original_df.timestamp.astype(np.float64)
    original_df.x = original_df.x.astype(np.int64)
    original_df.y = original_df.y.astype(np.int64)

    original_df.timestamp = original_df.timestamp.round(4)
    main_df.timestamp = main_df.timestamp.round(4)

    return np.array_equal(original_df.values,main_df.values)


def subject_code_test():
    df = pd.read_csv('./data/raw/train_data.csv')[['subject','target']].drop_duplicates()
    df = df.sort_values(by='target',ascending=True).reset_index(drop=True)
    df.columns = [['Subject','Code']]

    df_subject = pd.read_csv('./data/raw/subjects_codes.csv',delimiter=';')

    return np.array_equal(df.values,df_subject.values)
