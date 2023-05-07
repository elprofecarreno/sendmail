from lib import mail

if __name__ == '__main__':
    to_list = 'portalfresia@outlook.com'
    email = 'portalfresia@outlook.com'
    password = '@Portal123'
    mail.send_outlook(to_list, email, password)