![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Spyder](https://img.shields.io/badge/Spyder-838485?style=for-the-badge&logo=spyder%20ide&logoColor=maroon)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![SciKit](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white)


# Term_Deposit_Prediction using Deep Learning

### Descriptions
 1) This dataset contains more than 30,000 data with 18 attributes ~ `17 features` & `1 target`
 2) This is a classification problem: either True(1) or False(0)
 3) The dataset contains NaN/null value, the highest is above 20,000 
 4) The approach for this Training Data will be `Sequential` in Deep Learning using `Dense Layer`
 5) The dataset is combination of categorical and continuous data, the target is in Categorical data
 6) Two approach needed to inspect the model and select the best features
 7) 1st approach: Continuos vs Categorical : `Logistic Regression`
 8) 2nd approach: Categorical vs Categorical : `Cramers'V`
 9) The data is being trained with 100 epochs with DropOut layer, BatchNormalizaton Layer and EarlyStopping
 
### Results

`Model using Sequential`

![model_2](https://user-images.githubusercontent.com/106902414/175005001-69c50a0f-f4fb-4b65-92e8-22832fed1836.PNG)


`Model`: 

<img src="plot and result/model_3.png" alt="model" style="width:350px;height:500px;">




`Classification_Report`

![f1 score](https://user-images.githubusercontent.com/106902414/175004436-260b9566-a4a7-4578-a785-f2333b501464.PNG)

`Confusion_Matrix` 

![ConfusionMatrixDisplay](https://user-images.githubusercontent.com/106902414/175007451-2d60ebb1-fde1-4cc3-bc90-78a1004b1ee4.png)


`Training Data` example for continuous data:

![customer_age](https://user-images.githubusercontent.com/106902414/175008522-0096dc41-6166-4217-81a2-8e685c8e71e4.png)


`Training Data` example for categorical data:

![education](https://user-images.githubusercontent.com/106902414/175008968-7722f4f1-3ad6-4d42-8ded-c33949b403a7.png)



`Training Data` example for relationship between the features and the target:


![term_deposit vs personal_loan](https://user-images.githubusercontent.com/106902414/175009335-6fc032af-4e93-4689-9604-9f7a9bda11a7.png)


`TensorBoard`


![Tensorboard_1](https://user-images.githubusercontent.com/106902414/175007299-51d16572-5d38-4b4d-8d8c-e1e39d746ed8.png)


### Discussion
1) 

### Credits
`Dataset`
HackerEarth HackLive: Customer Segmentation | Kaggle
https://www.kaggle.com/datasets/kunalgupta2616/hackerearth-customer-segmentation-hackathon
