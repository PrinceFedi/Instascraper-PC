import os
import re
from openpyxl import Workbook


wb = Workbook()
ws = wb.active
ws.title = "Summary"

headers = ["Date_of_Post", "Caption", "Likes", "Comment_count", "Comments"]
ws.append(headers)


folder_path = input("Please enter the path to the parent folder of where you saved all the profiles' info: ")
pattern_lc = re.compile(r'like_count') # lc stands for like and comment count
pattern_caption = re.compile(r'UTC.txt')
pattern_comments = re.compile(r'comments')

#filesnames = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]
#filesnames.sort(reverse=True)
for filename in os.listdir(folder_path):
    # if filename.endswith('.txt'): # comment this code out to see every picture
            
    file_path = os.path.join(folder_path, filename)
    file_name_like_count = os.path.splitext(filename)[0]

    caption, like_count, comment_count, comments = None, None, None, None

    if pattern_lc.search(file_name_like_count):
        with open(file_path, "r") as file:
            lines = file.readlines()

        like_count = lines[0].strip() if len(lines) > 0 else None
        comment_count =  lines[1].strip() if len(lines) > 1 else None

    if pattern_caption.search(filename):
        with open(file_path, "r") as caption_file:
            caption = caption_file.readlines()
            caption = "".join(caption)

    if pattern_comments.search(filename):
        with open(file_path, "r") as comment_file:
            comments = comment_file.readlines()
            comments = "".join(comments)


    ws.append([file_name_like_count, caption, like_count, comment_count, comments])


output_file = output_file = input('Please enter the desired name for your CSV file (for example, "my_data.xlsx"): ')
wb.save(output_file)
print("IT works: ", output_file)

