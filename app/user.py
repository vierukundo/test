#!/usr/bin/python3

from models.user import User
from models import storage
u = {'username': 'Jango', 'email': 'james1@example.com', 'password_hash': 'password_hash_example one'}
u = User(**u)

print(u)

u.save()

user = storage.all(User)

users = user.values()
for user in users:
    print(user)
