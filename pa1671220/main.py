import pandas as pd
mood = pd.read_csv("mood_project_3.csv")
records_array = mood.to_dict("record")

print(type(records_array))

print(records_array[10])

print(mood.iloc[10])



import requests
import json
def get_prediction(data={"sentence":"I am sad."}):
  url = 'https://5syr7ttrk5.execute-api.us-east-1.amazonaws.com/Predict/b036f506-76f9-4b6b-a318-4f0fe0199be1'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  print("RESPONSE", response)
  return response
  

response = json.loads(json.loads(get_prediction(records_array[10]))['body'])['predicted_label']
