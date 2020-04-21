# Django Web Library
A web library api with django. Also contains image processing.
A manager can upload a book image and api read ISBN number then save to db.
Also manager modules:
1) Manager could be list all user and their books.
2) Manager could be use time jump module (to check users that pass delivery date)

User modules:
1) User could be search a book with name or ISBN number.
2) User could be give book by uploading a image of book then api takes ISBN number from image.
3) User can not take more than 3 number of books and also if he/she has a book that passed delivery date, can not take a new book.
## Installation
You must have virtualenv
For example:
```bash
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv vlibrary
```
In Addition:
on ubuntu 12.04 LTS, installing through pip, it is installed to
/usr/local/bin/virtualenvwrapper.sh

on ubuntu 17.04, installing through pip as a normal user, it is installed to
~/.local/bin/virtualenvwrapper.sh

Then 
```
pip install -r config/requirements.txt
```
Finally

Install pytesseract

### On Linux
```
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```
### On mac
brew install tesseract
