import smtplib
import config
import checker
import pprint

pprint.PrettyPrinter(indent=4).pprint(checker.get_new_in_radius(config.radius))

# server = smtplib.SMTP(config.host, config.port)
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login(config.username, config.password)
# server.sendmail(config.sender, config.receiver, "yeet".encode("utf8"))
# server.quit()
