import page

user_name = "Helga"
password = "Helga"


def autirize (wait):
    page.login(wait).click()
    page.user(wait).send_keys(user_name)
    page.passw(wait).send_keys(password)
    page.submit(wait).click()