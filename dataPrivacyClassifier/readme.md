About this Project:

This is a simple Data privacy classifier project using Supervised machine learning algorithm Random forest algorithm. In this project,
we are identifying the privacy level of the structured data that is entered via input command line.

Basically, we are training our model using sample data which contains predefined columns (input features & output feature). There are 4 input features for this project: Email field, Phone number field, Address field & ID field. There is 1 output feature which is
Target Privacy level. 

These input & output features columns data are in binary format.



To run this Project:

Download python, any python IDE (preferably PYCharm), and program packages dependencies. Download this repository. Sample data csv file is present in the Sample data folder.

Install these packages before running program: 
1) pandas
2) from sklearn.model_selection import train_test_split
3) from sklearn.ensemble import RandomForestClassifier
4) from sklearn.metrics import accuracy_score
5) from datetime import datetime
6) seaborn
7) matplotlib.pyplot
8) from sklearn.model_selection import GridSearchCV

Download these packages using python interpreter and then run the main.py file.

Note: Before running main.py, close the csv file or it will throw error on running.


Mechanism of Project:

Privacy level of data is classified based on the input features(encoded in binary 0, 1). There are 3 privacy levels low, medium, high encoded as 0, 1, 2. Now, the input features will decide what is the target privacy level. If data contains ID or Address, its privacy level is high, if it contains only phone number, then its medium. If it contains only email, then its privacy level is low.



Working of Program: 

1) The program firsts read the sample data file. It extracts the inpput & output features from the data.
2) Then, program takes the data to be classified as input from user on command line. This data is basically input features that will be used to predict the privacy level of data.
3) The data is inputted from user is in text or null string form. If the data field is empty or null, then that input feature is assigned 0, and if it contains data, then that input feature is assigned 1.
4) After converting data into its encoded form. Now the data is sent to predict_privacy_level function. Sample data file url is also sent into this function (as later the results will also be uploaded into this csv sample data file).
5) Inside function, first a graph is plotted which shows the summary of sample data in terms of output feature (it shows the total number of each class (0,1,2) in the sample data)
6) Then the sample data is classified into two datasets: Test Dataset & Training Dataset.
5) After that, the model is trained using Random Forest classifier using Train dataset.
7) Then, the model is tested using test dataset. 
8) Then the accuracy of the test dataset is calculated.
9) Finally, the target privacy level of the input data (bu user) is predicted using .predict() function.
10) If predicted privacy level is 0, then it will be low, if its 1, then it will be medium and if its 2, then it will be high.
11) If accuracy of the model is greater than 85, then the results of this new prediction is uploaded into Sample dataset, so each time a prediction is made, the size of sample data increases which increases the accuracy of the model. 
12) In the end, the function returns the results, and the target privacy level is displayed.


Note: All the data is made up, and not actual.


