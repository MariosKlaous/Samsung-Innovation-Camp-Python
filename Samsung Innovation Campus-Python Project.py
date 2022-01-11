import pandas as pd
#1.Διαβάστε το αρχείο data.csv
data = pd.read_csv('C:/Users/mario/Documents/Personal/Project/Samsung Innovation Campus/Εργασία Python/data.csv', sep=',', header='infer')
#2.Εκτυπώστε τις τελευταίες 5 εγγραφές του dataframe
print(data.iloc[541904:])
#3.Πόσες (αριθμό) και ποιες (ονόματα) στήλες (columns) έχει το dataset που φορτώσατε;
print(data.columns)
len(data.columns)
#4.Ως τι τύπο δεδομένων αναγνωρίζει η βιβλιοθήκη pandas τις στήλες του dataset;
print(type(data.columns))
columns= list(data.columns) #ΧΡΕΙΑΖΕΤΑΙ Η ΜΕΤΑΤΡΟΠΗ ΣΕ ΛΙΣΤΑ;;;
print(type(columns))
#5.Υπάρχουν στήλες με τιμές που λείπουν; Κι αν ναι ποιες; (Ποιες στήλες έχουν missing values /NaN)
data.isnull().any()
#6.Ποιος ο συνολικός αριθμών των εγγραφών; (χωρίς τα headers)
len(data)
