# GAN-based-data-augmentation-for-improved-hate-speech-detection
SeqGAN data augmentation is used for improved hate speech detection, and we use the SMOTE oversampling method as the baseline. We also use four trained classifier-SVM,LSTM,BERT,Logistic regression.
# Requirments
* Tensorflow 1.15.0
* Python 3.7
# Classification model
If you want to use the classification model, click directly on the __classificaition model__ folder, in which you will see two __.ipynb__ files, containing all 4 classification models. The training set, test set, and validation set in csv format used in the model can be seen in the __data set__ folder.
# SMOTE Oversampling
If you want to achieve SMOTE oversampling, you only need to open the __SMOTE Oversamling__ folder. There are also two __.ipynb__ files in it, which are the results of the 4 classification models after the SMOTE algorithm. Click on any file, you can see the specific method of implementing SMOTE.It should be noted that the SMOTE algorithm can only be used for unbalanced data sets.
