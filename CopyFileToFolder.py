import shutil
import os
import pandas

src="SOURCE OF DIRECTORY WHERE YOU WANT TO SEARCH"              #example: D:\demo
dest_1="DESTINATION DIRECTORY WHERE YOU WANT TO COPY THAT FILE FOR CLASS 1"   #example: D:\DemoCopy
dest_0="DESTINATION DIRECTORY WHERE YOU WANT TO COPY THAT FILE FOR CLASS 0"   #example: D:\DemoCopy
search_dataset_file="CSV DATASET THAT CONTAINS THE FILENAME TO BE SEARCHED"      #example: "Dataset.csv"
search_success_count=0  # number of file that have been successfully searched
search_target_count=0   # targeted number of file to be searched
extension="jpg"         #example: "jpg, png..."
index=0                 #index of dataset

try:
    os.makedirs(dest_1)
    os.makedirs(dest_0)
except:
    print("ALREADY EXISTING")

#Recursive Fuction to Check the file in each Folder
def checkFile(src,search_dataset_file,extension):
    global search_success_count, search_target_count, index
    #listDir returns all files and folder within the src in src_file
    src_file = os.listdir(src)

    # read filename dataset to be searched from csv file
    data = pandas.read_csv(search_dataset_file)
    # read only the filename with the title 'id' into dataframe
    search_id=data["id"]
    search_class=data['class']
     # convert from dataframe to list  
    search_dataset=search_id.values.tolist()
    search_class=search_class.values.tolist()
    # number of targeted searching file
    search_target_count=len(search_dataset)

    # loop through filename in the search dataset
    for search_file_name in search_dataset:
        # join filename and extension
        joiner='.'
        full_search_file_name=joiner.join([str(search_file_name),extension])
        # full path of search image
        full_search_file_name_path=os.path.join(src,full_search_file_name)

        # check the class of the image
        if (search_class[index] == 1):
            # check if file already exist in the destination folder
            if (os.path.isfile(os.path.join(dest_1,full_search_file_name))==False):
                # try to copy if file exist in the source folder
                try:
                    # Copy the file to the destination folder class 1
                    shutil.copy(full_search_file_name_path, dest_1)
                    # display string
                    string_to_disp=''.join(["Copy ",full_search_file_name," to \early"])
                    print(string_to_disp)
                    # increment of file count    
                    search_success_count += 1
                # if file does not exist in source folder
                except:
                    print("File not exist")        
            else:
                print("File already exist")          
        elif (search_class[index] == 0):
            # check if file already exist in the destination folder
            if (os.path.isfile(os.path.join(dest_0,full_search_file_name))==False):
                # try to copy if file exist in the source folder     
                try:
                    # Copy the file to the destination folder class 0
                    shutil.copy(full_search_file_name_path, dest_0)
                    # display string
                    string_to_disp=''.join(["Copy ",full_search_file_name," to \late"])
                    print(string_to_disp)    
                    # increment of file count                
                    search_success_count += 1
                except:
                    print("File not exist")
            # if file does not exist in source folder
            else:
                print("File already exist")         
             
        index += 1

checkFile(src,search_dataset_file,extension)

#count of targeted searching file
print("Count of targeted searching file: ", search_target_count)

#COUNT OF TOTAL FILES
print("Count of file that have been successfully searched",search_success_count)

#compare targeted and final searching count
if (search_target_count == search_success_count):
    print("All files have been successfully searched")
else:
    print("There are files that have not been successfully searched")


