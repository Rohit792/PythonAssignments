import os
import hashlib
import time

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



def calculateCheckSum(fileName):
    # print("File name: ", os.path.basename(fileName))
    if not os.path.exists(fileName):
        print("File Not found")
        return
    
    fileobj = open(fileName, "rb")
    hashobj = hashlib.md5()

    buffer = fileobj.read(1024)

    while len(buffer) > 0:
        hashobj.update(buffer)
        buffer = fileobj.read(1024)

    fileobj.close()
    return hashobj.hexdigest()

def findCheckSumOfFilesIn(directoryName, sourceDirectory = "Logs"):
    
    if not os.path.exists(directoryName):
        print("Directory Not found")
    else:
        print("\n")
        print("------------------------------------")
        createDirIfNotExist(sourceDirectory)

        timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = os.path.join(sourceDirectory,"Marvellous_%s.log" %timeStamp)

        
        fobj = open(fileName, "w")
        headerData = printHeader("FILE LOGGER", isTOWriteInFile=True)
        footerData = printFooter("FILE LOGGER", isTOWriteInFile=True)


        fobj.write(headerData)

        fobj.write(f"\nSource Directory to search in:  {directoryName}") 
        fobj.write("\n")
        for curDirName, _, curFileNames in os.walk(directoryName):
            fobj.write(f"\nCurrent Directory:  {curDirName}") 
            for fName in curFileNames:
                fileName = os.path.join(curDirName, fName)
                fobj.write(f"\nFile Name: {fName}\nCheckSum: {calculateCheckSum(fileName)}\n") 
            fobj.write("\n")

    fobj.write(footerData)


def findDuplicateInDirectory(directoryName, sourceDirectory = "Logs"):
    if not os.path.exists(directoryName):
        print("Directory Not found")
    else:
        print("\n")
        print("------------------------------------")
        createDirIfNotExist(sourceDirectory)

        timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = os.path.join(sourceDirectory,"Marvellous_%s.log" %timeStamp)

        
        fobj = open(fileName, "w")
        headerData = printHeader("FILE LOGGER", isTOWriteInFile=True)
        footerData = printFooter("FILE LOGGER", isTOWriteInFile=True)


        fobj.write(headerData)

        fobj.write(f"\nSource Directory to search in:  {directoryName}") 
        fobj.write("\n")
        dirDuplicate = {}
        listDuplicateData = []
        lastFound = []
        for curDirName, _, curFileNames in os.walk(directoryName):
            fobj.write(f"\nCurrent Directory:  {curDirName}") 
            for fName in curFileNames:
                fileName = os.path.join(curDirName, fName)
                fobj.write(f"\nFile Name: {fName}\nCheckSum: {calculateCheckSum(fileName)}\n") 
                checkSum = calculateCheckSum(fileName)
                if dirDuplicate.get(checkSum) != None:
                    listDuplicateData.append(fileName)
                    lastFound.append(dirDuplicate[checkSum])
                dirDuplicate[checkSum] = fileName

        fobj.write("\n\n--------------------\n")
        if len(listDuplicateData) > 0:
            fobj.write("\nList of Duplicate files are: \n")
            for i in range(len(listDuplicateData)):
                fobj.write(f"\nindex: {i}\n")
                fobj.write(f"Found Duplicate of File: {lastFound[i]}\n")
                fobj.write(f"Duplicate fIle name: {listDuplicateData[i]}\n")
                fobj.write("--------------------")
                fobj.write("\n")

        fobj.write("\n")
        fobj.write(footerData)

def findAndRemoveDuplicateInDirectory(directoryName, sourceDirectory = "Logs"):
    if not os.path.exists(directoryName):
        print("Directory Not found")
    else:
        print("\n")
        print("------------------------------------")
        createDirIfNotExist(sourceDirectory)

        fileName = os.path.join("logs.text")

        
        fobj = open(fileName, "w")
        headerData = printHeader("FILE LOGGER", isTOWriteInFile=True)
        footerData = printFooter("FILE LOGGER", isTOWriteInFile=True)


        fobj.write(headerData)

        fobj.write(f"\nSource Directory to search in:  {directoryName}") 
        fobj.write("\n")
        dirDuplicate = {}
        listDuplicateData = []
        lastFound = []
        for curDirName, _, curFileNames in os.walk(directoryName):
            for fName in curFileNames:
                fileName = os.path.join(curDirName, fName)
                checkSum = calculateCheckSum(fileName)
                if dirDuplicate.get(checkSum) != None:
                    listDuplicateData.append(fileName)
                    lastFound.append(dirDuplicate[checkSum])
                    os.remove(fileName)
                dirDuplicate[checkSum] = fileName

        fobj.write("\n\n--------------------\n")
        if len(listDuplicateData) > 0:
            fobj.write("\nList of Duplicate files are: \n")
            for i in range(len(listDuplicateData)):
                fobj.write(f"\nindex: {i}\n")
                fobj.write(f"Found Duplicate of File: {lastFound[i]}\n")
                fobj.write(f"Deleted File name: {listDuplicateData[i]}\n")
                fobj.write("--------------------")
                fobj.write("\n")

        fobj.write("\n")
        fobj.write(footerData)

def findAndRemoveDuplicateInDirectoryWithTime(directoryName, sourceDirectory = "Logs"):
    if not os.path.exists(directoryName):
        print("Directory Not found")
    else:
        startTime = time.time()
        print("\n")
        print("------------------------------------")
        createDirIfNotExist(sourceDirectory)

        fileName = os.path.join("logs.text")

        
        fobj = open(fileName, "w")
        headerData = printHeader("FILE LOGGER", isTOWriteInFile=True)
        footerData = printFooter("FILE LOGGER", isTOWriteInFile=True)


        fobj.write(headerData)

        fobj.write(f"\nSource Directory to search in:  {directoryName}") 
        fobj.write("\n")
        dirDuplicate = {}
        listDuplicateData = []
        lastFound = []
        for curDirName, _, curFileNames in os.walk(directoryName):
            for fName in curFileNames:
                fileName = os.path.join(curDirName, fName)
                checkSum = calculateCheckSum(fileName)
                if dirDuplicate.get(checkSum) != None:
                    listDuplicateData.append(fileName)
                    lastFound.append(dirDuplicate[checkSum])
                    os.remove(fileName)
                dirDuplicate[checkSum] = fileName

        fobj.write("\n\n--------------------\n")
        if len(listDuplicateData) > 0:
            fobj.write("\nList of Duplicate files are: \n")
            for i in range(len(listDuplicateData)):
                fobj.write(f"\nindex: {i}\n")
                fobj.write(f"Found Duplicate of File: {lastFound[i]}\n")
                fobj.write(f"Deleted File name: {listDuplicateData[i]}\n")
                fobj.write("--------------------")
                fobj.write("\n")

        endTime = time.time()
        requiredTime = endTime - startTime

        fobj.write(f"\nScript executed in {requiredTime:.2f} seconds.\n")

        fobj.write("\n")
        fobj.write(footerData)


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
  
