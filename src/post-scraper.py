
from instaloader import *
import time

folder_path = input("Enter the path to the folder which is tilted the username you want to save the files to, Ex: ~/INSTASCRAPER-PC/username: ")

def getPost(scraper, test_profile):
    for post in test_profile.get_posts():
        scraper.download_post(post, target=test_profile.username)
        # Make sure to change the username to the folder name of the profile you want.
        # Example: princefedi_ has all of Fedi's post
        with open(f"{folder_path}/{post.date}_like_count.txt", 'w') as file:
            print(f"Like_count: {post.likes}\n" f"Comment count: {post.comments}", file=file) # if like count is -1 they hid there likes
        comments = []
        for comment in post.get_comments():
            comments.append(f"{comment.owner.username}: {comment.text}\n") 
        # Make sure to change the username to the folder name of the profile you want.
        # Example: princefedi_ has all of Fedi's post so thats why its in front of Thesis_Project
        with open(f"{folder_path}/{post.date}_comments.txt", "w") as f:
            f.writelines(comments)
        
        time.sleep(20)


def main():
    scraper = instaloader.Instaloader()
    scraper.load_session_from_file(input("Enter your username: "))
    # To run this just change the username at the end of the test profile statement
    # scraper.context, 'princefedi') -> scraper.context, any username)
    test_profile = instaloader.Profile.from_username(scraper.context, input("Enter the username of the profile you want to scrape: "))
   
    getPost(scraper, test_profile)
    


if __name__ == "__main__":
    main()









