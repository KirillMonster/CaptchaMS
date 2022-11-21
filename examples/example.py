from CaptchaMS import Captcha

captcha = Captcha()
captcha.generate()
captcha.save('captcha.png')
