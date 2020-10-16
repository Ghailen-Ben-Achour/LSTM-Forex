from tensorflow.keras.models import load_model
import sys
from functions import extract_train_data,extract_train_datah1,extract_train_datah2,extract_val_data,extract_val_datah1,extract_val_datah2,organising_data,split_sequence
import numpy as np

def compile_model(path):
    """
    :return: compiled model and the timesteps
    """
    model=load_model(path)
    layer=model.layers[0].input
    n_input=layer.shape[2]
    n_steps=layer.shape[1]
    return model,n_input,n_steps

def chose_null_inputs(x_test,network):
    for i in range(x_test.shape[2]):
        val = network.get('p'+str(i))        
        x_test[:,:,i] = x_test[:,:,i]*val
    
def _data(network,n_steps):

        timeframe=network.get('time')
        if timeframe=='h4':
            
            #extraction validation data
            AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY = extract_val_data()

            #Organising the data
            
            data_AUD_CAD,data_AUD_CHF,data_AUD_JPY,data_AUD_NZD,data_AUD_USD,data_CAD_CHF,data_CAD_JPY,data_CHF_JPY,data_EUR_AUD,data_EUR_CAD,data_EUR_CHF,data_EUR_GBP,data_EUR_JPY,data_EUR_NZD,data_EUR_USD,data_GBP_AUD,data_GBP_CAD,data_GBP_CHF,data_GBP_JPY,data_GBP_NZD,data_GBP_USD,data_NZD_CAD,data_NZD_CHF,data_NZD_JPY,data_NZD_USD,data_USD_CAD,data_USD_CHF,data_USD_JPY= organising_data(AUD_CAD,AUD_CHF,AUD_JPY,
                  AUD_NZD,AUD_USD,CAD_CHF,
                  CAD_JPY,CHF_JPY,EUR_AUD,
                  EUR_CAD,EUR_CHF,EUR_GBP,
                  EUR_JPY,EUR_NZD,EUR_USD,
                  GBP_AUD,GBP_CAD,GBP_CHF,
                  GBP_JPY,GBP_NZD,GBP_USD,
                  NZD_CAD,NZD_CHF,NZD_JPY,
                  NZD_USD,USD_CAD,USD_CHF,
                  USD_JPY)
            #Split X and Y

            X_AUD_CAD,y_AUD_CAD=split_sequence(data_AUD_CAD , n_steps)
            X_AUD_CHF,y_AUD_CHF=split_sequence(data_AUD_CHF , n_steps)
            X_AUD_JPY,y_AUD_JPY=split_sequence(data_AUD_JPY , n_steps)
            X_AUD_NZD,y_AUD_NZD=split_sequence(data_AUD_NZD , n_steps)
            X_AUD_USD,y_AUD_USD=split_sequence(data_AUD_USD , n_steps)
            X_CAD_CHF,y_CAD_CHF=split_sequence(data_CAD_CHF , n_steps)
            X_CAD_JPY,y_CAD_JPY=split_sequence(data_CAD_JPY , n_steps)
            X_CHF_JPY,y_CHF_JPY=split_sequence(data_CHF_JPY , n_steps)
            X_EUR_AUD,y_EUR_AUD=split_sequence(data_EUR_AUD , n_steps)
            X_EUR_CAD,y_EUR_CAD=split_sequence(data_EUR_CAD , n_steps)
            X_EUR_CHF,y_EUR_CHF=split_sequence(data_EUR_CHF , n_steps)
            X_EUR_GBP,y_EUR_GBP=split_sequence(data_EUR_GBP , n_steps)
            X_EUR_JPY,y_EUR_JPY=split_sequence(data_EUR_JPY , n_steps)
            X_EUR_NZD,y_EUR_NZD=split_sequence(data_EUR_NZD , n_steps)
            X_EUR_USD,y_EUR_USD=split_sequence(data_EUR_USD , n_steps)
            X_GBP_AUD,y_GBP_AUD=split_sequence(data_GBP_AUD , n_steps)
            X_GBP_CAD,y_GBP_CAD=split_sequence(data_GBP_CAD , n_steps)
            X_GBP_CHF,y_GBP_CHF=split_sequence(data_GBP_CHF , n_steps)
            X_GBP_JPY,y_GBP_JPY=split_sequence(data_GBP_JPY , n_steps)
            X_GBP_NZD,y_GBP_NZD=split_sequence(data_GBP_NZD , n_steps)
            X_GBP_USD,y_GBP_USD=split_sequence(data_GBP_USD , n_steps)
            X_NZD_CAD,y_NZD_CAD=split_sequence(data_NZD_CAD , n_steps)
            X_NZD_CHF,y_NZD_CHF=split_sequence(data_NZD_CHF , n_steps)
            X_NZD_JPY,y_NZD_JPY=split_sequence(data_NZD_JPY , n_steps)
            X_NZD_USD,y_NZD_USD=split_sequence(data_NZD_USD , n_steps)
            X_USD_CAD,y_USD_CAD=split_sequence(data_USD_CAD , n_steps)
            X_USD_CHF,y_USD_CHF=split_sequence(data_USD_CHF , n_steps)
            X_USD_JPY,y_USD_JPY=split_sequence(data_USD_JPY , n_steps)
            
            

            #Concatinate the input in a single 3D matrix
            val_inputs=np.dstack((X_AUD_CAD,X_AUD_CHF,X_AUD_JPY,X_AUD_NZD,X_AUD_USD,
                  X_CAD_CHF,X_CAD_JPY,X_CHF_JPY,X_EUR_AUD,X_EUR_CAD,
                  X_EUR_CHF,X_EUR_GBP,X_EUR_JPY,X_EUR_NZD,X_EUR_USD,
                  X_GBP_AUD,X_GBP_CAD,X_GBP_CHF,X_GBP_JPY,X_GBP_NZD,
                  X_GBP_USD,X_NZD_CAD,X_NZD_CHF,X_NZD_JPY,X_NZD_USD,
                  X_USD_CAD,X_USD_CHF,X_USD_JPY))


            #Concatinate the output in a single matrix
            val_output=np.column_stack((y_AUD_CAD,y_AUD_CHF,y_AUD_JPY,y_AUD_NZD,y_AUD_USD,
                  y_EUR_AUD,y_GBP_AUD))
            
        elif timeframe=='h1':

            
            #extraction validation data
            AUD_CAD,AUD_CHF,AUD_JPY,AUD_NZD,AUD_USD,CAD_CHF,CAD_JPY,CHF_JPY,EUR_AUD,EUR_CAD,EUR_CHF,EUR_GBP,EUR_JPY,EUR_NZD,EUR_USD,GBP_AUD,GBP_CAD,GBP_CHF,GBP_JPY,GBP_NZD,GBP_USD,NZD_CAD,NZD_CHF,NZD_JPY,NZD_USD,USD_CAD,USD_CHF,USD_JPY = extract_val_datah1()

            #Organising the data
            
            data_AUD_CAD,data_AUD_CHF,data_AUD_JPY,data_AUD_NZD,data_AUD_USD,data_CAD_CHF,data_CAD_JPY,data_CHF_JPY,data_EUR_AUD,data_EUR_CAD,data_EUR_CHF,data_EUR_GBP,data_EUR_JPY,data_EUR_NZD,data_EUR_USD,data_GBP_AUD,data_GBP_CAD,data_GBP_CHF,data_GBP_JPY,data_GBP_NZD,data_GBP_USD,data_NZD_CAD,data_NZD_CHF,data_NZD_JPY,data_NZD_USD,data_USD_CAD,data_USD_CHF,data_USD_JPY= organising_data(AUD_CAD,AUD_CHF,AUD_JPY,
                  AUD_NZD,AUD_USD,CAD_CHF,
                  CAD_JPY,CHF_JPY,EUR_AUD,
                  EUR_CAD,EUR_CHF,EUR_GBP,
                  EUR_JPY,EUR_NZD,EUR_USD,
                  GBP_AUD,GBP_CAD,GBP_CHF,
                  GBP_JPY,GBP_NZD,GBP_USD,
                  NZD_CAD,NZD_CHF,NZD_JPY,
                  NZD_USD,USD_CAD,USD_CHF,
                  USD_JPY)
            #Split X and Y

            X_AUD_CAD,y_AUD_CAD=split_sequence(data_AUD_CAD , n_steps)
            X_AUD_CHF,y_AUD_CHF=split_sequence(data_AUD_CHF , n_steps)
            X_AUD_JPY,y_AUD_JPY=split_sequence(data_AUD_JPY , n_steps)
            X_AUD_NZD,y_AUD_NZD=split_sequence(data_AUD_NZD , n_steps)
            X_AUD_USD,y_AUD_USD=split_sequence(data_AUD_USD , n_steps)
            X_CAD_CHF,y_CAD_CHF=split_sequence(data_CAD_CHF , n_steps)
            X_CAD_JPY,y_CAD_JPY=split_sequence(data_CAD_JPY , n_steps)
            X_CHF_JPY,y_CHF_JPY=split_sequence(data_CHF_JPY , n_steps)
            X_EUR_AUD,y_EUR_AUD=split_sequence(data_EUR_AUD , n_steps)
            X_EUR_CAD,y_EUR_CAD=split_sequence(data_EUR_CAD , n_steps)
            X_EUR_CHF,y_EUR_CHF=split_sequence(data_EUR_CHF , n_steps)
            X_EUR_GBP,y_EUR_GBP=split_sequence(data_EUR_GBP , n_steps)
            X_EUR_JPY,y_EUR_JPY=split_sequence(data_EUR_JPY , n_steps)
            X_EUR_NZD,y_EUR_NZD=split_sequence(data_EUR_NZD , n_steps)
            X_EUR_USD,y_EUR_USD=split_sequence(data_EUR_USD , n_steps)
            X_GBP_AUD,y_GBP_AUD=split_sequence(data_GBP_AUD , n_steps)
            X_GBP_CAD,y_GBP_CAD=split_sequence(data_GBP_CAD , n_steps)
            X_GBP_CHF,y_GBP_CHF=split_sequence(data_GBP_CHF , n_steps)
            X_GBP_JPY,y_GBP_JPY=split_sequence(data_GBP_JPY , n_steps)
            X_GBP_NZD,y_GBP_NZD=split_sequence(data_GBP_NZD , n_steps)
            X_GBP_USD,y_GBP_USD=split_sequence(data_GBP_USD , n_steps)
            X_NZD_CAD,y_NZD_CAD=split_sequence(data_NZD_CAD , n_steps)
            X_NZD_CHF,y_NZD_CHF=split_sequence(data_NZD_CHF , n_steps)
            X_NZD_JPY,y_NZD_JPY=split_sequence(data_NZD_JPY , n_steps)
            X_NZD_USD,y_NZD_USD=split_sequence(data_NZD_USD , n_steps)
            X_USD_CAD,y_USD_CAD=split_sequence(data_USD_CAD , n_steps)
            X_USD_CHF,y_USD_CHF=split_sequence(data_USD_CHF , n_steps)
            X_USD_JPY,y_USD_JPY=split_sequence(data_USD_JPY , n_steps)
            
            
            #Concatinate the input in a single 3D matrix
            val_inputs=np.dstack((X_AUD_CAD,X_AUD_CHF,X_AUD_JPY,X_AUD_NZD,X_AUD_USD,
                  X_CAD_CHF,X_CAD_JPY,X_CHF_JPY,X_EUR_AUD,X_EUR_CAD,
                  X_EUR_CHF,X_EUR_GBP,X_EUR_JPY,X_EUR_NZD,X_EUR_USD,
                  X_GBP_AUD,X_GBP_CAD,X_GBP_CHF,X_GBP_JPY,X_GBP_NZD,
                  X_GBP_USD,X_NZD_CAD,X_NZD_CHF,X_NZD_JPY,X_NZD_USD,
                  X_USD_CAD,X_USD_CHF,X_USD_JPY))


            #Concatinate the output in a single matrix
            val_output=np.column_stack((y_AUD_CAD,y_AUD_CHF,y_AUD_JPY,y_AUD_NZD,y_AUD_USD,
                  y_EUR_AUD,y_GBP_AUD))
            
        
        return val_inputs,val_output


def loss(network,y_test,prediction):
    MAE=0
    for i in range(prediction.shape[0]):
        for j in range (prediction.shape[1]):
            MAE += abs(prediction[i][j]-y_test[i][j])
    MAE/=prediction.shape[0]
    return MAE

def output_order(network,y_test,prediction,output):
    
    for i in range(prediction.shape[0]):
        for j in range (prediction.shape[1]):
            if j!= output:
                prediction[i][j]=y_test[i][j]
    
    order=network.get('output') 

    prediction[:,order]=prediction[:,output]
    prediction[:,output]=y_test[:,output]
    y_test[:,order]=y_test[:,output]


    return prediction,order
    
def train_and_score(network,path,output):
    """
    :return float: score
    """
    model,n_input,n_steps=compile_model(path)
    x_test, y_test=_data(network,n_steps)
    chose_null_inputs(x_test,network)
    prediction=model.predict([x_test])
    prediction,order=output_order(network,y_test,prediction,output)   
    MAE=loss(network,y_test,prediction)
    print(MAE)
    return MAE  #loss.
