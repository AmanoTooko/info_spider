from web_spider import http_downloader


a=http_downloader.Downloader()
a.photo_download('1205010314')
print(a.code_veryfy(lib_veryfy_link))