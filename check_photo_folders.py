#! python3
"""
check_photo_folders.py will scan all folders from current working directory and report if they are primarily photo
folders. Criteria: more than 50% of the files are photos, the height and width of the photo are greater than 500px.
"""

import os
from PIL import Image
import win_unicode_console

win_unicode_console.enable()

photo_folder_list = []
photo_file_extensions = ('.jpg', '.jpeg', '.png')
min_img_size = 500


for filefolders, subfolders, filenames in os.walk('.'):
    num_photo_files = 0
    num_non_photo_files = 0

    # if not filenames:
    #     continue  # skip directories with 0 files. Empty lists are False.

    for file in filenames:
        if not file.lower().endswith(photo_file_extensions):
            num_non_photo_files += 1
            continue
        else:

            try:
                im = Image.open(os.path.join(filefolders, file))
                width, height = im.size
            except OSError as err:
                print(err)
                continue

            if width < min_img_size or height < min_img_size:
                continue
            else:
                num_photo_files += 1

    total_files = num_photo_files + num_non_photo_files
    if total_files == 0:
        continue  # skip directories with 0 files.
    image_ratio = num_photo_files / total_files
    if image_ratio > 0.5:
        photo_folder_list.append((num_photo_files, os.path.abspath(filefolders)))
        # print('No. of Photos is {}.'.format(num_photo_files), end='   ')
        # print(os.path.abspath(filefolders))

photo_folder_list.sort(reverse=True)  # print me a list of items with most to least photos
for item in photo_folder_list:
    print(item)

win_unicode_console.disable()
