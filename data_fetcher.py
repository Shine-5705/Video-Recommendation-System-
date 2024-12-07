# data_fetcher.py  
import requests  

def fetch_data(url, headers):  
    data = []  
    page = 1  
    while True:  
        response = requests.get(f"{url}&page={page}&page_size=1000", headers=headers)  
        print(f"Fetching data from {url} - Page {page}: Status Code {response.status_code}")  # Debugging line  
        if response.status_code != 200:  
            print(f"Error fetching data: {response.text}")  # Print error message  
            break  
        page_data = response.json()  
        if not page_data:  # Break if no more data  
            break  
        data.extend(page_data)  
        page += 1  
    return data  

def fetch_all_data(headers):  
    viewed_posts = fetch_data("https://api.socialverseapp.com/posts/view", headers)  
    liked_posts = fetch_data("https://api.socialverseapp.com/posts/like", headers)  
    inspired_posts = fetch_data("https://api.socialverseapp.com/posts/inspire", headers)  
    rated_posts = fetch_data("https://api.socialverseapp.com/posts/rating", headers)  
    all_posts = fetch_data("https://api.socialverseapp.com/posts/summary/get", headers)  
    all_users = fetch_data("https://api.socialverseapp.com/users/get_all", headers)  

    print("Fetched Data Summary:")  # Debugging line  
    print(f"Viewed Posts: {len(viewed_posts)}")  
    print(f"Liked Posts: {len(liked_posts)}")  
    print(f"Inspired Posts: {len(inspired_posts)}")  
    print(f"Rated Posts: {len(rated_posts)}")  
    print(f"All Posts: {len(all_posts)}")  
    print(f"All Users: {len(all_users)}")  # Print number of users fetched  

    return {  
        "viewed": viewed_posts,  
        "liked": liked_posts,  
        "inspired": inspired_posts,  
        "rated": rated_posts,  
        "all_posts": all_posts,  
        "all_users": all_users  
    }  