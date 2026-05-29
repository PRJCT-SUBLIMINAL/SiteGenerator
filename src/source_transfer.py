import os
import shutil

def copy_recursive(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    dirs = os.listdir(src)
    for directory in dirs:
        directory_src = os.path.join(src, directory)
        if os.path.isfile(directory_src):
            shutil.copy(directory_src, dst)
        else:
            new_dst = os.path.join(dst, directory)
            copy_recursive(directory_src, new_dst)
    

def static_to_public():
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    copy_recursive("./static", "./docs")