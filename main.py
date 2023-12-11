#
# Christopher Ferreira
# CIS 542 Project
#
# 542-Project
# This code is designed to take in 2 directories and compare each file in the first
# directory to each file in the second directory. It will print the number of
# files, along with the files themselves, that share the same hash values but
# have different file names. It will also print the number of files and the files
# that share a file name but have different hash values.
#
# This program is not designed to interpret the data printed!
# It simply returns raw data and requires the user to determine what that data means.
#
# This program uses two particular python libraries: hashlib and os
# Hashlib is used to retrieve the hash values of files and os
# is usd to retrieve all the files ans filepaths used.



import hashlib
import os

# retrieves the paths to both test folders that will be compared later
dir1 = os.getcwd() + '\\TestSet1'  # filepath for the first set, can be changed to a single letter
# to test an entire drive, may need permissions
dir2 = os.getcwd() + '\\TestSet2'  # filepath for the second set, can be changed to a single letter
# to test an entire drive, may need permissions

# These two filter out the folders and only show files
dir1Files = [os.path.join(dir1, f) for f in os.listdir(dir1) if
             os.path.isfile(os.path.join(dir1, f))]

dir2Files = [os.path.join(dir2, t) for t in os.listdir(dir2) if
             os.path.isfile(os.path.join(dir2, t))]


# print(len(dir1Files))
# print(len(dir2Files))

# This function returns the hash of the file passed into it
def hash_file(filename):

    # create a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop util the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex representation of digest
    return h.hexdigest()

# stores all hashes in a 2D array, pairing the filename with the hash value
dir1Hash = [[0 for x in range(2)] for y in range(len(dir1Files))]
dir2Hash = [[0 for p in range(2)] for q in range(len(dir2Files))]

# loops through the list of files in dir1Files and gets their hash values
for i in range(len(dir1Files)):
    dir1Hash[i][0] = dir1Files[i]
    dir1Hash[i][1] = hash_file(dir1Files[i])

# loops through the list of files in dir2Files and gets their hash values
for l in range(len(dir2Files)):
    dir2Hash[l][0] = dir2Files[l]
    dir2Hash[l][1] = hash_file(dir2Files[l])

hashMismatch = 0
filenameMismatch = 0

print()

for a in range(len(dir1Hash)): # outer loop that will iterate through the first set of files
    for b in range(len(dir2Hash)): # inner loop that will iterate through the second set of files

        # This block checks for issues where two files share a hash value, but have a different
        # file name, indicating duplicate files
        if (dir1Hash[a][1] == dir2Hash[b][1]) and (
                os.path.basename(dir1Hash[a][0]) != os.path.basename(dir2Hash[b][0])):
            hashMismatch += 1
            # This will print the two files that share a hash but have different names
            print(os.path.basename(dir1Hash[a][0]) + " in " + dir1 + " shares a hash with " +
                  os.path.basename(dir2Hash[b][0])
                  + " in " + dir2)

        # This block checks for issues where two files share a file name, but have a different
        # hash value, indicating potential fake files
        if (dir1Hash[a][1] != dir2Hash[b][1]) and (
                os.path.basename(dir1Hash[a][0]) == os.path.basename(dir2Hash[b][0])):
            filenameMismatch += 1
            # This will print the two files that share a name but have different hashes
            print(os.path.basename(dir1Hash[a][0]) + " in " + dir1 + " shares a name with " +
                  os.path.basename(dir2Hash[b][0])
                  + " in " + dir2)

# print(dir1Hash)
# print(dir2Hash)
print()
print("Number of files that share a hash with another file but have a different file name: ", hashMismatch)
print("\nNumber of files that share a file name with another file but have a different hash: ", filenameMismatch)
