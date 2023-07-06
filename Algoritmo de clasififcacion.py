# Importar bibliotecas necesarias
import sklearn
import pandas as pd
datos = pd.read_csv("abc-entrenamiento.csv")
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

datos.info()
datos.head(5)

print(datos)

# Preprocesar los datos de entrenamiento
#X_entrenamiento = datos.loc[:, ['nsrr_age','nsrr_sex','nsrr_bmi','nsrr_ttldursp_f1','ess_total','snoring','arterial_hypertension','daytime_sleepiness']]
#y_entrenamiento = datos.loc[:, ['diagnosis']]

#print(X_entrenamiento)
#print(y_entrenamiento)
