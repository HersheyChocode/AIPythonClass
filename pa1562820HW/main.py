import pandas as pd



#Excercise 1
columns = ["ID","Disease", "Symptom 1", "Symptom 2", "Symptom 3"]
dfObj = pd.DataFrame(columns = columns)


dfObj = dfObj.append({"ID":"345234", "Disease":"Pneumonia",  "Symptom 1": "Fever", "Symptom 2": "Cough", "Symptom 3":  "Fatigue"}, ignore_index=True)
dfObj = dfObj.append({"ID":"576634", "Disease":"Pneumonia",  "Symptom 1": "Chills", "Symptom 2": "Fever", "Symptom 3":  "Dehydration"}, ignore_index=True)
dfObj = dfObj.append({"ID":"456345", "Disease":"Pneumonia",  "Symptom 1": "Sweating", "Symptom 2": "Fever", "Symptom 3":  "Shortness of breath"}, ignore_index=True)
dfObj = dfObj.append({"ID":"563478", "Disease":"Pneumonia",  "Symptom 1": "Fatigue", "Symptom 2": "Chills", "Symptom 3":  "Shortness of breath"}, ignore_index=True)

dfObj = dfObj.append({"ID":"234985", "Disease":"Malaria",  "Symptom 1": "Chills", "Symptom 2": "Fever", "Symptom 3":  "Nausea"}, ignore_index=True)
dfObj = dfObj.append({"ID":"678932", "Disease":"Malaria",  "Symptom 1": "Diarrhea", "Symptom 2": "Nausea", "Symptom 3":  "Fever"}, ignore_index=True)
dfObj = dfObj.append({"ID":"345692", "Disease":"Malaria",  "Symptom 1": "Nausea", "Symptom 2": "Diarrhea", "Symptom 3":  "Chills"}, ignore_index=True)
dfObj = dfObj.append({"ID":"234845", "Disease":"Malaria",  "Symptom 1": "Fever", "Symptom 2": "Chills", "Symptom 3":  "Nausea"}, ignore_index=True)

print(dfObj)

#Excercise 2
#contents = {}

symptoms = ["Disease"]
disease = []
for x in range(0,len(dfObj)):
  disease.append(dfObj.iloc[x,1])

  for y in range(2, len(dfObj.columns)):
    if (dfObj.iloc[x,y] not in symptoms):
      symptoms.append(dfObj.iloc[x,y])

dfObj2 = pd.DataFrame(columns = symptoms)

for x in range(0,len(disease)):
  array = {}
  array["Disease"] = disease[x]
  for y in range(1,len(symptoms)):
    if(symptoms[y] in dfObj.iloc[x,2] or symptoms[y] in dfObj.iloc[x,3] or symptoms[y] in dfObj.iloc[x,4]):
      array[symptoms[y]] = "1"
    else:
      array[symptoms[y]] = "0"
  dfObj2 = dfObj2.append(array, ignore_index = True)
    
print(dfObj2)