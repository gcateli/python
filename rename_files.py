import os
    #1 - get file names from a folder
def rename_files():
    folder = r"C:\Users\ernetwork\Downloads\prank"
    file_list = os.listdir(folder)
    saved_path = os.getcwd()
    print(file_list)
    os.chdir(folder)
    table = str.maketrans("","","0123456789")
    #2 - for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)
        
rename_files()
    
    
