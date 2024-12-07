# evaluation.py  
from sklearn.metrics import mean_absolute_error, mean_squared_error  
import numpy as np  

def evaluate_recommendations(true_ratings, predicted_ratings):  
    mae = mean_absolute_error(true_ratings, predicted_ratings)  
    rmse = np.sqrt(mean_squared_error(true_ratings, predicted_ratings))  
    return mae, rmse  