import pandas as pd
data = pd.read_csv('C:/Users/mario/Documents/Personal/Project/Samsung Innovation Campus/Εργασία Python/data.csv', sep=',', header='infer')
# imports library and reads the csv file as "data"



# Οδηγίες για τον καθαρισμό του dataset
data = data.dropna(axis=0, inplace=True)
# Αφαιρέστε από το dataset όλες τις γραμμές (rows) που έχουν NaN (missing values) στις στήλες  'Description' ή/και 'CustomerID'.

for i in data.index.tolist():
    if data.at[i, "Description"] == "AMAZON FEE" or data.at[i, "Quantity"]<0:
        data.drop(i, implace=True, axis=0)
    else if data.at[i, "Description"] == "Manual" or data.at[i, "Quantity"]<0:
        data.drop(i, implace=True, axis=0)
    else if data.at[i, "Description"] == "SAMPLES" or data.at[i, "Quantity"]<0:
        data.drop(i, implace=True, axis=0)
    else if data.at[i, "Description"] == "POSTAGE" or data.at[i, "Quantity"]<0:
        data.drop(i, implace=True, axis=0)
    else if data.at[i, "Description"] == "PACKING CHARGE" or data.at[i, "Quantity"]<0:
        data.drop(i, implace=True, axis=0)
# Διαγράψτε όλες τις γραμμές που η περιγραφή της στήλης 'Description' είναι : \"AMAZON FEE\",\"Manual\", \"SAMPLES\", \"POSTAGE\" ή \"PACKING CHARGE\". 
# Αφαιρέστε απο το dataset όλες εγγραφές έχουν αρνητική τιμή στη στήλη 'Quantity'

data["ItemTotal"]=data["Quantity"]*data["UnitPrice"]
# Δημιουργήστε στήλη ονόματι ItemTotal που περιέχει ανά γραμμή το αποτέλεσμα της πράξης Quantity*UnitPrice για τον υπολογισμό του συνολικού κόστους ανά κατηγορία προϊόντων
