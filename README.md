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

![model_3](https://user-images.githubusercontent.com/106902414/175003917-3ac39209-45a0-4894-9f35-0a056a7d0016.png)




`Classification_Report`

![f1 score](https://user-images.githubusercontent.com/106902414/175004436-260b9566-a4a7-4578-a785-f2333b501464.PNG)

`Confusion_Matrix` 

![ConfusionMatrixDisplay](https://user-images.githubusercontent.com/106902414/175004527-3722b3e2-f625-44fd-b91c-b363220538cd.png)


`Training Data` example for continuous data:

![customer_age](https://user-images.githubusercontent.com/106902414/175004568-a3edd933-508c-4a2a-a5ee-ebaada1ba076.png)


`Training Data` example for categorical data:
![education](https://user-images.githubusercontent.com/106902414/175004598-fd6bbe31-996f-4619-8256-f5516b83e739.png)

`Training Data` example for relationship between the features and the target:

![term_deposit vs communication_type](https://user-images.githubusercontent.com/106902414/175004781-29392a9e-04cd-4a45-a6a4-2be37773e89f.png)

### Discussion
1) 

### Credits
`Dataset`
HackerEarth HackLive: Customer Segmentation | Kaggle
https://www.kaggle.com/datasets/kunalgupta2616/hackerearth-customer-segmentation-hackathon
