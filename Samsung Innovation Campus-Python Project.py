from tkinter import BOTH
import pandas as pd
data = pd.read_csv('C:/Users/mario/Documents/Personal/Project/Samsung Innovation Campus/Εργασία Python/data.csv', sep=',', header='infer')



















































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
