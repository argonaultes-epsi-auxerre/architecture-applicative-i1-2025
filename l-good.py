from abc import ABC, abstractmethod

class Contact:

    def __init__(self, name : str, email : str, phone : str):
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def email(self) -> str :
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def discord(self):
        return self.__discord

    @discord.setter
    def discord(self, discord):
        self.__discord = discord

class Notification(ABC):

    def __init__(self, contact):
        self._contact = contact

    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):

    def notify(self, message):
        print(f'Send {message} to {self._contact.email}')


class SMS(Notification):
    def notify(self, message):
        print(f'Send {message} to {self._contact.phone}')

class Discord(Notification):
    def notify(self, message):
        print(f'Discord send to {self._contact.discord}')

class NotificationManager:

    def __init__(self, notification):
        self.__notification = notification

    def send(self, message):
        self.__notification.notify(message)

    @property
    def notification(self):
        return self.__notification

    @notification.setter
    def notification(self, notification):
        self.__notification = notification

if __name__ == '__main__':
    president = Contact('president', 'president@lafrance.fr', '01010101')
    president.discord = 'president#1213'
    sms_notif = SMS(president)
#    sms_notif.notify('Hello')
    email_notif = Email(president)
#    email_notif.notify('Hello')

    notifManager = NotificationManager(sms_notif)
    notifManager.send('hello hello')
    notifManager.notification = email_notif
    notifManager.send('hello hello')
    notifManager.notification = Discord(president)
    notifManager.send('hello hello')


