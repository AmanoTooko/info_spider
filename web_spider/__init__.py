from web_spider import http_downloader
jw_addr=['60.18.131.133:11181','60.18.131.133:11180','60.18.131.131:11080','60.18.131.131:11180']
jw_veryfy_link = 'http://'+jw_addr[0]+'/academic/common/security/check1.jsp'
lib_veryfy_link = 'http://202.199.233.11:8080/reader/captcha.php'

a=http_downloader.Downloader()
a.photo_download('1205010314')
print(a.code_veryfy(lib_veryfy_link))