import shutil
import os
import pandas

src="SOURCE OF DIRECTORY WHERE YOU WANT TO SEARCH"              #example: D:\demo
search_dataset_file="CSV DATASET THAT CONTAINS THE FILENAME TO BE SEARCHED"      #example: "Dataset.csv"
log_file_path="TXT FILE WHERE THE LOG MESSAGE WILL BE WRITTEN"
search_success_count=0      # number of file that have been successfully searched
search_target_count=0       # targeted number of file to be searched
extension="jpg"             # example: "jpg, png..."
index=0                     # index of dataset
strClass=["Early","Late"]   # string of class

# create file for logging
log_file = open(log_file_path,"w")

try:
    os.makedirs(dest_1)
    os.makedirs(dest_0)
except:
    print("ALREADY EXISTING")

#Recursive Fuction to Check the file in each Folder
def checkFile(src,search_dataset_file,extension):
    global search_success_count, search_target_count, index, log_file
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

        # message to displays
        string_to_disp=""
        # check if file exist
        if (os.path.isfile(full_search_file_name_path)==True):
            string_to_disp=''.join([strClass[search_class[index]],": ", full_search_file_name, " exists"])
            # increment of number of file that sucessfully been searched
            search_success_count+=1
        else:
            string_to_disp=''.join([strClass[search_class[index]],": ", full_search_file_name, " does not exist"])
        # print the message
        print(string_to_disp)
        # log message to file
        log_file.write(string_to_disp)
        log_file.write("\n")

checkFile(src,search_dataset_file,extension)
# close log file
log_file.close()

#count of targeted searching file
print("Count of targeted searching file: ", search_target_count)

#COUNT OF TOTAL FILES
print("Count of file that have been successfully searched",search_success_count)

#compare targeted and final searching count
if (search_target_count == search_success_count):
    print("All files have been successfully searched")
else:
    print("There are files that have not been successfully searched")
