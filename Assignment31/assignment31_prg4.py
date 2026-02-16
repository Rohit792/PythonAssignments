"""
Question:
Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp.

"""
import sys
import fileOperatinModel as fModel
import schedule
import time

def main():
    
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is use to: ")
            print("1. Copy all files from first directory into second directory. ")
            print("2. Second directory should be created at run time.")
         
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as:\n")
            print("- Script: DirectoryCopy.py SourceDirectory destinationDirectory extension")
            print("- SourceDirectory: Name of directory to search the file with given extention")
            print("- destinationDirectory: Copy all files from Source directory into destination directory")
            print("- extension: Check if this extension available for copy")

        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u to get more details")

    # python DirectoryCopyExt.py “Demo” “Temp” “.exe”
    elif(len(sys.argv) == 4):
        print("Inside project logic")
        print(f"Copy From {sys.argv[1]} and paste it to {sys.argv[2]} directory if {sys.argv[3]} exist.")

        schedule.every(interval=1).minutes.do(fModel.checkExtensionBeforCopy, sys.argv[1], sys.argv[2], sys.argv[3])
        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()