import os
import django
import random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simpleblog.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Profile, Tag, Post

def create_users():
    user_data = [
        {'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'bob_brown', 'email': 'bob@example.com', 'password': 'password123', 'role': 'suscriber'},
        {'username': 'alice_white', 'email': 'alice@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'charlie_green', 'email': 'charlie@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'david_black', 'email': 'david@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'eve_silver', 'email': 'eve@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'frank_grey', 'email': 'frank@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'grace_yellow', 'email': 'grace@example.com', 'password': 'password123', 'role': 'author'},
        {'username': 'henry_blue', 'email': 'henry@example.com', 'password': 'password123', 'role': 'author'}
    ]

    for user in user_data:
        u, created = User.objects.get_or_create(username=user['username'], defaults={'email': user['email']})
        if created:
            u.set_password(user['password'])
            u.save()
        profile, created = Profile.objects.get_or_create(user=u)
        profile.role = user['role']
        profile.save()

def create_tags():
    tags = ['django', 'python', 'web development', 'backend', 'api']
    for tag in tags:
        Tag.objects.get_or_create(name=tag, slug=tag.replace(' ', '-'))

def create_posts():
    author_profiles = Profile.objects.filter(role='author')
    tags = Tag.objects.all()

    if not author_profiles.exists():
        print("No authors found. Skipping post creation.")
        return

    post_data = [
        {
            'title': 'Getting Started with Django',
            'slug': 'getting-started-with-django',
            'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.',
        },
        {
            'title': 'Building APIs with Django REST Framework',
            'slug': 'building-apis-with-django-rest-framework',
            'content': 'Django REST framework is a powerful and flexible toolkit for building Web APIs.',
        },
        {
            'title': 'Understanding Django ORM',
            'slug': 'understanding-django-orm',
            'content': 'The Django ORM is the interface used by Django to provide database access.',
        }
    ]

    # Generar 20 publicaciones adicionales con títulos y slugs únicos
    for i in range(1, 21):
        post_data.append({
            'title': f'Example Post {i}',
            'slug': f'example-post-{i}',
            'content': f'This is the content of example post {i}.'
        })

    for post in post_data:
        author = random.choice(author_profiles)
        p, created = Post.objects.get_or_create(
            title=post['title'],
            slug=post['slug'],
            author=author,
            defaults={
                'content': post['content']
            }
        )
        if created:
            # Assign random tags to the post
            p.tags.set(random.sample(list(tags), k=random.randint(1, len(tags))))
            p.save()

def main():
    create_users()
    create_tags()
    create_posts()
    print("Data population complete.")

if __name__ == '__main__':
    main()