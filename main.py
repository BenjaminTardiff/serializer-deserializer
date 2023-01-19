from datetime import datetime
import base64

class Email:
    def __init__(self, sender, recipiant, contents):
        self.sender = sender
        self.recipiant = recipiant
        self.date = str(datetime.now().date())
        self.contents = contents

    def edit_contents(self, newContents):
        self.contents = newContents

def serializeEmail(email):
    sender_encoded = base64.b64encode(email.sender.encode('UTF-8'))
    recipiant_encoded = base64.b64encode(email.recipiant.encode('UTF-8'))
    date_encoded = base64.b64encode(email.date.encode('UTF-8'))
    contents_encoded = base64.b64encode(email.contents.encode('UTF-8'))

    f = open('serializedEmail.txt', 'w')
    f.write(sender_encoded.decode('utf-8') + "/" + recipiant_encoded.decode('utf-8') + '/' + date_encoded.decode('utf-8') + '/' + contents_encoded.decode('utf-8'))
    f.close()

def deserializeEmail():
    f = open('serializedEmail.txt')
    serialized_email = f.read()
    print(serialized_email)
    f.close()

    # sender unicode
    i1 = 0
    i2 = serialized_email.find('/', i1)
    serialized_sender = serialized_email[i1:i2]
    sender_unicode = base64.b64decode(serialized_sender)

    # recipiant unicode
    i3 = serialized_email.find('/', i2 + 1)
    serialized_recipiant = serialized_email[i2 + 1:i3]
    recipiant_unicode = base64.b64decode(serialized_recipiant)

    print(sender_unicode)
    sender = sender_unicode.decode('utf-8')
    print(sender)
    print()

    print(recipiant_unicode)
    recipiant = recipiant_unicode.decode('utf-8')
    print(recipiant)
    print()

    






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    email1 = Email('John', 'Sarah', 'Hi Sarah, my name is John.')
    serializeEmail(email1)
    deserializeEmail()