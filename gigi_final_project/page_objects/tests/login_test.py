from gigi_final_project.page_objects.pages.login_page import loginPage


class Testlogin():

    def test_correct_login(self,setup_swaglabs):
        print("Test Start")
        page = setup_swaglabs
        login_page = loginPage(page) #In __init__ you can send definitions of characteristics of objects
        login_page.set_user_and_password()
        login_page.click_on_login_button()