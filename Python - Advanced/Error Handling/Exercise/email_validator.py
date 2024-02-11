class NameTooLongError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


DOMAINS = ('com', 'org', 'bg', 'net')

while True:

    emails = input()

    if emails == 'End':
        break

    elif len(emails.split('@')[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif len(emails.split('@')[0]) > 10:
        raise NameTooLongError('Name must be less than 10 characters')

    elif '@' not in emails:
        raise MustContainAtSymbolError("Email must contain @")

    elif emails.split(".")[-1] not in DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print(f'Email is valid')

