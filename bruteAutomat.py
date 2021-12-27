from webbot import Browser
web = Browser("C:\Program Files\Google\Chrome\Application\chrome.exe")
web.go_to('https://satu.unma.ac.id/')
web.type('password',username = '18.14.1.0004',classname="form-input")
web.type('username',username = '@Mrky404',classname="form-input")
web.click('Masuk')
