#!/usr/bin/python3

from app.models.user import User
from app.models import storage
u = {'username': 'john', 'email': 'john@example.com', 'password_hash': 'password_hash_example'}
u = User(**u)

print(u)

u.save()

user = storage.all(User)

print(user.values())
