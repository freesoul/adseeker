# -*- encoding: utf-8 -*-

import logging
import json
import os
import importlib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from modules.milanuncios import Milanuncios


class Adseeker():


    def __init__(self):

        self._set_logger();
        self.logger.info("Starting")

        self._load_config()
        self.logger.info("Loaded configuration")

        self._load_modules()

        self.ads = []



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
            self.emails = json.loads(data)

            with open("config_queries.json", "r") as f:
                data = f.read()
            self.queries = json.loads(data)

        except Exception as e:
            self.logger.warning("Failed to load config_emails.json or config_queries.json")
            self.logger.error(str(e))
            exit(0)



    def _load_modules(self):
        self.modules = {}
        module_files = [item for item in os.listdir('modules') if item[-3:]=='.py']
        for module_file in module_files:
            module_name = module_file[:-3]
            module_class_name = module_name.title()
            module_lib = importlib.import_module('modules.{0}'.format(module_name))
            module_class = getattr(module_lib, module_class_name)
            self.modules[module_name.lower()] = module_class
            self.logger.info("Loaded module: {0}".format(module_name))



    def email_ads(self):
        pass



    def _email(self, config, _msg):

        # if len(ads) == 0:
        #     self.logger.info("Skipping emails (0 interesting ads)")
        #     return False

        try:
            email_notifier = self.emails[config['notifier']]
            email_notify = self.emails[config['notify']]
        except:
            self.logger.info("Email data missing")
            return False

        # msg = "\r\n".join([
        #   "From: {0}".format(email_notifier['email_address']),
        #   "To: {0}".format(email_notify['email_address']),
        #   "Subject: Ads report",
        #   "Content-Type: text/html; charset=UTF-8",
        #   "",
        #   msg # format this for a better report
        #   ])


        msg = MIMEMultipart('alternative')
        msg.set_charset('utf8')
        msg['From'] = email_notifier['email_address']
        msg['To'] = email_notify['email_address']
        msg['Subject'] = Header(
            'Ads report'.encode('utf-8'),
            'UTF-8'
        ).encode()
        msg.attach(MIMEText(_msg.encode('utf-8'), 'html', 'UTF-8'))  



        try:
            server = smtplib.SMTP(email_notifier['email_smtp'])
            server.ehlo()
            server.starttls()
            server.login(email_notifier['email_address'],email_notifier['email_password'])
            server.sendmail(email_notifier['email_address'], email_notify['email_address'], msg.as_string())
            server.quit()
        except Exception as e:
            self.logger.info("Failed sending mail")
            self.logger.info(str(e))
            return False

        return True



    def run_at(self, dt):
        pass



    def run_once(self):

        for query in self.queries:
            for module in query['modules']:
                module_key = module.lower()
                if not module_key in self.modules: continue

                module_obj = self.modules[module_key]()

                ads = module_obj.query(**query['query_args'])

                if ads: self.ads = self.ads + ads

                self._email(query, str(ads)) # test



    def run_each(self):
        pass




adseeker = Adseeker()
adseeker.run_once()
