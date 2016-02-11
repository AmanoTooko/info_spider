import urllib.request
from PIL import Image
from pytesseract.pytesseract import image_to_string
jw_addr=['60.18.131.133:11181','60.18.131.133:11180','60.18.131.131:11080','60.18.131.131:11180']
jw_veryfy_link = 'http://'+jw_addr[0]+'/academic/common/security/check1.jsp'
lib_veryfy_link = 'http://202.199.233.11:8080/reader/captcha.php'
class Downloader:
    def __init__(self):
        self.data_path = 'A:/data/'
    def photo_download(self,num):
        local =self.data_path+num+'.jpg'
        try:
            urllib.request.urlretrieve('http://'+jw_addr[0]+'/newacademic/manager/studentinfo/photo/photo/'+num+'.jpg',local)
        except Exception :
           print("Error occured in photo downloading... ")
        return "/"+num+'.jpg'
    def code_veryfy(self,link):
        local = 'verifycode.jpg'
        try:
            urllib.request.urlretrieve(link,local)
            image1=Image.open(local)
            text=image_to_string(image1)
        except Exception :
           print("Error occured in code verifing... ")
        return text






#urllib.request.urlretrieve('http://60.18.131.131:11180/academic/common/security/check1.jsp',local)
