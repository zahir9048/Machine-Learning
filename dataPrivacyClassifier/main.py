import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV


def predict_privacy_level(df, sample_data_file, feature_mapping, output_feature, values_dict):
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.columns = df.columns.str.strip()

    # Display the sample loaded data
    # print("\nAll Columns:")
    # print(df.columns)
    # print(df.isnull().sum())
    # print("\nLoaded Data:")
    # print(df)

    # Plotting the graph of Target Variable
    plt.bar(df['Target_Privacy_Level'].value_counts().index, df['Target_Privacy_Level'].value_counts().values, color='blue')
    # Set labels and title
    plt.xlabel('Privacy Level Encoding')
    plt.ylabel('Count of Targets')
    plt.xticks([0, 1, 2])
    plt.title('Distribution of Privacy Levels in Sample Data')
    plt.show()

    # Features (X)
    input_Features = list(feature_mapping.keys())
    df[input_Features] = df[input_Features].fillna(0)
    X = df[input_Features]  # Input Features variable (X)
    Y = df[output_feature]  # Target variable (Y)

    # Split & Train the model on the training data
    print("\nTraining the Model using Training Dataset...")
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    rf_clf = RandomForestClassifier(random_state=42, min_samples_split=10)
    rf_clf.fit(X_train, Y_train)

    # print(rf_clf.predict([[1,0,0,0.6]]))
    # print(rf_clf.predict_proba([[1,0,0,0.6]]))

    print("Model Trained Successfuly!")
    # Predictions on the test data set
    Y_pred_rf = rf_clf.predict(X_test)
    # print(Y_test)
    # print(Y_pred_rf)

    # Evaluate the accuracy of the model
    accuracy_rf = (accuracy_score(Y_test, Y_pred_rf)) * 100

    # Extract Input Features into a variable for Prediction
    user_input = pd.DataFrame({feature: [mapping] for feature, mapping in feature_mapping.items()})
    # Predict the Privacy level of the Entered Data
    print("\nPredicting the Privacy Level of the Input Data using Random Forest Classifier...")
    predicted_class = rf_clf.predict(user_input)
    print("Data Privacy Level Classified Successfully!")

    if predicted_class[0] == 0:
        privacy_level = 'Low'
    elif predicted_class[0] == 1:
        privacy_level = 'Medium'
    else:
        privacy_level = 'High'

    if accuracy_rf > 85:
        user_input[output_feature] = predicted_class[0]
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.today().strftime("%d-%m-%Y")
        user_input['Date&Time'] = current_date + " " + current_time
        user_input['Privacy_Level'] = privacy_level
        user_input = user_input.reindex(columns=df.columns, fill_value=None)
        for column, value in values_dict.items():
            user_input[column] = value
        updated_df = pd.concat([df, user_input], ignore_index=True)
        print("\nUpdating the Training Dataset with the Input Data...")
        updated_df.to_csv(sample_data_file, index=False)
        print("Data Uploaded into CSV Training Dataset File Successfully!")
    return privacy_level, accuracy_rf


sample_data_file = r"C:\Users\CC\PycharmProjects\dataPrivacyClassifier\sample data\Data.csv"

df = pd.read_csv(sample_data_file)
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
df.columns = df.columns.str.strip()
# print(df.columns)

non_input_feature_columns = [col for col in df.columns if
                             'Has_' not in col and 'Target_' not in col and 'Privacy_Level' not in col and 'Date' not in col]
# print(non_input_feature_columns)

input_features = [col for col in df.columns if 'Has_' in col]
# print(input_features)

output_feature = next((col for col in df.columns if "Target_" in col), None)

values_list = []
mapping_list = []
print(" ")
for non_input_feature in non_input_feature_columns:

    corresponding_input_feature = f'Has_{non_input_feature}'
    value = input(f"Enter the value for {non_input_feature}: ")

    if corresponding_input_feature in input_features:
        mapping = 0 if not value else 1
        if value == '':
            values_list.append((non_input_feature, ''))
        else:
            values_list.append((non_input_feature, value))
        mapping_list.append((corresponding_input_feature, mapping))
    else:
        if value == '':
            values_list.append((non_input_feature, ''))
        else:
            values_list.append((non_input_feature, value))


values_dict = {input_value: values for input_value, values in values_list}
# print("Values List: ", values_dict)

input_features_dict = {input_feature: mapping_value for input_feature, mapping_value in mapping_list}
# print("Input Features List: ", input_features_dict)

result, accuracy_rf = predict_privacy_level(df, sample_data_file, input_features_dict, output_feature, values_dict)

print('\nResults:')
print(f"Predicted Privacy Level using Random Forest Algorithm of Entered Data is: {result}")
print(f"Random Forest Algorithm Data Accuracy: {accuracy_rf:.2f}%")
