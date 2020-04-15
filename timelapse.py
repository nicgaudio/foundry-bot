#Timelapse script for 3D print captures
#Run on Raspberry pi

#Import peripheral modules
# from picamera import PiCamera
import dropbox
from dotenv import load_dotenv

#Standard imports
import os
from os import system
import argparse
from time import sleep
import logging as log

#Load .env
load_dotenv()

# #Define arg parser and arguments
# parser = argparse.ArgumentParser(description='Parser to define timelapse capture parameters')
# parser.add_argument('-p', help="Pass the directory name for the images to be written to (typically the print name).", dest='img_out_path', required=True)
# parser.add_argument('-t', help="Pass the estimated time of the print in 'DD:HH:MM:SS' format.", dest='print_time_est', required=True)
# args = parser.parse_args()

#Get Dropbox envs and instantiate class obj
DB_ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')
DB_OUTPUT_PATH = os.getenv('DROPBOX_OUTPUT_PATH')
dbx = dropbox.Dropbox(DB_ACCESS_TOKEN)
print(DB_ACCESS_TOKEN)
print(DB_OUTPUT_PATH)

# #Display useful info
# print('Image filepath: {}'.format(args.img_out_path))
# print('Print time: {}'.format(args.print_time_est))

# #Get args
# img_out_path = args.img_out_path
# print_time_est = args.print_time_est

# #Check if output directory exists. If not, create it!
# if not os.path.exists(img_out_path):
#     print('')
#     print('Output path {} does not exist. Creating it!'.format(img_out_path))
#     os.mkdir(img_out_path)

# camera = PiCamera()
# camera.resolution = (1024, 768)

# for i in range(500):
#     camera.capture('{0}/{1}_{2:04d}.jpg'.format(img_out_path, img_out_path, i))
#     print('Image {0}_{1:04d}.jpg saved to {0}/{0}_{1:04d}.jpg'.format(img_out_path, i))
#     sleep(30)

# print('')
# print('Converting images to .gif. This may take a moment')
# gif_filename = '{0}/{0}.gif'.format(img_out_path)
# system('convert -delay 10 -loop 0 {0}/{0}*.jpg {1}'.format(img_out_path, gif_filename))

# print('')
# print('Uploading file {} to Dropbox.'.format(gif_filename))
# with open(gif_filename) as f:
#     dbx.files_upload(f.read(), '{0}/{1}'.format(DB_OUTPUT_PATH, gif_filename))

# print('')
# print('Finished upload!')
