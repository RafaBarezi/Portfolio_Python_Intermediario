# import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# criação de um objeto de mensagem
msg = MIMEMultipart()  # criação de um objeto de mensagem.
texto = "Estou enviando um email usando Python"

# Parâmetros
senha = "#Roito1458"
msg["From"] = "rb.contato.email@gmail.com"
msg["To"] = "rafinhabarezi@gmail.com"
msg["Subject"] = "Teste Python"
# criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login na conta para envio
server.login(msg['From'], senha)

# envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

# encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')