import pandas as pd
import os
from sklearn.model_selection import train_test_split

input_data_path = os.path.join("/opt/ml/processing/input", "dataset.csv")
df = pd.read_csv(input_data_path)
print("Shape of data is: ", df.shape)
train, test = train_test_split(df, test_size=0.2)
train, validation = train_test_split(train, test_size=0.2)

train_path = "/opt/ml/processing/output/train"
valid_path = "/opt/ml/processing/output/validation"
test_path = "/opt/ml/processing/output/test"

is_exist_train = os.path.exists(train_path)
is_exist_valid = os.path.exists(valid_path)
is_exist_test = os.path.exists(test_path)

try:
    if not is_exist_train:
        os.makedirs("/opt/ml/processing/output/train")
    if not is_exist_valid:
        os.makedirs("/opt/ml/processing/output/validation")
    if not is_exist_test:
        os.makedirs("/opt/ml/processing/output/test")
    print("Successfully created directories")
except Exception as e:
    # if the Processing call already create these directories ( or directory otherwise cannot be created)
    print(e)
    print("Could not make directories")
    pass

try:
    train.to_csv("/opt/ml/processing/output/train/train.csv")
    validation.to_csv("/opt/ml/processing/output/validation/validation.csv")
    test.to_csv("/opt/ml/processing/output/test/test.csv")
    print("Wrote files successfully")
except Exception as e:
    print("Failed to write the files")
    print(e)
    pass

print("Completed running the processing job")
    
