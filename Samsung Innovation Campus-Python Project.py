import pandas as pd
data = pd.read_csv('C:/Users/user/Documents/Personal/Project/Samsung Innovation Campus/Εργασία Python/data.csv',sep  = ',', header= 'infer')

#2.Εκτυπώστε τις τελευταίες 5 εγγραφές του dataframe
print("Οι τελευταίες 5 εγγραφές του dataframe είναι:")
print(data.iloc[541904:])
print()

#3.Πόσες (αριθμό) και ποιες (ονόματα) στήλες (columns) έχει το dataset που φορτώσατε;
print("Τα ονόματα των στηλών του dataset είναι:", list(data.columns))
print("Και ο αριθμός τους είναι:", len(data.columns))
print()

#4.Ως τι τύπο δεδομένων αναγνωρίζει η βιβλιοθήκη pandas τις στήλες του dataset;
print("Ο τύπος δεδομένων των στηλών του dataset είναι:")
print(data.dtypes)
print()

#5.Υπάρχουν στήλες με τιμές που λείπουν; Κι αν ναι ποιες; (Ποιες στήλες έχουν missing values /NaN)
columns_with_nan = data.columns[data.isna().any()].tolist()
print("Οι στήλες του dataset στις οποίες λείπουν τιμές (missing values/NaN) είναι:", columns_with_nan)
print()

#6.Ποιος ο συνολικός αριθμών των εγγραφών; (χωρίς τα headers)
print("Ο συνολικός αριθμός των εγγραφών (χωρίς τα headers) είναι:",len(data))

# Αφαιρέστε από το dataset όλες τις γραμμές (rows) που έχουν NaN (missing values) στις στήλες  'Description' ή/και 'CustomerID'.
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

# reset the indexes of DataFrame
data.reset_index()

# Διαγράψτε όλες τις γραμμές που η περιγραφή της στήλης 'Description' είναι : \"AMAZON FEE\",\"Manual\", \"SAMPLES\", \"POSTAGE\" ή \"PACKING CHARGE\".
# Αφαιρέστε απο το dataset όλες εγγραφές έχουν αρνητική τιμή στη στήλη 'Quantity'
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

data.reset_index()
# reset the indexes of DataFrame

# Δημιουργήστε στήλη ονόματι ItemTotal που περιέχει ανά γραμμή το αποτέλεσμα της πράξης Quantity*UnitPrice για τον υπολογισμό του συνολικού κόστους ανά κατηγορία προϊόντων
data["ItemTotal"]=data["Quantity"]*data["UnitPrice"]

#1 - Ποιός ο αριθμός των μοναδικών/διαφορετικών πελατών
print("Number of unique customers: ", end='')
print(data['CustomerID'].nunique())

#2 - Με ποιες χώρες έχει μέχρι σήμερα συναλλαγές η εταιρεία
print("Transactions in the following countries: ")
print(data['Country'].unique())

#3 - Ποιο χρονικό διάστημα αφορούν τα δεδομένα που έχουμε διαθέσιμα
print("Data refers to a timeframe between: ", end='')
print(data['InvoiceDate'].max(), end='')
print(" and ", end='')
print(data['InvoiceDate'].min())

#4 - Ποιο/ ποια προϊόν/τα μπορεί να αγοράσει ένας πελάτης που επιθυμεί να διαθέσει 100-150 ευρώ;
print("A customer can buy the following products with a budget between 100€ and 150€: ")
print(data[data['UnitPrice'].between(100, 150, inclusive=BOTH)].Description.unique())

#5 - Αν κάνουμε αναζήτηση στα προϊόντα (στις περιγραφές) με τον όρο \"HANDBAG\" ποια αποτελέσματα θα λάβουμε;
print("Products with the word 'handbag' in them are the following: ")
print(data[data['Description'].str.contains('HANDBAG', na=False, regex=False)].Description.unique())
