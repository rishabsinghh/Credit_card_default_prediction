import pandas as pd
from file_operations import file_methods
from preprocessing.preprocessing import preprocessor
from app_logger import logger
import pickle


class prediction:
    def __init__(self):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.log_writer = logger.application_logger()
    def predictionFromModel(self,data):
        try:
            self.log_writer.log(self.file_object,'Start of Prediction')
            self.preprocessor=preprocessor(self.file_object,self.log_writer)
            data=self.preprocessor.remove_columns(data,['ID'])
            columns={"EDUCATION":"EDU","MARRIAGE":"MARR"}
            data=self.preprocessor.encodevariables(data,columns)
            data=self.preprocessor.remove_columns(data,['EDUCATION','MARRIAGE'])
            data=self.preprocessor.scale_data(data)
            file_loader=file_methods.File_Operation(self.file_object,self.log_writer)
            kmeans=file_loader.load_model('KMeans')
            clusters=kmeans.predict(data)#drops the first column for cluster prediction
            data['clusters']=clusters
            clusters=data['clusters'].unique()
            result=[] # initialize balnk list for storing predicitons
            for i in clusters:
                cluster_data= data[data['clusters']==i]
                cluster_data = cluster_data.drop(['clusters'],axis=1)
                model_name = file_loader.find_correct_model_file(i)
                model = file_loader.load_model(model_name)
                for val in (model.predict(cluster_data)):
                    result.append(val)
            result = pd.DataFrame(result,columns=['Predictions'])
            path="Prediction_Output_File/Predictions.csv"
            result.to_csv("Prediction_Output_File/Predictions.csv",header=True) #appends result to prediction file
            self.log_writer.log(self.file_object,'End of Prediction')
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the prediction!! Error:: %s' % ex)
            raise ex
        return path

           




