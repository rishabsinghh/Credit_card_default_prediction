from logging import exception
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split

class preprocessor:
    def __init__(self,file_object,logger_object):
        self.file_object=file_object
        self.logger_object=logger_object
    def rename_columns(self,data,column,column_new):
        self.logger_object.log(self.file_object, 'Entered the remove_columns method of the Preprocessor class')
        self.data=data
        self.column=column
        self.column_new=column_new
        try:
            self.data=self.data.rename(columns={column:column_new})
            self.logger_object.log(self.file_object,'Rename_columns successful,Exited the rename columns method of the Preprocessor class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in rename_columns method of the Preprocessor class. Exception message:  '+str(e))
            self.logger_object.log(self.file_object,
                                   'Rename Column Unsuccessful. Exited the rename_columns method of the Preprocessor class')
            raise Exception()

    def remove_columns(self,data,columns):
        self.logger_object.log(self.file_object, 'Entered the remove_columns method of the Preprocessor class')
        self.data=data
        self.columns=columns
        try:
            self.useful_data=self.data.drop(columns,axis=1)
            self.logger_object.log(self.file_object,
                                   'Column removal Successful.Exited the remove_columns method of the Preprocessor class')
            return self.useful_data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in remove_columns method of the Preprocessor class. Exception message:  '+str(e))
            self.logger_object.log(self.file_object,
                                   'Column removal Unsuccessful. Exited the remove_columns method of the Preprocessor class')
            raise Exception()
    def separate_label_feature(self,data,target):
        self.logger_object.log(self.file_object, 'Entered the separate_label_feature method of the Preprocessor class')
        try:
            self.X=data.drop(target,axis=1)
            self.Y=data[target]
            return self.X,self.Y

        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class')
            raise Exception()
    def encodevariables(self,data,columns):
        self.logger_object.log(self.file_object, 'Entered the encode variables method of the Preprocessor class')
        self.data=data
        self.columns=columns
        try:
            for column,prefix in columns.items():
                col=pd.get_dummies(self.data[column],prefix=prefix)
                self.data=pd.concat([self.data,col],axis=1)
            self.logger_object.log(self.file_object,"Encode Variables successful, Exited the Encode Variables Method of the Preprocessor class")
            return self.data
        
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in encode_variables method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'Encode Variables Unsuccessful. Exited the enocode variables method of the Preprocessor class')
            raise Exception()
    def handle_imbalanced_data(self,X,Y):
        rdsmple = RandomOverSampler()
        x_sampled, y_sampled = rdsmple.fit_resample(X, Y)
        return x_sampled,y_sampled
    def scale_data(self,data):
        self.logger_object.log(self.file_object, 'Entered the scale_data method of the Preprocessor class')
        self.data=data
        try:
            sc=StandardScaler()
            self.data=pd.DataFrame(sc.fit_transform(self.data),columns=self.data.columns)
            self.logger_object.log(self.file_object,"Scale_data successful, Exited the Scale Data Method of the Preprocessor class")
            return self.data 
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in scale_data method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'scale_data Unsuccessful. Exited the scale_data method of the Preprocessor class')
            raise Exception()

        
  




        
     