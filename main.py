from datetime import datetime
import base64

class Email:
    def __init__(self, sender, recipiant, contents, date=str(datetime.now().date())):
        self.sender = sender
        self.recipiant = recipiant
        self.date = date
        self.contents = contents

    def edit_contents(self, newContents):
        self.contents = newContents

    def __str__(self):
        s = 'From: ' + self.sender + '\n'
        s += 'To: ' + self.recipiant + '\n'
        s += 'Date: ' + self.date + '\n'
        s += '\n' + self.contents
        return s

def serializeEmail(email):
    sender_encoded = base64.b64encode(email.sender.encode('UTF-8'))
    recipiant_encoded = base64.b64encode(email.recipiant.encode('UTF-8'))
    date_encoded = base64.b64encode(email.date.encode('UTF-8'))
    contents_encoded = base64.b64encode(email.contents.encode('UTF-8'))

    print('Base 64 sender: ')
    print(str(sender_encoded))
    print()

    print('Base 64 recipiant: ')
    print(str(recipiant_encoded))
    print()

    print('Base 64 date: ')
    print(str(recipiant_encoded))
    print()

    print('Base 64 contents: ')
    print(str(contents_encoded))
    print()

    f = open('serializedEmail.txt', 'w')
    f.write(sender_encoded.decode('utf-8') + "/" + recipiant_encoded.decode('utf-8') + '/' + date_encoded.decode('utf-8') + '/' + contents_encoded.decode('utf-8') + '/')
    f.close()

def deserializeEmail():
    f = open('serializedEmail.txt')
    serialized_email = f.read()
    f.close()

    print('Serialized email: ')
    print(serialized_email)
    print()

    # sender
    i1 = 0
    i2 = serialized_email.find('/', i1)
    serialized_sender = serialized_email[i1:i2]
    sender_unicode = base64.b64decode(serialized_sender)
    sender = sender_unicode.decode('utf-8')

    # recipiant
    i3 = serialized_email.find('/', i2 + 1)
    serialized_recipiant = serialized_email[i2 + 1:i3]
    recipiant_unicode = base64.b64decode(serialized_recipiant)
    recipiant = recipiant_unicode.decode('utf-8')

    # date
    i4 = serialized_email.find('/', i3 + 1)
    serialized_date = serialized_email[i3 + 1:i4]
    date_unicode = base64.b64decode(serialized_date)
    date = date_unicode.decode('utf-8')

    # contents
    i5 = serialized_email.find('/', i4 + 1)
    serialized_contents = serialized_email[i4 + 1:i5]
    contents_unicode = base64.b64decode(serialized_contents)
    contents = contents_unicode.decode('utf-8')

    # create email instance for the deserialized info
    return_email = Email(sender, recipiant, contents, date=date)
    return return_email
    

if __name__ == '__main__':
    before_email = Email('John', 'Sarah', 'Hi Sarah, my name is John.')
    print('Email before serializer: ')
    print(str(before_email))
    print()

    serializeEmail(before_email)
    after_email = deserializeEmail()

    print('Email after deserializer: ')
    print(str(after_email))