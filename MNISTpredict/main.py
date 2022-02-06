import json
import pandas as pd
import requests

def get_prediction(data):
    url = "https://3h6ys7t373.execute-api.us-east-1.amazonaws.com/Predict/17871c01-adb4-4d0c-8a85-ffe4c3d164ee"
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    #print(response)
    return response
mnist_test = pd.read_csv('mnist_test_2000.csv')
records_array = mnist_test.to_dict('records')

# Please change the row_index to any value you like between 0 and 1999
row_index = 1800

response = get_prediction(data=records_array[row_index])
print('AI predicted: ', json.loads(json.loads(response)['body'])['predicted_label'])
print('Real value:', records_array[row_index]['label'])