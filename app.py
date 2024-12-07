# app.py  
from flask import Flask, request, jsonify  
from data_fetcher import fetch_all_data  
from data_preprocessing import preprocess_all_data  
from recommendation import hybrid_recommendations  
from user_data import get_user_id, get_user_viewed_posts, get_user_interactions  

app = Flask(__name__)  

# Define headers for API requests  
headers = {  
    "Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"  
}  

# Fetch and preprocess data  
data = fetch_all_data(headers)  
preprocessed_data = preprocess_all_data(data)  
all_posts_df = preprocessed_data["all_posts"]  
all_users_df = preprocessed_data["all_users"]  
viewed_df = preprocessed_data["viewed"]  
liked_df = preprocessed_data["liked"]  
inspired_df = preprocessed_data["inspired"]  
rated_df = preprocessed_data["rated"]  

# Debugging: Print the structure of all_users_df  
print("All Users DataFrame:")  
print(all_users_df.head())  # Print the first few rows of the DataFrame  
print(all_users_df.columns)  # Print the column names  

@app.route('/feed', methods=['GET'])  
def get_recommendations():  
    username = request.args.get('username')  
    category_id = request.args.get('category_id', None)  
    mood = request.args.get('mood', None)  

    # Fetch user data and interactions based on username  
    user_id = get_user_id(username, all_users_df)  # Get user ID  
    if user_id is None:  
        return jsonify({"error": "User not found"}), 404  

    user_viewed_posts = get_user_viewed_posts(user_id, viewed_df)  # Get viewed posts  
    user_interactions = get_user_interactions(user_id, all_posts_df, liked_df, inspired_df, rated_df)  # Get all interactions  

    recommendations = hybrid_recommendations(user_viewed_posts, user_interactions, all_posts_df)  

    return jsonify(recommendations.to_dict(orient='records'))  

if __name__ == '__main__':  
    app.run(port=5000, debug=True)  