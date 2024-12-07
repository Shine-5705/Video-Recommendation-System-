# recommendation.py  
import pandas as pd  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import linear_kernel  
from sklearn.metrics.pairwise import cosine_similarity  

def content_based_recommendations(user_viewed_posts, all_posts_df):  
    tfidf = TfidfVectorizer(stop_words='english')  
    all_posts_df['content'] = all_posts_df['title'] + ' ' + all_posts_df['description']  
    tfidf_matrix = tfidf.fit_transform(all_posts_df['content'])  

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)  

    indices = pd.Series(all_posts_df.index, index=all_posts_df['id']).drop_duplicates()  

    user_indices = [indices[post_id] for post_id in user_viewed_posts if post_id in indices]  

    sim_scores = list(enumerate(cosine_sim[user_indices].mean(axis=0)))  
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  

    recommended_indices = [i[0] for i in sim_scores[:10]]  
    return all_posts_df.iloc[recommended_indices]  

def collaborative_filtering(user_id, user_interactions, all_posts_df):  
    user_item_matrix = pd.pivot_table(user_interactions, index='user_id', columns='post_id', values='interaction_type', fill_value=0)  
    user_similarity = cosine_similarity(user_item_matrix)  

    user_index = user_item_matrix.index.get_loc(user_id)  

    similar_users = list(enumerate(user_similarity[user_index]))  
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:11]  

    recommended_posts = set()  
    for similar_user in similar_users:  
        similar_user_id = user_item_matrix.index[similar_user[0]]  
        posts = user_item_matrix.loc[similar_user_id][user_item_matrix.loc[similar_user_id] > 0].index  
        recommended_posts.update(posts)  

    return all_posts_df[all_posts_df['id'].isin(recommended_posts)].head(10)  

def hybrid_recommendations(user_viewed_posts, user_interactions, all_posts_df):  
    content_recommendations = content_based_recommendations(user_viewed_posts, all_posts_df)  
    collaborative_recommendations = collaborative_filtering(user_interactions, all_posts_df)  

    combined_recommendations = pd.concat([content_recommendations, collaborative_recommendations]).drop_duplicates()  
    return combined_recommendations.head(10)  