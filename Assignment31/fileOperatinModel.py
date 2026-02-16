import os
import time
import shutil

border = 50

    
def createDirIfNotExist(folderName):
        ret = False
        ret = os.path.exists(folderName)
        if ret == True:
            ret = os.path.isdir(folderName)
            if(ret == False):
                print("Enable to create folder")
                return
        else:
            os.mkdir(folderName)
            print("Directory for log files gets created succesfully")
        

def fetchAllFilesWithExtensionUsing(directoryName, extension):
    print("\n")
    if not os.path.exists(path=directoryName):
        print("Directory not found")
        print("Please select directory from avaialble List of directories:\n")
        
        with os.scandir('.') as allFiles:
          for dir in allFiles:
              if dir.is_dir() == True:
                print(dir.name)
    else:
        availableFiles = []
        currDirectoryName = ""
        isFileFound = False
        fileWithDirectory = {}

        for currentDir, subdDir, curDirFiles in os.walk(directoryName):
            # print("Curretn Diretory: ", currentDir)
            # print("dir:", subdDir)
            # print("Current Directory Files: ",curDirFiles)
            if currDirectoryName != currentDir:
                currDirectoryName = currentDir

            availableFiles = []
            isFileFound = False
            for curfileName in curDirFiles:
                if extension in str(curfileName):
                    isFileFound = True
                    availableFiles.append(curfileName)
            if isFileFound == True:
                fileWithDirectory[currentDir] = availableFiles

        return fileWithDirectory
       
def logFileData(directoryName, extension, sourceDirectory = "Logs"):
    result = fetchAllFilesWithExtensionUsing(directoryName= directoryName, extension= extension)

    if len(result) == 0:
        print("No files found with extention: ", extension)
    else:
        createDirIfNotExist(sourceDirectory)

        timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = os.path.join(sourceDirectory,"Marvellous_%s.log" %timeStamp)

        
        fobj = open(fileName, "w")
        headerData = printHeader("FILE LOGGER", isTOWriteInFile=True)
        footerData = printFooter("FILE LOGGER", isTOWriteInFile=True)


        fobj.write(headerData)

        fobj.write(f"\nSource Directory to search in:  {directoryName}")
        fobj.write(f"\nFile Extention to search for:  {extension}\n\n")

        fobj.write(f"The following files with extension {extension} were found")
 
    
        for dir in result:
            fobj.write(f"\nDirectory: {dir}\n")

            for fName in result[dir]:
                fobj.write(f"{fName}\n")

        
        fobj.write(footerData)
        fobj.close()
       
def replaceFileExtensionUsing(directoryName, extension, replaceWithExtension , sourceDirectory = "Logs"):

    print("\n")
    if not os.path.exists(path=directoryName):
        print("Directory not found")
        print("Please select directory from avaialble List of directories:\n")
        
        with os.scandir('.') as allFiles:
            for dir in allFiles:
                if dir.is_dir() == True:
                    print(dir.name)
    else:
        createDirIfNotExist(sourceDirectory)

        timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = os.path.join(sourceDirectory,"Marvellous_%s.log" %timeStamp)

        
        fobj = open(fileName, "w")
        headerData = printHeader("FILE LOGGER", isTOWriteInFile=True)
        footerData = printFooter("FILE LOGGER", isTOWriteInFile=True)


        fobj.write(headerData)

        fobj.write(f"\nSource Directory to search in :  {directoryName}")
        fobj.write(f"\nFile Extention to search for  :  {extension}\n\n")
        fobj.write(f"\nFile Extention to Replace with:  {extension}\n\n")
 
        currDirectoryName = ""
        odlFileDir = {}
        newFileDir = {}

        for currentDir, subdDir, curDirFiles in os.walk(directoryName):
            if currDirectoryName != currentDir:
                currDirectoryName = currentDir

            oldFileNameList = []
            newFileList = []
            isFileFound = False

            for curfileName in curDirFiles:
                if extension in str(curfileName):
                    oldFilePath = os.path.join(currentDir, curfileName)
                    
                    newFileName = curfileName.replace(extension, replaceWithExtension)
                    newFilePath = os.path.join(currentDir, newFileName)
                    
                    isFileFound = True
                    
                    os.rename(oldFilePath, newFilePath)
                    
                    oldFileNameList.append(curfileName)
                    newFileList.append(newFileName)
                    print("newFileName: ", newFileName)
                    print("curfileName: ", curfileName)

                if isFileFound == True:
                   odlFileDir[currentDir] = oldFileNameList
                   newFileDir[currentDir] = newFileList

        fobj.write("\n")  
        fobj.write("-"*border) 
        fobj.write(f"\nThe following files with before replace with {extension}")
        for dir in odlFileDir:
            fobj.write(f"\nDirectory: {dir}\n")
            for fName in odlFileDir[dir]:
                fobj.write(f"{fName}\n")

        fobj.write("\n")
        fobj.write("-"*border)

        fobj.write(f"\nThe following files with after replaced with {extension} by {replaceWithExtension}.")

        for dir in newFileDir:
            fobj.write(f"\nDirectory: {dir}\n")
            for fName in newFileDir[dir]:
                fobj.write(f"{fName}\n")

        print("\n\n")
        fobj.write("-"*border)
        print("\n")
        fobj.write(footerData)

