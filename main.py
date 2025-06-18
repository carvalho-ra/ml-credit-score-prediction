import pandas as pd

table = pd.read_csv("clientes.csv")

from sklearn.preprocessing import LabelEncoder

coder = LabelEncoder()
coder2 = LabelEncoder()
coder3 = LabelEncoder()

table["profissao"] = coder.fit_transform(table["profissao"])
table["mix_credito"] = coder2.fit_transform(table["mix_credito"])
table["comportamento_pagamento"] = coder3.fit_transform(table["comportamento_pagamento"])

y = table["score_credito"]
x = table.drop(columns=["score_credito", "id_cliente"])

from sklearn.model_selection import train_test_split

x_training, x_test, y_training, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

tree_model = RandomForestClassifier()
knn_model = KNeighborsClassifier()

tree_model.fit(x_training, y_training)
knn_model.fit(x_training, y_training)

predict_tree = tree_model.predict(x_test)
predict_knn = knn_model.predict(x_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predict_tree))
print(accuracy_score(y_test, predict_knn))

new_table = pd.read_csv("novos_clientes.csv")

print(new_table)

new_table["profissao"] = coder.fit_transform(new_table["profissao"])
new_table["mix_credito"] = coder2.fit_transform(new_table["mix_credito"])
new_table["comportamento_pagamento"] = coder3.fit_transform(new_table["comportamento_pagamento"])

final_predict = tree_model.predict(new_table)

print(final_predict)
