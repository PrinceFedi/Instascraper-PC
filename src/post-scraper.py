
from datetime import datetime
import os
import time
import re

from instaloader import *

KEYWORDS = []

# This is an example of the keywords you can use to filter which post you want to scrape
# KEYWORDS = [
#     "environment", "sustainability", "environmental", "sustainable",
#     "climate", "pollution", "recycling", "water", "soil", "sufficiency", "farmland",
#     "land", "water quality", "soil quality", "land quality"
# ]

def contains_keywords(text, keywords):
    # Convert to lower case for case insensitive search
    pattern = r'\b(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b'
    # Search for the pattern in the text and return all matches
    matched_keywords = re.findall(pattern, text, flags=re.IGNORECASE)
    return matched_keywords

def getPost(scraper, test_profile, folder_path):
    
    # modify this to choose the exact date you want to scrape the profiles
    start_date = datetime(2024, 1, 1)  # Start date
    end_date = datetime(2024, 1, 2)  # End date

    for post in test_profile.get_posts():
        
        post_date = post.date_utc  # Get the date of the post
        # Check if the post date is within the desired date range

        if start_date <= post_date <= end_date:

            # Check if the post caption contains any of the keywords
            matched_keywords = contains_keywords(post.caption, KEYWORDS) if post.caption else []
            if matched_keywords:
                downloaded = scraper.download_post(post, target=test_profile.username)
                if downloaded:
                    print("Contains keywords:", ', '.join(matched_keywords), " - Downloading post...")
                    expanded_folder_path = os.path.expanduser(folder_path)

                    # Creation of the like/comment count and comments txt files
                    with open(f"{expanded_folder_path}/{post.date}_like_count.txt", 'w+') as file:
                        print(f"Like_count: {post.likes}\n" f"Comment count: {post.comments}", file=file) # if like count is -1 they hid there likes
                    comments = []
                    for comment in post.get_comments():
                        comments.append(f"{comment.owner.username}: {comment.text}\n")  
                    with open(f"{expanded_folder_path}/{post.date}_comments.txt", "w") as f:
                        f.writelines(comments)          
                    time.sleep(20)
            

def main():
    scraper = instaloader.Instaloader()
    
     # Ask for the Instaloader session username
    session_username = input("Enter your profile's username for the session: ")
    scraper.load_session_from_file(session_username)
    
     # Ask for the username of the profile you want to scrape
    profile_to_scrape = input("Enter the username of the profile you want to scrape: ")

    # Get the current working directory (which should be the src directory)
    current_working_directory = os.getcwd()

    # Then append the profile's username directory to the working directory
    folder_path = os.path.join(current_working_directory, profile_to_scrape)
    
    # Pass the folder path and the profile to scrape to the getPost function
    test_profile = instaloader.Profile.from_username(scraper.context, profile_to_scrape)
    
    getPost(scraper, test_profile, folder_path)


if __name__ == "__main__":
    main()









