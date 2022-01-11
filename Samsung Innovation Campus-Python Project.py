import pandas as pd
data = pd.read_csv('C:/Users/mario/Documents/Personal/Project/Samsung Innovation Campus/Εργασία Python/data.csv', sep=',', header='infer')







# ! Οδηγίες για τον καθαρισμό του dataset
description_bool = data["Description"].isnull()
customer_bool = data['CustomerID'].isnull()
# create isnull bool Series for the two collums of the DataFrame
for i in data.index:
    # for each index in the two Series check if value is NaN
    if description_bool.at[i]==True or customer_bool.at[i]==True:
        print(description_bool.at[i], "and", customer_bool.at[i])
        data.drop(i, inplace=True, axis=0)
        print("row",i,"deleted")
        # if value NaN in Series found, delete row of main DataFrame
# ! Αφαιρέστε από το dataset όλες τις γραμμές (rows) που έχουν NaN (missing values) στις στήλες  'Description' ή/και 'CustomerID'.

data.reset_index()
# reset the indexes of DataFrame

for i in data.index:
    if data.at[i, "Description"] == "AMAZON FEE" or data.at[i, "Quantity"] < 0:
        data.drop(i, inplace=True, axis=0)
        print("item_deleted at", i)
    elif data.at[i, "Description"] == "Manual" or data.at[i, "Quantity"] < 0:
        data.drop(i, inplace=True, axis=0)
        print("item_deleted at", i)
    elif data.at[i, "Description"] == "SAMPLES" or data.at[i, "Quantity"] < 0:
        data.drop(i, inplace=True, axis=0)
        print("item_deleted at", i)
    elif data.at[i, "Description"] == "POSTAGE" or data.at[i, "Quantity"] < 0:
        data.drop(i, inplace=True, axis=0)
        print("item_deleted at", i)
    elif data.at[i, "Description"] == "PACKING CHARGE" or data.at[i, "Quantity"] < 0:
        data.drop(i, implace=True, axis=0)
        print("item_deleted at", i)
# ! Διαγράψτε όλες τις γραμμές που η περιγραφή της στήλης 'Description' είναι : \"AMAZON FEE\",\"Manual\", \"SAMPLES\", \"POSTAGE\" ή \"PACKING CHARGE\".
# ! Αφαιρέστε απο το dataset όλες εγγραφές έχουν αρνητική τιμή στη στήλη 'Quantity'

data.reset_index()
# reset the indexes of DataFrame

data["ItemTotal"]=data["Quantity"]*data["UnitPrice"]
# ! Δημιουργήστε στήλη ονόματι ItemTotal που περιέχει ανά γραμμή το αποτέλεσμα της πράξης Quantity*UnitPrice για τον υπολογισμό του συνολικού κόστους ανά κατηγορία προϊόντων
