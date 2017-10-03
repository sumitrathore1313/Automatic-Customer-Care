import os
def generate_mix_file(dir_path, output_path):
    '''
    this funtion take all labeled resume and combine to form all.txt
    NOTE - delete all file if already exist beacuse it will not overwrite
    :param dir_path: path of resume dir
    :param output_path : path of output file
    :return: generate segments file for level
    '''
    # select only dir not file
    filelist = os.walk(dir_path).next()[2]
    for file in filelist:
            with open(dir_path+file, 'r') as f:
                contents = f.read()
            with open(output_path, 'a') as f:
                f.write(contents)
    return 0

