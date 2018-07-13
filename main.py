# -*- encoding: utf-8 -*-

import logging
import json

import smtplib

from modules.milanuncios import Milanuncios


class Adseeker():


    def __init__(self):

        self._set_logger();
        self.logger.info("Starting")

        self._load_config()
        self.logger.info("Loaded configuration")



    def _set_logger(self):

        logFormatter = logging.Formatter("%(asctime)s:  %(message)s")
        self.logger = logging.getLogger('adseeker')

        fileHandler = logging.FileHandler("adseeker.log")
        fileHandler.setFormatter(logFormatter)
        self.logger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        self.logger.addHandler(consoleHandler)

        self.logger.setLevel(logging.INFO)




    def _load_config(self):

        try:
            with open("config_emails.json", "r") as f:
                data = f.read()
            emails = json.loads(data)

            with open("config_queries.json", "r") as f:
                data = f.read()
            queries = json.loads(data)

        except Exception as e:
            self.logger.warning("Failed to load config_emails.json or config_queries.json")
            self.logger.error(str(e))
            exit(0)



    def email(self, config, ads):

        if len(ads) == 0:
            self.logger.info("Skipping emails (0 interesting ads)")
            return False

        try:
            email_notifier = emails[config['notifier']]
            email_notify = emails[config['notify']]
        except:
            self.logger.info("Email data missing")
            return False

        msg = "\r\n".join([
          "From: {0}".format(email_notifier['email_address']),
          "To: {0}".format(email_notify['email_address']),
          "Subject: Ads report",
          "",
          str(ads) # format this to a better report
          ])

        try:
            server = smtplib.SMTP(email_notifier['email_smtp'])
            server.ehlo()
            server.starttls()
            server.login(email_notifier['email_address'],email_notifier['email_password'])
            server.sendmail(email_notifier['email_address'], email_notify['email_address'], msg)
            server.quit()
        except Exception as e:
            self.logger.info("Failed sending mail")
            self.logger.info(str(e))
            return False

        return True



    def run_at(self, dt):
        pass

    def run_once(self):
        pass

    def run_each(self):
        pass


adseeker = Adseeker()

exit(0)



ret = Milanuncios().query(
                            zona='madrid',
                            desde=150,
                            hasta=400,
                            query='portatil',
                            max_pag=99999, # no limitamos por pagina
                            max_minutes=60*24*2.5, # limitamos por antiguedad: dos dias y medio
                            max_ads=1000, # no limitamos por numero de anuncios
                            filtros=[
                                {
                                    'con'   :   [
                                                    ['(?:12|16)\s*(?:gb|giga)', 'i[78]'], # con mucha ram
                                                    ['(?:12|16)\s*(?:gb|giga)', 'msi', 'ddr5'],
                                                    ['i[678][\-\s][678][0-9]{3}'], # buen procesador
                                                    ['1[0-9]{3}\s*gtx'], # nvidia
                                                    ['9[0-9]{2}\s*gtx'],
                                                    ['1[0-9]{3}\s*(?:gt|rx)'], # radeon
                                                    ['9[0-9]{2}\s*(?:gt|rx)'], 
                                                    ['msi'], # buena marca
                                                    ['urge'] # cosas rebajadas

                                                ],
                                    'sin'   :   [
                                                    #'intel graphics',
                                                    '4\s*(?:gb|giga)',
                                                    'rot[oa]',
                                                    'torre'
                                                ]
                                }

                            ]
                         )
