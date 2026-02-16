"""
Question:
Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py “Demo” “Temp”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp.

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
            print("- Script: DirectoryCopy.py SourceDirectory destinationDirectory")
            print("- SourceDirectory: Name of directory to search the file with given extention")
            print("- destinationDirectory: Copy all files from Source directory into destination directory")

        else:
            print("Unable to procced as there is no such option")
            print("Please use --h or --u to get more details")

    # python DirectoryCopy.py SourceDirectory destinationDirectory
    elif(len(sys.argv) == 3):
        print("Inside project logic")
        print(f"Copy From {sys.argv[1]} and paste it to {sys.argv[2]} directory.")

        schedule.every(interval=1).minutes.do(fModel.copyAllToDestination, sys.argv[1], sys.argv[2])
        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()