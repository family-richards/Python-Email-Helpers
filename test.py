from os import getenv
def test_make_email():
  from emailHelpers import Email
  email = Email("kidscodingplace@gmail.com")
  email.setTo("kidscodingplace@gmail.com")
  email.setSubject("Does this thing work?")
