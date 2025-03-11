import time
# import sched
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Función para revisar la web y verificar la entrada "Grimey x Palestina VI"
def check_grimey_blog():
    # print("🔍 Comprobando la web de Grimey...")

    options = Options()
    options.add_argument("--headless")  # ✅ Modo sin interfaz gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())  # ✅ Instalar ChromeDriver automáticamente
    driver = webdriver.Chrome(service=service, options=options)  # ✅ Ahora con modo headless

    url = "https://grimey.com/blog"
    driver.get(url)
    print("✅ Página cargada correctamente")

    # Buscar todos los h3 que contienen un anchor <a> con un span dentro
    h2_elements = driver.find_elements(By.CLASS_NAME, "h2")
    
    for h2 in h2_elements:
        print(h2.text)
    
    # Cerrar navegador
    driver.quit()

    print("✅ Navegador cerrado correctamente")
        
    #     # Esperar a que Cloudflare cargue (10 segundos por seguridad)
    #     time.sleep(10)

    #     # Obtener el HTML
    #     page_source = driver.page_source
    #     soup = BeautifulSoup(page_source, "html.parser")

    #     # Extraer títulos de los posts
    #     titles = [title.get_text(strip=True) for title in soup.find_all(["h1", "h2", "h3"])]

    #     # Verificar si existe "Grimey x Palestina VI"
    #     for title in titles:
    #         if "Grimey x Palestina VI" in title:
    #             print("✅ ¡Nueva entrada encontrada!")
    #             send_email_notification()
    #             break
    #     else:
    #         send_email_nonews_notification()
    #         print("🚫 No se encontró ninguna nueva entrada.")

    # except Exception as e:
    #     print(f"❌ Error: {e}")

    # finally:
    #     driver.quit()

# Función para enviar un correo si hay novedades
def send_email_notification():
    sender_email = "alfonsoapariciovega@gmail.com"
    receiver_email = "alfonsoapariciovega@gmail.com"  # Cambia esto al email donde quieres recibir la alerta
    password = "kdbppwebtkjgwpof"

    subject = "¡Nueva Entrada en Grimey: Grimey x Palestina VI!"
    body = "Se ha detectado una nueva entrada en el blog de Grimey sobre 'Grimey x Palestina VI'. ¡Revisa la web ahora!"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("📩 Correo enviado con éxito.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")

def send_email_nonews_notification():
    sender_email = "alfonsoapariciovega@gmail.com"
    receiver_email = "alfonsoapariciovega@gmail.com"  # Cambia esto al email donde quieres recibir la alerta
    password = "kdbppwebtkjgwpof"

    subject = "¡SIN NOVEDADES en Grimey: Grimey x Palestina VI!"
    body = "NO se ha detectado una nueva entrada en el blog de Grimey sobre 'Grimey x Palestina VI'. ¡Revisa la web ahora!"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("📩 Correo enviado con éxito.")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")

check_grimey_blog()
# Programar para que se ejecute todos los días a las 12:00 PM
# schedule.every().day.at("12:00").do(check_grimey_blog)

# print("⏳ Script en ejecución. Comprobará la web todos los días a las 12:00 PM.")
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Revisa cada minuto si hay tareas programadas
