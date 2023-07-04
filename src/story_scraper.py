from instaloader import *
import time



def getStory(scraper, test_profile):
    for stories in scraper.get_stories(userids=[test_profile.userid]):
        for story in stories.get_items():
            scraper.download_storyitem(story, f"{test_profile.username}_stories")
        time.sleep(5)


def main():
    scraper = instaloader.Instaloader()
    scraper.load_session_from_file(input("Enter your username: "))
    test_profile = instaloader.Profile.from_username(scraper.context, input("Enter the username of the profile you want to scrape: "))
   

    getStory(scraper, test_profile)


if __name__ == "__main__":
    main()
