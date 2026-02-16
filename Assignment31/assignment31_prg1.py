"""
Question:
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
1.Design automation script which accept directory name and file extension from user. Display all
files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
Demo is name of directory and .txt is the extension that we want to search.

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
            print("- Use the automation script as")
            print("- SCript name.py sourceDirectory extenion")
            print("- SourceDirectory: Name of directory to search the file with given extention")
            print("- extenion: file to search with perticular extetnion. Ex: .txt, .pdf, .jpeg")

        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u to get more details")

    # python name.py sourceDirectory extenion
    elif(len(sys.argv) == 3):
        print("Inside project logic")
        print("Directory name: ", sys.argv[1])
        print("File Extention: ", sys.argv[2])

        schedule.every(interval=1).minutes.do(fModel.logFileData, sys.argv[1], sys.argv[2])
        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    print("\n")
    fModel.printFooter("FILE LOGGER")

if __name__ == "__main__":
    main()