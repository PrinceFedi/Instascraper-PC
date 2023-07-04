from instaloader import *
import time

def getHighlights(scraper, test_profile):
    for highlight in scraper.get_highlights(test_profile):
        for item in highlight.get_items():
            scraper.download_storyitem(item, f"{test_profile.username}_highlights_{highlight.title}")




def main():
    scraper = instaloader.Instaloader()
    scraper.load_session_from_file(input("Enter your username: "))
    test_profile = instaloader.Profile.from_username(scraper.context, input("Enter the username of the profile you want to scrape: "))
   
    getHighlights(scraper, test_profile)
    


if __name__ == "__main__":
    main()

