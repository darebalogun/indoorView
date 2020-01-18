# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

#Directory name
folder_name= "IndoorView_Images"
save_location = "/home/pi/Desktop/"+ folder_name

# Function to rename multiple files 
def main(): 
	i = 1
	
	for filename in os.listdir(save_location): 
		dst ="image_" + str(i) + ".jpg"
		src = save_location + "/" +filename 
		dst = save_location + "/" +dst 
		
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
		i += 1

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
