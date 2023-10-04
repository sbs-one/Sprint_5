from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    HEADER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    ADDS_LINK = (By.XPATH, '//span[contains(text(),"Начинки")]')
    SOUS_LINK = (By.XPATH, '//span[contains(text(),"Соусы")]')
    BREAD_LINK = (By.XPATH, '//span[contains(text(),"Булки")]')
    MEAT_DESCRIPTION = (By.XPATH, '//p[contains(text(),"Мясо бессмертных моллюсков Protostomia")]')
    SPICY_X_DESCRIPTION = (By.XPATH, '//p[contains(text(),"Соус Spicy-X")]')
    R2D3_DESCRIPTION = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]')


class NavigationPageLocators:
    LK_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    CONSTRUCTOR_LINK = (By.XPATH, '//p[contains(text(),"Конструктор")]')
    BURGER_HEADER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    LOGIN_HEADER = (By.XPATH, '//h2[contains(text(),"Вход")]')
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input[@type="text"]')
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password" and @name="Пароль"]')
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')


class LoginPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
    REGISTER_LINK = (By.XPATH, '//a[contains(text(),"Зарегистрироваться")]')
    PERSONAL_KABINET_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    REGISTER_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    LOGIN_LINK = (By.XPATH, '//a[contains(text(),"Войти")]')
    FORGET_PASSWORD = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')


class RegistrationPageLocators:
    LK_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    REGISTER_LINK = (By.XPATH, '//a[contains(text(),"Зарегистрироваться")]')
    REGISTER_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input[@type="text"]')
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password" and @name="Пароль"]')
    LOGIN_HEADER = (By.XPATH, '//h2[contains(text(),"Вход")]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    LOGIN_INPUT = (By.XPATH, "//label[text()='Логин']/following-sibling::input")

