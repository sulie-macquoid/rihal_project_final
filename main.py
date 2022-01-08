import pytesseract #OCR library
import cv2 #opencv to deal with the image, making it pop up and interact with the OCR library
import re #RegEx
from datetime import datetime #datetime to reformat the dates into a YYYY-MM-DD basis

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nowax\tesseract\tesseract.exe' #imports tesseract library from hard drive (replace this line with the directory begining from C:)

img = cv2.imread('ocr.png') #converts the png into a file the program can deal with
img = cv2.resize(img, (700, 700)) #resizes the image into a size that is clear to read by the OCR lib
string = pytesseract.image_to_string(img) #the OCR is done in this line, places the text into a string called string lol

datesO = [] #V1 of dates, before reformating
dateTimeA = [] #after being converted into a format the datetime lib can read
datesN = [] #final array of dates, can be printed now
roomNO = [] #room names old
roomNN = [] #room names new
roomRO = [] #room rates old
roomRN = [] #room rates new
namesO = [] #names old
namesN = [] #names new
emails = [] #emails


datesO = re.findall(r'[0-9]+[0-9]+\/+[0-9]+[0-9]+\/+[0-9]+[0-9]+[0-9]+[0-9]', string) #finds all characters with the
# XX/XX/XXXX format, X being a number
for x in datesO: 
    y = datetime.strptime(x, '%d/%m/%Y') #implements the datetime library
    dateTimeA.append(y) #adds the result to the dateTimeA array
for x in dateTimeA: 
    y = x.strftime('%Y-%m-%d') #converts the results from the previous array to the format YYYY-MM-DD
    datesN.append(y) #adds them to the final list
#the desired outputs for dates were achived

roomNO = re.findall(r'Room: +[\w]+', string) #finds all words that contain "Room: " before them
for x in roomNO: #will remove the "Room: " infront of the string
    y = x[6:] #deletes the first 6 chars of the string
    roomNN.append(y) #adds them to the final list
#the desired outputs for room names were achived

roomRO = re.findall(r'\$([0-9,]+)', string) #finds all the numbers that have a dollar sign before them
for x in roomRO: 
    y = "${:}".format(x) #will add a dollar sign infront of the numbers, since they aren't added from the previous line
    roomRN.append(y) #adds all of the numbers, with the dollar sign infront
#the desired outputs for room rates were achived

namesO = re.findall(r'[:;]\s*(.+?)\s*<', string) #finds all words that follow a semicolon or a colon, and ends with a >
for x in namesO: #will format the names to a FIRSTNAME LASTNAME basis
    for lname, fname in [q.split(",") for q in x.split(";")]: #splits the string into two sections called fname lname
        a = fname[1:] #erases the first char of fname, which is a whitespace
        b = len(lname)+1
        c = lname.rjust(b) #adds a space infront of lname, to seperate them
        r = a + c #adds both fname and lname after being formated
        namesN.append(r) #adds them to the namesN list
#the desired outputs for names were achived

emails = re.findall(r'[\w\.-]+@[\w\.-]+', string) #finds the words that have a . after them, then an @ symbol, then
# another word that ends with a .
#the desired outputs for emails were achived

print(string) #print the entire string

print(datesN)
print(roomNN)
print(roomRN)
print(namesN)
print(emails)
#prints all of the outputs
cv2.imshow('sulieman says hi', img) #makes the image pop out when code is run
cv2.waitKey(0) #makes the image stay up for infinity
