Welcome to Heart Failure Prediction capstone project! 

The Heat Failure Dataset used for prediction was taken from UCI Machine Learning Repository. There are 11 features encompassing 6 categorical features and 5 continuous features with a binary output of whether the patient is diagnosed with heart failure with 1190 instances.

The aim of this Capstone project is as follow:
1. To find out the machine/deep learning algorithms that yield acceptable results.
2. To implement the models found in step 1 in a stacked ensemble to produce a reinforced meta-learner.
3. To obtain the HIGHEST achievable accuracy, sensitivity, specificity and matthew Correlation Coefficient (MCC).
4. To identify the quality features that are crucial to the predicitive models via feature reselection procedure.
5. To deploy the model onto Heroku (web application).
6. To deploy the model onto Glide via the web app created (mobile application).


Methodology
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
The idea of a stacked ensemble is to gather a bunch of insights, observations and inferences ovbtained from an array of ML/DL models (acting as the base learners in layer 1) and pass it to a DL model (acting as the reinforced meta-learner in layer 2)

Models Selected as Base Learners:
Extra Trees Classifier
Random Forest Classifier
Support Vector Machine (Linear)
Support Vector Machine (RBF)
Adaptive Boost Classifier
Gradient Boosting Classifier                                                       
XG Boost
Multiple Learning Perceptron

Reinforced Meta-Learner:
Multiple Learning Perceptron
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The stacked classifier is evaluated according to accuracy, sensitivity, specificity and MCC.

Feature Reselection is done through SHAP analysis and PDP plot along with a few statistical coefficients to identify the impact of each individual feature to the model outcome.

Web App: https://health-prediction-heart.herokuapp.com
Mobile App: https://tired-street-7279.glideapp.io/
