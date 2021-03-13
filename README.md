# GAN-based-data-augmentation-for-improved-hate-speech-detection
SeqGAN data augmentation is used for improved hate speech detection, and we use the SMOTE oversampling method as the baseline. We also use four trained classifier-SVM,LSTM,BERT,Logistic regression.
# Requirments
* Tensorflow 1.15.0
* Python 3.7
# Classification model
If you want to use the classification model, click directly on the __classificaition model__ folder, in which you will see two __.ipynb__ files, containing all 4 classification models. The training set, test set, and validation set in __.csv__ format used in the model can be seen in the __data set__ folder.
# SMOTE Oversampling
If you want to achieve SMOTE oversampling, you only need to open the __SMOTE Oversamling__ folder. There are also two __.ipynb__ files in it, which are the results of the 4 classification models after the SMOTE algorithm. Click on any file, you can see the specific method of implementing SMOTE.It should be noted that the SMOTE algorithm can only be used for unbalanced data sets.
# Use SeqGAN to generate hate speech
* Extract hate speech in the dataset <br />
  Because we want to generate hate speech, we need to use hate speech to train the generator in SeqGAN. However, our data set contains both hate speech and non-hate speech, so the first step is to extract the hate speech in the data set. the way is:In the __SeqGAN__ folder, __train.txt__ is the original data set file, and we can see a __script.py__ python file. Running this file can extract all the hate speech in train.txt and put it in __train_set.txt__ File.
* Adjustment parameters <br />
Also in the SeqGAN folder, we can adjust the parameters in the __config.ini__ file, such as the number of generated hate speech, the number of Monte Carlo searches, the maximum sentence length, the number of epochs, and so on.__(Here you need to pay attention to the path of the opened file and the path where the file is stored, which may be different.)__ Try not to change other files.
* Run the SeqGAN model <br /> 
In order to run the SeqGAN model, just run __main.py__.
* Generated hate speech  <br />
The generated hate speech will be stored in the __generated_sentences.txt__ file.
# SeqGAN based data augmentation 
We tag the generated hate speech and put it in the original data set to achieve data augmentation. After importing the data-augmentaed data set into 4 classification models, the classification results are obtained. Thus, the impact of data augmentation based on SeqGAN on the performance of hate speech detection can be observed.
