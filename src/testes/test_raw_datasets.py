import pytest
import os
import pandas as pd
import numpy as np
from src.testes import functions

@pytest.mark.parametrize(
    'mode,subject,expected', [('train','Subject_1',True),
                                ('train','Subject_9',True),
                                ('test', '0b50c151efc1',True)]
)
def test_datasets(mode,subject,expected):
    assert functions.test_raw_dataset(mode,subject) == expected
    assert functions.subject_code_test() == True

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
