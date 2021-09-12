import shutil
import os
import pandas

src="D:\\Master\\Galaxy Zoo dataset\\images_gz2\\images"              #example: D:\demo
dest_1=""   #example: D:\DemoCopy
dest_0=""   #example: D:\DemoCopy
dest_path="D:\\Master\\Galaxy Zoo dataset\\Dataset\\Dataset multiclass 10\\"
search_dataset_file="D:\\Master\\Galaxy Zoo dataset\\CSV\\Dataset multiclass 10\\late_face on_no bar_no spiral-dataset.csv"      #example: "Dataset.csv"
search_success_count=0  # number of file that have been successfully searched
search_target_count=0   # targeted number of file to be searched
extension="jpg"         #example: "jpg, png..."
index=0                 #index of dataset

class_num=10
class_idx=[]
dest_class_name=[]
dest_class_path=[]

for x in range(class_num):
    class_idx.append(x)
    dest_class_name.append("class"+str(x))
    dest_class_path.append(os.path.join(dest_path,dest_class_name[x]))
    try:
        os.makedirs(dest_class_path[x])
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
        # if (search_class[index] == 1):
        # check if file already exist in the destination folder
        if (os.path.isfile(os.path.join(dest_class_path[search_class[index]],full_search_file_name))==False):
            # try to copy if file exist in the source folder
            try:
                # Copy the file to the destination folder class 1
                shutil.copy(full_search_file_name_path, dest_class_path[search_class[index]])
                # display string
                string_to_disp=''.join(["Copy ",full_search_file_name," to /",dest_class_name[search_class[index]]])
                print(string_to_disp)
                # increment of file count    
                search_success_count += 1
            # if file does not exist in source folder
            except:
                print("File not exist")        
        else:
            print("File already exist")          
        # elif (search_class[index] == 0):
        #     # check if file already exist in the destination folder
        #     if (os.path.isfile(os.path.join(dest_0,full_search_file_name))==False):
        #         # try to copy if file exist in the source folder     
        #         try:
        #             # Copy the file to the destination folder class 0
        #             shutil.copy(full_search_file_name_path, dest_0)
        #             # display string
        #             string_to_disp=''.join(["Copy ",full_search_file_name," to \late"])
        #             print(string_to_disp)    
        #             # increment of file count                
        #             search_success_count += 1
        #         except:
        #             print("File not exist")
        #     # if file does not exist in source folder
        #     else:
        #         print("File already exist")         
             
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


