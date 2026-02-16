# Python Assignment 31

## Python Programming - File Automation Scripts

**Important Rules for Automation Scripts:**
- Accept input through command line or through file
- Display any message in log file instead of console
- For separate task define separate function
- For robustness handle every expected exception
- Perform validations before taking any action
- Create user defined modules to store the functionality

---

### Problem 1: Directory File Search
**Problem Statement:**  
Design automation script which accepts directory name and file extension from user. Display all files with that extension.

**Usage:**
```
DirectoryFileSearch.py "Demo" ".txt"
```

**Explanation:**  
`Demo` is name of directory and `.txt` is the extension that we want to search.

---

### Problem 2: Directory Rename Files
**Problem Statement:**  
Design automation script which accepts directory name and two file extensions from user. Rename all files with first file extension with the second file extension.

**Usage:**
```
DirectoryRename.py "Demo" ".txt" ".doc"
```

**Explanation:**  
`Demo` is name of directory and `.txt` is the extension that we want to search and rename with `.doc`. After execution this script each `.txt` file gets renamed as `.doc`.

---

### Problem 3: Directory Copy All Files
**Problem Statement:**  
Design automation script which accepts two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.

**Usage:**
```
DirectoryCopy.py "Demo" "Temp2"
```

**Explanation:**  
`Demo` is name of directory which is existing and contains files in it. We have to create new directory as `Temp2` and copy all files from Demo to Temp2.

---

### Problem 4: Directory Copy Files by Extension
**Problem Statement:**  
Design automation script which accepts two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time.

**Usage:**
```
DirectoryCopyExt.py "Demo" "Temp3" ".exe"
```

**Explanation:**  
`Demo` is name of directory which is existing and contains files in it. We have to create new directory as `Temp3` and copy all files with extension `.exe` from Demo to Temp3.
