# Volors Routes

## /headers/[model_name]

`GET` 

Return the list of data headers for a model
    
    Takes a model name as string
    Returns json list of header names as strings
    

## /learn

`POST` 

Clean up data, train model, and dump to file. Return model name.

    Takes a base64-encoded csv file
    Returns model name as string
    

## /models

`GET` 

Get list of model names for each model in the folder
    
    Returns json list of model names as strings.
    

## /predict

`POST` 

Load the model and return a json-formatted prediction
    
    Takes a form with 'model' attribute set to model name
    Returns the prediction array for csv features ('data')
    

