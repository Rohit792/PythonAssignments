"""
Question:
Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc.

"""
import sys
import fileOperatinModel as fModel
import schedule
import time

def main():
    print("\n")
    fModel.printHeader("FILE LOGGER")
    
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is use to: ")
            print("1. Display all files with given extension.")
         
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as:\n")
            print("- Script: DirectoryRename.py SourceDirectory existingExtension replaceWithExtension")
            print("- SourceDirectory: Name of directory to search the file with given extention")
            print("- existingExtension: file to search with perticular extetnion. Ex: .txt, .pdf, .jpeg")
            print("- replaceWithExtension: Replaced the existingFiles extention with given extension.")
            print("- Example: DirectoryRename.py “Demo” “.txt” “.doc”")
            print("    - It will replace .txt files with .doc extention.")

        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u to get more details")

    # python DirectoryRename.py “Demo” “.txt” “.doc”
    elif(len(sys.argv) == 4):
        print("Inside project logic")
        print("Directory name: ", sys.argv[1])
        print("Search for Extention: ", sys.argv[2])
        print(f"Replace {sys.argv[2]} Extention with {sys.argv[3]}")

        schedule.every(interval=1).minutes.do(fModel.replaceFileExtensionUsing, sys.argv[1], sys.argv[2], sys.argv[3])
        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    fModel.printFooter("FILE LOGGER")

if __name__ == "__main__":
    main()