def copyAllToDestination(sourceDirectory, destinationDirectory, logsDir = "Logs"):
    printHeader("Copy Directory", True)
    print("\nSource Directory     : ", sourceDirectory)
    print("\nDestination Directory: ", destinationDirectory,"\n")

    if not os.path.exists(sourceDirectory):
        print("Directory does not exist.")
        return
    
    try:

        createDirIfNotExist(sourceDirectory)

        timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = os.path.join(logsDir,"Marvellous_%s.log" %timeStamp)

        
        fobj = open(fileName, "w")
        headerData = printHeader("Copy Directory", isTOWriteInFile=True)
        footerData = printFooter("Copy Directory", isTOWriteInFile=True)


        fobj.write(headerData)
        fobj.write("\n\n")
    
        shutil.copytree(sourceDirectory, destinationDirectory, dirs_exist_ok=True)
        fobj.write(f"Directory '{sourceDirectory}' successfully copied to '{destinationDirectory}'.")
        
        fobj.write("\n\nSource FIles\n")
        fobj.write("________________________________\n")

        currDirectoryName = ""
        for currentDir, subdDir, curDirFiles in os.walk(sourceDirectory):
            if currDirectoryName != currentDir:
                currDirectoryName = currentDir
                fobj.write(f"Directory: {currDirectoryName}")
                fobj.write("\n")

            for fNames in curDirFiles:
                fobj.write(fNames)
                fobj.write("\n")
            
            fobj.write("\n\n")


        fobj.write("\nCopied Destination Files\n")
        fobj.write("________________________________\n")

        currDirectoryName = ""
        for currentDir, subdDir, curDirFiles in os.walk(destinationDirectory):
            if currDirectoryName != currentDir:
                currDirectoryName = currentDir
                fobj.write(f"Directory: {currDirectoryName}")
                fobj.write("\n")

            for fNames in curDirFiles:
                fobj.write(fNames)
                fobj.write("\n")
            
            fobj.write("\n\n")

    except FileExistsError:
        fobj.write(f"Error: The destination directory '{destinationDirectory}' already exists.")
    except Exception as e:
        fobj.write(f"An error occurred: {e}")
            
    fobj.write("\n")
    fobj.write(footerData)


def checkExtensionBeforCopy(sourceDirectory, destinationDirectory, extension):
    if not os.path.exists(sourceDirectory):
        print(f"Source directory '{sourceDirectory}' does not exist.")
        return
    
    os.makedirs(destinationDirectory, exist_ok=True)

    
    for currDir, sub_dirs, files in os.walk(sourceDirectory):
        relativePath = os.path.relpath(currDir, sourceDirectory)
        destpath = os.path.join(destinationDirectory, relativePath)
        listOfSourceFilesToCopy = []
        listOfdestFilesToCopy = []

        for fName in files:
            sourceFile = os.path.join(currDir, fName)
            destFile = os.path.join(destpath, fName)
            if extension in str(fName):
                listOfSourceFilesToCopy.append(sourceFile)
                listOfdestFilesToCopy.append(destFile)
                
        if len(listOfSourceFilesToCopy) != 0:
            os.makedirs(destpath, exist_ok=True)
            for i in range(len(listOfSourceFilesToCopy)):
                shutil.copy2(listOfSourceFilesToCopy[i], listOfdestFilesToCopy[i])
                print(f"Copied {sourceFile} to {destFile}")



def printHeader(ProjectName, isTOWriteInFile = False):
    borderLine = "-"*border
    projectName = f"---------------THIS IS {ProjectName}----------------"

    print(f"{borderLine}\n{projectName}\n{borderLine}\n")

    if isTOWriteInFile:
        return f"{borderLine}\n{projectName}\n{borderLine}\n"



def printFooter(ProjectName, isTOWriteInFile = False):
    borderLine = "-"*border
    projectName = f"-----------THIS IS THE END OF {ProjectName}---------"

    print(f"{borderLine}\n{projectName}\n{borderLine}\n")

    if isTOWriteInFile:
        return f"{borderLine}\n{projectName}\n{borderLine}\n"
  
