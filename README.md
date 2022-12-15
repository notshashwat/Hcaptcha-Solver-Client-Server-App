dependencies:

install opencv by:

$pip install opencv-python


how to use:
put the image you want to predict './imgs' folder 
the image can be any of  ['airplane', 'bicycle', 'boat', 'motorbus', 'motorcycle', 'seaplane', 'truck']
example images can be found in ./example images



the code will automatically work with the latest image in the ./imgs folder


$python3 server.py

(please wait some time after [LISTENING] appears before running the client)

$python3 client.py

The output is recived by the client which tells what the captcha image was of 