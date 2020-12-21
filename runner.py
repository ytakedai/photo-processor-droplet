from os.path import isfile, join
from os import listdir
import os
import time
from time import ctime
import datetime

FILEPATH_DROPLET = '/Users/ytakedai/Desktop/PhotoProcessor.app/'
FILEPATH_PHOTOS = '/Users/ytakedai/Desktop/RAW-to-JPG/'
FILEPATH_FINAL_DESTINATION = '/Users/ytakedai/Google\ Drive/Personal/Photos/Sony+Nikon/Uploads\ \(Macbook\ Pro\)'
FILEPATH_DROPLET_DESTINATION = '/Users/ytakedai/Desktop/RAW-to-JPG/JPEG/'

def main():

    files = [f for f in listdir(FILEPATH_PHOTOS)
            if isfile(join(FILEPATH_PHOTOS, f)) and '.' != f[0]]

    if len(files) == 0:
        print('ERROR: No files found')
        quit()
    files[0]
    # Get date of first original photo for destination folder name
    timestamp = ctime(os.path.getctime('{0}/{1}'.format(FILEPATH_PHOTOS, files[0])))
    timestamp_list = timestamp.split()
    month = timestamp_list[1]
    day = timestamp_list[2]
    # time = timestamp_list[3]  NAME OVERLAPS WITH PACKAGE, NOT USED
    year = timestamp_list[4]
    date = '{0}_{1}_{2}'.format(year, month_to_num[month], day)

    # Run Droplet on photos
    print('{0} Opening Photoshop and running Droplet'.format(datetime.datetime.now()))
    os.system('open -a {0} {1}'.format(FILEPATH_DROPLET ,FILEPATH_PHOTOS))

    # Check for photoshop to be done
    num_files = len(files)
    done = False
    while not done:
        print('{0} Waiting for Photoshop to finish'.format(datetime.datetime.now()))
        files_droplet_destination = [f for f in listdir(FILEPATH_DROPLET_DESTINATION)
                             if isfile(join(FILEPATH_DROPLET_DESTINATION, f)) and '.' != f[0]]
        if len(files_droplet_destination) == len(files):
            done = True
        else:
            time.sleep(30)
    # Copy files to folder
    print('{0} Copying files to destination'.format(datetime.datetime.now()))
    os.system('mkdir {0}/{1}'.format(FILEPATH_FINAL_DESTINATION, date))
    os.system('cp -a {0}/* {1}/{2}/'.format(FILEPATH_PHOTOS,
                                    FILEPATH_FINAL_DESTINATION, date))

    print('{0} Finished! Photos are ready for upload'.format(datetime.datetime.now()))

month_to_num = {
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
}

main()
