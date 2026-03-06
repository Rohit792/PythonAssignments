# Python Assignment 32

## Python Programming - File Automation Scripts

**Please follow below rules while designing automation script:**
- Accept input through command line or through file.
- Display any message in log file instead of console.
- For separate task define separate function.
- For robustness handle every expected exception.
- Perform validations before taking any action.
- Create user defined modules to store the functionality.

---

### Problem 1: Directory Checksum Calculator
Design automation script which accept directory name and display checksum of all files.

**Usage:**
```bash
DirectoryChecksum.py "Demo"
```
Demo is name of directory.

**Output:**
```
Source Directory to search in: demo
-----------------------------------------------------
Current Directory: demo
File Name: candidate_bulk_upload_template.numbers
CheckSum: d2615368f676fc66af24642c4c248c6b

File Name: rohit-resume.pdf
CheckSum: e30254ec92df74709f5383b4b1769c88
-----------------------------------------------------
Current Directory: demo/images
File Name: male3.jpg
CheckSum: 6e9778e14865cdbc0974f4affc62cf32
-----------------------------------------------------
```

---

### Problem 2: Find Duplicate Files
Design automation script which accept directory name and write names of duplicate files from that directory into log file named as `Log.txt`. Log.txt file should be created into current directory.

**Usage:**
```bash
DirectoryDuplicate.py "Demo"
```
Demo is name of directory.

**Output:**
```
--------------------
List of Duplicate files are: 

index: 0
Found Duplicate of File: demo/candidate_bulk_upload_template.numbers
Duplicate file name: demo/images/test_duplicate.txt
--------------------

index: 1
Found Duplicate of File: demo/images/male3.jpg
Duplicate file name: demo/images/screenShots/male3.jpg
--------------------

index: 2
Found Duplicate of File: demo/rohit-resume.pdf
Duplicate file name: demo/images/screenShots/rohit-resume.pdf
--------------------
```

---

### Problem 3: Delete Duplicate Files with Logging
Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as `Log.txt`. Log.txt file should be created into current directory.

**Usage:**
```bash
DirectoryDuplicateRemoval.py "Demo"
```
Demo is name of directory.

**Output:**
```
--------------------
List of Duplicate files are: 

index: 0
Found Duplicate of File: demo/candidate_bulk_upload_template.numbers
Deleted File name: demo/images/test_duplicate.txt
--------------------

index: 1
Found Duplicate of File: demo/images/male3.jpg
Deleted File name: demo/images/screenShots/male3.jpg
--------------------

index: 2
Found Duplicate of File: demo/rohit-resume.pdf
Deleted File name: demo/images/screenShots/rohit-resume.pdf
--------------------
```

---

### Problem 4: Delete Duplicate Files with Execution Time
Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as `Log.txt`. Log.txt file should be created into current directory. Display execution time required for the script.

**Usage:**
```bash
DirectoryDuplicateRemoval.py "Demo"
```
Demo is name of directory.

**Output:**
```
--------------------
List of Duplicate files are: 

index: 0
Found Duplicate of File: demo/candidate_bulk_upload_template.numbers
Deleted File name: demo/images/duplicate.txt
--------------------

index: 1
Found Duplicate of File: demo/images/male3.jpg
Deleted File name: demo/images/screenShots/male3.jpg
--------------------

index: 2
Found Duplicate of File: demo/rohit-resume.pdf
Deleted File name: demo/images/screenShots/rohit-resume-duplicate.pdf
--------------------

Script executed in 0.01 seconds.
```