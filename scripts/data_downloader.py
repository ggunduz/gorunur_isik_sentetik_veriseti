import urllib.request
import zipfile
from urllib.request import urlretrieve

annotations_url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
trail_url = "http://images.cocodataset.org/zips/train2017.zip"
validation_url = "http://images.cocodataset.org/zips/val2017.zip"

# 1) Download Annotations file and unzip
print('Downloading annotaton file...')
urlretrieve(annotations_url, "../data/annotations_trainval2017.zip")

print('Unzipping annotaton file...')
with zipfile.ZipFile("../data/annotations_trainval2017.zip","r") as zip_ref:
    zip_ref.extractall("../data/annotations_trainval2017")

# 2) Download training file and unzip
print('Downloading training file...')
urlretrieve(trail_url, "../data/train2017.zip")

print('Unzipping training file...')
with zipfile.ZipFile("../data/train2017.zip","r") as zip_ref:
    zip_ref.extractall("../data/train2017")

# 3) Download validation file and unzip
print('Downloading validation file...')
urlretrieve(validation_url, "../data/val2017.zip")

print('Unzipping validation file...')
with zipfile.ZipFile("../data/val2017.zip","r") as zip_ref:
    zip_ref.extractall("../data/val2017")