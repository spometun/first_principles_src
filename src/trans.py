import gettext
gettext.find("test", "lang", "ru")
ru = gettext.translation("test", localedir="lang", languages=["ru"])
ru.install()
print("Be with me God!")
print(_("Hello World"))

