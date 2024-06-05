from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Para evitar que se cierre automáticamente: (comentar después):
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
# Esperar 10 segundos hasta comprobar la web:
browser.implicitly_wait(10)
browser.get("https://github.com")

# Para ir al enlace de iniciar sesión:
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()


user_input = browser.find_element(By.ID, "login_field")
password_input = browser.find_element(By.ID, "password")

# Rellenamos desde las variables de entorno:
user_input.send_keys(os.environ.get("GH_USER"))
password_input.send_keys(os.environ.get("GH_PASSWORD"))
password_input.send_keys(Keys.RETURN)

# Comprobamos que se ha iniciado sesión correctamente
# si aparece nuestro nombre de usuario en la siguiente clase
# para especificar varias clases a la vez, se unen con un punto:
profile_section = browser.find_element(By.CLASS_NAME, "avatar.circle")
profile_section.click()

possible_profile = browser.find_elements(
    By.CLASS_NAME,
    "Truncate-text"
)

for element in possible_profile:
    label = element.get_attribute("innerHTML")

    if label.strip() == "darfox97":
        print("Inicio de sesión correcto.")
        break

# Si no se cumple el assert, devolverá una excepción AssertionError:
assert "darfox97" in label

browser.quit()
