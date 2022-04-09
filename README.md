# credit_card_default_prediction

# Problem Statement
Financial threats are displaying a trend about the credit risk of commercial banks as the
incredible improvement in the financial industry has arisen. In this way, one of the
biggest threats faces by commercial banks is the risk prediction of credit clients. The
goal is to predict the probability of credit default based on credit card owner's
characteristics and payment history. This is a binary classification

# Data

Data was taken from Kaggle. Here is the link- https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset

The Data was quite clean, with 30,000 entries. Not much of processing was required.This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.
There are 25 variables:
ID: ID of each client
LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
SEX: Gender (1=male, 2=female)
EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
MARRIAGE: Marital status (1=married, 2=single, 3=others)
AGE: Age in years
PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
PAY_2: Repayment status in August, 2005 (scale same as above)
PAY_3: Repayment status in July, 2005 (scale same as above)
PAY_4: Repayment status in June, 2005 (scale same as above)
PAY_5: Repayment status in May, 2005 (scale same as above)
PAY_6: Repayment status in April, 2005 (scale same as above)
BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
default.payment.next.month: Default payment (1=yes, 0=no)

# Preprocsseing and Clustering
The Dataset was quite clean fortunately. The only thing that was needed to be taken care of were 3 features. ID, EDUCATION and MARRIAGE
ID didn't have any relevance to our Target variable. So we dropped it.

EDUCATION and Marriage didn't have the correct order, encoding wasn't accurate enough to quantify the categories in them. Hence we one hot encoded them.
I divided the datasets into clusters and trained separate models for each cluster for better results. Used Kmeans clustering for clustering.
# Model Building 
Tested it one core algorithm and one bagging algorithm. Random forest classifier and KNN. The metric i used for AUC Score, KNN suprisingly performed better. I am still shocked regarding this, feel free to drop in any thoughts about this. KNN had an AUC of 71,72, 77 for respective clusters whereas for RF it was 65,70,73.
# Model Deployment 
Used Streamlit and Heroku to deploy. Streamlit is a fantastic library for UI. Prediction input was taken in form of test csv. And output was stored in the folder. 

# Conclusion

Overall, good beginner problem. But we can do more on it's variation. Like finding out what factors effect the Credit, what are the various key point indicators while calcualting someone's credit limit.
