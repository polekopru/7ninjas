# 7ninjas Python Developer Test

Short description on how to test funcionalities such as Facebook sign in/sign up and captcha.

## Facebook

Due to Facebook app setting for Site URL and for local use it has to be *localhost:8000*.

For Facebook sign in/sign up purposes try

'''
localhost:8000/accounts/login/
'''

and click "Facebook" hyperlink.

## Captcha

For testing if captcha works fine in sign up form, site url must starts with *127.0.0.1*.

E.g.

```
127.0.0.1:8000/accounts/signup/
```
