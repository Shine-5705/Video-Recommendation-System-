from data_fetcher import fetch_all_data  

def get_user_id(username, all_users_df):  
    """Fetch user ID based on username."""  
    user = all_users_df[all_users_df['user_name'] == username]  # Adjusted column name  
    if not user.empty:  
        return user.iloc[0]['id']  
    return None  

def get_user_viewed_posts(user_id, viewed_df):  
    """Fetch viewed posts for a specific user."""  
    user_viewed = viewed_df[viewed_df['user_id'] == user_id]  
    return user_viewed['post_id'].tolist()  

def get_user_interactions(user_id, all_posts_df, liked_df, inspired_df, rated_df):  
    """Fetch all interactions for a specific user."""  
    interactions = []  

    # Liked posts  
    liked_posts = liked_df[liked_df['user_id'] == user_id]  
    interactions.extend(liked_posts[['post_id', 'interaction_type']].assign(interaction_type='like').to_dict(orient='records'))  

    # Inspired posts  
    inspired_posts = inspired_df[inspired_df['user_id'] == user_id]  
    interactions.extend(inspired_posts[['post_id', 'interaction_type']].assign(interaction_type='inspire').to_dict(orient='records'))  

    # Rated posts  
    rated_posts = rated_df[rated_df['user_id'] == user_id]  
    interactions.extend(rated_posts[['post_id', 'interaction_type']].assign(interaction_type='rate').to_dict(orient='records'))  

    return interactions  