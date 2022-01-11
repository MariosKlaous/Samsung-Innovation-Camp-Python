import pandas as pd
#Ερωτήματα που αφορούν την περιγραφή του dataset

#1.Διαβάστε το αρχείο data.csv
data = pd.read_csv('C:/Users/mario/Documents/Personal/Project/Samsung Innovation Campus/Εργασία Python/data.csv', sep=',', header='infer')
print(data)

#2.Εκτυπώστε τις τελευταίες 5 εγγραφές του dataframe
print("Οι τελευταίες 5 εγγραφές του dataframe είναι:")
print(data.iloc[541904:])

#3.Πόσες (αριθμό) και ποιες (ονόματα) στήλες (columns) έχει το dataset που φορτώσατε;
print("Τα ονόματα των στηλών του dataset είναι:", list(data.columns))
print("Και ο αριθμός τους είναι:", len(data.columns))

#4.Ως τι τύπο δεδομένων αναγνωρίζει η βιβλιοθήκη pandas τις στήλες του dataset;
print("Ο τύπος δεδομένων των στηλών του dataset είναι:")
data.dtypes

#5.Υπάρχουν στήλες με τιμές που λείπουν; Κι αν ναι ποιες; (Ποιες στήλες έχουν missing values /NaN)
columns_with_nan = data.columns[nan_values.any()].tolist()
print("Οι στήλες του dataset στις οποίες λείπουν τιμές (missing values/NaN) είναι:", columns_with_nan)

#6.Ποιος ο συνολικός αριθμών των εγγραφών; (χωρίς τα headers)
print("Ο συνολικός αριθμός των εγγραφών (χωρίς τα headers) είναι:",len(data))
