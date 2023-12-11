# 542-Project

This project was created as part of a project for CIS 542 at UMass Dartmouth (Fall 2023)

This code is designed to take in 2 directories and compare each file in the first
directory to each file in the second directory. It will print the number of
files, along with the files themselves, that share the same hash values but
have different file names. It will also print the number of files and the files
that share a file name but have different hash values.

This program is not designed to interpret the data printed!
It simply returns raw data and requires the user to determine what that data means.

This program uses two particular python libraries: hashlib and os
Hashlib is used to retrieve the hash values of files and os
is usd to retrieve all the files ans filepaths used.

The program is used by modifying the two lines with filepaths. These can be changed
to any filepath that the program has access to, including entire drives. Accessing
an entire drive is done simply by using the drive letter as opposed to an entire
filepath. The two test folders are used for testing purposes and contain random
files which the program is set to target by default.
