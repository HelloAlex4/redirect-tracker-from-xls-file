# redirect-tracker-from-xls-file

In this project the goal is to extract URLs from a Excel file, than track all the redirects.
The last step is to write the final redirected url to the excel file again.
(this project was created as a freelancing job)


When running the code, you will be prompted to input the path to the excel file which contains the URLs you wnat to track.
The excel file needs to be Formated the same way as the example file given.

The program will than track the redirects and write them back in the excel file.

The Problem with this code is that it runns very slowly a possible solution for that would be to implement threading.
