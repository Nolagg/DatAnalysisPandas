import codecademylib
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head())

orders['shoe_source'] = orders['shoe_material'].apply(
   lambda x: 'animal' \
   if x == 'leather' \
   else 'vegan')

salutation = lambda row: 'Dear Ms. ' + row['last_name'] \
if row['gender'] == 'female' \
else 'Dear Mr. ' + row['last_name']
axis=1

orders['salutation'] = orders.apply(lambda row: salutation(row),
                                   axis = 1)
print(orders)