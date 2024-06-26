# -*- coding: utf-8 -*-


from google.colab import drive
drive.mount('/content/drive/Colab Notebook')

import pandas as pd
test_data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/testTi.csv")
train_data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/trainTi.csv")

test_data.head()

train_data.head()

#For Numerical Attributes
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

#For Categorical Attributes
from sklearn.preprocessing import OneHotEncoder
cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("cat_encoder", OneHotEncoder(sparse=False)),
    ])

from sklearn.compose import ColumnTransformer

num_attribs = ["Age", "SibSp", "Parch", "Fare"]
cat_attribs = ["Pclass", "Sex", "Embarked"]

preprocess_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", cat_pipeline, cat_attribs),
    ])

X_train = preprocess_pipeline.fit_transform(
    train_data[num_attribs + cat_attribs])
X_train

y_train = train_data["Survived"]

X_test = preprocess_pipeline.transform(test_data[num_attribs + cat_attribs])

y_test=test_data



from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)

df_result = pd.DataFrame(test_data,columns=['PassengerId'])
df_result["Survived"]=y_pred
df_result

df_result.to_csv("submission.csv",index=False)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=120)
knn.fit(X_train,y_train)
y_pred2=knn.predict(X_test)

df_result1 = pd.DataFrame(test_data,columns=['PassengerId'])
df_result1["Survived"]=y_pred2
df_result1







