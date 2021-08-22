import pandas as pd
import pickle
from flask              import Flask, request, Response
from rossmann.Rossmann  import Rossmann


# loading model

model = pickle.load(open('C:/Users/herna/repos/Data_Science_em_Producao/Model/model_rossmann.pkl', 'rb'))

# inicializar API

app = Flask(__name__)

@app.route('/rossmann/predict', methods=['POST'])

def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # se houver dados
        
        if isinstance(test_json, dict):  # um exemplo      
            test_raw = pd.DataFrame(test_json, index=[0])        
        else:  # múltiplos exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
            
        # instanciando a rossmann class
        
        pipeline = Rossmann()
        
        # limpeza dos dados
        
        df1 = pipeline.data_cleaning(test_raw)
        
        # featuring engineering
        
        df2 = pipeline.featuring_engineering(df1)
        
        # data preparation
        
        df3 = pipeline.data_preparation(df2)
        
        # predict
        
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
        
    else: 
        return Response( '{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    
    app.run('0.0.0.0')
