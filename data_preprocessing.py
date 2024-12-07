# data_preprocessing.py  
import pandas as pd  

def preprocess_data(posts):  
    df = pd.DataFrame(posts)  
    df.dropna(inplace=True)  # Remove missing values  
    # Normalize numerical features if necessary  
    return df  

def preprocess_all_data(data):  
    return {  
        "viewed": preprocess_data(data["viewed"]),  
        "liked": preprocess_data(data["liked"]),  
        "inspired": preprocess_data(data["inspired"]),  
        "rated": preprocess_data(data["rated"]),  
        "all_posts": preprocess_data(data["all_posts"]),  
        "all_users": preprocess_data(data["all_users"])  
    }  