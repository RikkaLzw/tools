import os

folder_path = 'F:\\Python\\python_test\\datasets\\RE'

for filename in os.listdir(folder_path):
    if filename.endswith(".dot"):
        filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, 'no_' + filename)
        os.rename(filepath, new_filepath)

