import pytest
import os
import pandas as pd


def test_raw_dataset_train():

    subject = 'Subject_1'
    session = 'session_3320405034'

    main_path = os.path.join('./data/raw')
    subject_path = os.path.join(main_path+'/training_files',subject)

    main_df_train = pd.read_csv(os.path.join(main_path,'train_data.csv'))
    main_df_train = main_df_train[(main_df_train['subject']==subject) &
                                (main_df_train['session']==session)].reset_index()
    main_df_train = main_df_train.drop(['subject','session'],axis=1)


    aux_df_train = pd.read_csv(os.path.join(subject_path,session))

    return aux_df_train.equals(main_df_train)

def test_raw_testdataset():

    subject = 'Subject_1'
    session = 's_4ad65a2d0d2d'

    main_path = os.path.join('./data/raw')
    subject_path = os.path.join(main_path+'/test_files',subject)

    main_df_test = pd.read_csv(os.path.join(main_path,'train_data.csv'))
    main_df_test = main_df_test[(main_df_test['subject']==subject) &
                                (main_df_test['session']==session)].reset_index()
    main_df_test = main_df_test.drop(['subject','session'],axis=1)


    aux_df_test = pd.read_csv(os.path.join(subject_path,session))

    return aux_df_test.equals(main_df_test)

def dataset_tests():
    assert test_raw_dataset_test()
    assert test_raw_dataset_train()

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
