import pytest
import os
import pandas as pd
import numpy as np

@pytest.mark.parametrize(
    'mode, subject', [  ('train','Subject_1'),
                        ('train','Subject_9'),
                        ( 'test', '0b50c151efc1')
                    ]
)
def test_raw_dataset(mode,subject):

    path = './data/raw/'
    if mode == 'train':
        main_df_path = os.path.join(path,'train_data.csv')
        mode_path = os.path.join(path,'train_files')
    elif mode =='test':
        main_df_path = os.path.join(path,'test_data.csv')
        mode_path = os.path.join(path,'test_files')
    subject_path = os.path.join(mode_path,subject+'.csv')


    main_df = pd.read_csv(main_df_path)
    main_df = main_df[(main_df['subject']==subject)].reset_index(drop=True)
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
    original_df.timestamp = original_df.timestamp.astype(float)
    original_df.x = original_df.x.astype(np.int32)
    original_df.y = original_df.y.astype(np.int32)

    return original_df.equals(main_df)



def subject_code_test():
    df = pd.read_csv('./data/raw/train_data.csv')[['subject','target']].drop_duplicates()
    df.columns = [['Subject','Code']]
    df_subject = pd.read_csv('./data/raw/subjects.codes.csv')
    return df.equals(df_subject)

def dataset_tests():
    assert test_raw_dataset()
    assert subject_code_test()

#def same_rows_number(df1,df2):
#    return df1.shape[0]==df2.shape[0]
#
#def duplicated(df,column):
#    duplicateRowsDF = df[df.duplicated([column])]
#    if duplicateRowsDF.shape[0]==0:
#        return True
#    else:
#        print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')
#        return False
#
#def isna_test(df):
#    return not df.isnull().values.any()
