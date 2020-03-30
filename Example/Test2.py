from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

#This is used to test two different searches
#And how the progress bar interacts
response().download('Nemo,Dory', 50)
