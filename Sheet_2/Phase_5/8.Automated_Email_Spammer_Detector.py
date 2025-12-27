class SpamFilter:
    def __init__(self, spam_keywords):
        self.spam_keywords = spam_keywords

    def filter(self, message):
        for keyword in self.spam_keywords:
            if keyword.lower() in message.body.lower():
                message.is_spam = True
                return True
        return False

class Email:
    def __init__(self,sendor,body):
        self.sendor = sendor
        self.body = body
        self.is_spam = False

filter1 = SpamFilter(['spam','offer','win'])

msg1 = Email("abc@gmail.com", "You win a spam offer")
print(filter1.filter(msg1))