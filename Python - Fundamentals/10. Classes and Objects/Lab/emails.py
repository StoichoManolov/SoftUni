class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_content = []

while True:
    command = input()
    if command == 'Stop':
        break

    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails_content.append(email)

index = [int(x) for x in input().split(', ')]

for x in index:
    emails_content[x].send()

for emails in emails_content:
    print(emails.get_info())

