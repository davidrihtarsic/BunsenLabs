#! /usr/bin/python
import os
import sys
debug=False

def getPathNameDistLink(full_file_name):
    path,name=os.path.split(full_file_name)
    if '/Files/' in path:
        files_path=path
        cloud_path=files_path.replace('/Files/','/DropBox/')
    else:
        cloud_path=path
        files_path=cloud_path.replace('/DropBox/','/Files/')
    if '.' in name:
        link=name.replace('.','@DropBox.')
    else:
        link=name+'@DropBox'
    if debug:print('Files path:',files_path,'\nFile name:',name,'\nCloud path:',cloud_path,'\nLink name:',link)
    return [files_path,name,cloud_path,link]

def moveFileFromCloudToFiles(cloud_path, name, files_path, link):
    os.system('mkdir -p '+files_path)
    os.system('mv -v '+cloud_path+'/'+name+' '+files_path)
    #del a symlink in Files
    os.system('rm -v '+files_path+'/'+link)

def moveFileFromFilesToCloud(cloud_path, name, files_path, link):
    os.system('mkdir -p '+cloud_path)
    os.system('cp -v -r '+files_path+'/'+name+' '+cloud_path)
    os.system('rm -v -R '+files_path+'/'+name)
    #make a symlink to original dir
    os.system('ln -s '+cloud_path+'/'+name+' '+files_path+'/'+link)

#--MAIN-CODE-------
sys.argv.pop(0)
for argument in sys.argv:
    if argument=='-debug': debug=True
    if 'DropBox' in argument:
        if '@DropBox' in argument: argument=argument.replace('@DropBox','')
        files_path,name,cloud_path,link=getPathNameDistLink(argument)
        moveFileFromCloudToFiles(cloud_path, name, files_path, link)    
    elif 'Files/' in argument:
        files_path,name,cloud_path,link=getPathNameDistLink(argument)
        moveFileFromFilesToCloud(cloud_path, name, files_path, link)