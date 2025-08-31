import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from training.train_utils import DATA_FILE_PATH,MODEL_DIR,MODEL_FILE_PATH

df = pd.read_csv(DATA_FILE_PATH)
df = df.drop_duplicates()
df = df.drop(columns=['name' , 'model' , 'edition'])

X = df.drop(columns=['selling_price'])
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_cols = X_train.select_dtypes(include='number').columns.to_list()
cat_cols = [col for col in X_train.columns if col not in num_cols]

num_pipe = Pipeline(
    steps=[
        ('imputer' , SimpleImputer(strategy='median')),
        ('scaler' , StandardScaler())
    ]
)

cat_pipe = Pipeline(
    steps=[
        ('imputer' , SimpleImputer(strategy='constant' , fill_value='missing')),
        ('onehot' , OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('num' , num_pipe , num_cols),
        ('cat' , cat_pipe , cat_cols) 
    ]
)

regressor = RandomForestRegressor(n_estimators=10, max_depth=5, random_state=42)

rf_model = Pipeline(
    steps=[
        ('preprocessor' , preprocessor),
        ('regressor' , regressor)
    ]
)

rf_model.fit(X_train, y_train)

os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_FILE_PATH)


