users = [
    ('pesho', 'qwe345!'),
    ('gosho', 'passwOrd1'),
    ('penka', '1a2b3c4d'),
]

strongest_pass = [(user, password) for user, password in users if any(ch.islower() for ch in password) and any(ch.isupper() for ch in password) and any(ch.isdigit() for ch in password) and len(password) >= 8]

print(strongest_pass)
