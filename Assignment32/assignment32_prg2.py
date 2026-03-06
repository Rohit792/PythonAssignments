"""
Question:
2. Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
Usage : DirectoryDusplicate.py "Demo"
Demo is name of directory.

"""
import sys
import file_operation_model as fModel
import schedule
import time

def main():
    print("\n")
    fModel.printHeader("Directory Checksum")

    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is use to: ")
            print("1. Display checksum of all files in the Directory.")
         
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("- Use the automation script as")
            print("- SCript name.py sourceDirectory")
            print("- SourceDirectory: Name of directory to search the file with checksum")

    # python name.py sourceDirectory
        else:
            print("Inside project logic")
            print("Directory name: ", sys.argv[1])
            fModel.findDuplicateInDirectory(sys.argv[1])

            # schedule.every(interval=1).minutes.do(fModel.logFileData, sys.argv[1], sys.argv[2])
            # #Wait till abort
            # while True:
            #     schedule.run_pending()
            #     time.sleep(1)

    else:
        print("Unable to procced as there is no such option")
        print("Please use --h or --u to get more details")
    print("\n")
    
    fModel.printFooter("Directory Checksum")

if __name__ == "__main__":
    main()