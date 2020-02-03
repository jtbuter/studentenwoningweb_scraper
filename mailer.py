import smtplib
import config
import checker
import pprint
import email.mime.multipart as hc
import email.mime.text as bc

def construct_body(urls):
	msg = hc.MIMEMultipart("alternative")

	msg["Subject"] = "Nieuwe beschikbare woningen"
	msg["From"] = config.sender
	msg["To"] = config.receiver

	links = ""

	for url in urls:
		href = "<a href='{:}'>{:}</a><br>".format(url, url)
		links += href

	msg.attach(bc.MIMEText("<html><body>" + links + "</body></html>", "html"))

	return msg.as_string()

def compose_mail(body):
	server = smtplib.SMTP(config.host, config.port)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(config.username, config.password)
	server.sendmail(config.sender, config.receiver, body)
	server.quit()

woningen = checker.get_new_in_radius(config.radius)
urls = []
root_url = "https://www.studentenwoningweb.nl"

for woning in woningen:
    urls.append(root_url + woning["AdvertentieUrl"])

if config.mailing:
	compose_mail(construct_body(urls))
else:
	for url in urls:
		print(url)
