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
        {'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://johndoe.com', 'bio': 'John Doe is a seasoned Django developer with a passion for web development and open source.'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://janesmith.com', 'bio': 'Jane Smith is an experienced Python programmer who loves building APIs and working with Django REST framework.'},
        {'username': 'bob_brown', 'email': 'bob@example.com', 'password': 'password123', 'role': 'suscriber', 'social_website': '', 'bio': 'Bob Brown is a subscriber who enjoys reading about the latest trends in web development.'},
        {'username': 'alice_white', 'email': 'alice@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://alicewhite.com', 'bio': 'Alice White, inspired by Princess Leia, is a Django developer focused on building scalable web applications.'},
        {'username': 'charlie_green', 'email': 'charlie@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://charliegreen.com', 'bio': 'Charlie Green, drawing inspiration from Luke Skywalker, specializes in backend development with Django.'},
        {'username': 'david_black', 'email': 'david@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://davidblack.com', 'bio': 'David Black, inspired by Darth Vader, is a Python enthusiast who loves diving deep into Django.'},
        {'username': 'eve_silver', 'email': 'eve@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://evesilver.com', 'bio': 'Eve Silver, like Rey, is a developer who excels in both frontend and backend development.'},
        {'username': 'frank_grey', 'email': 'frank@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://frankgrey.com', 'bio': 'Frank Grey, inspired by Han Solo, has a knack for solving complex problems with Django and Python.'},
        {'username': 'grace_yellow', 'email': 'grace@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://graceyelllow.com', 'bio': 'Grace Yellow, inspired by Yoda, is a Django master who loves teaching others about web development.'},
        {'username': 'henry_blue', 'email': 'henry@example.com', 'password': 'password123', 'role': 'author', 'social_website': 'https://henryblue.com', 'bio': 'Henry Blue, drawing inspiration from Obi-Wan Kenobi, is a seasoned developer who enjoys mentoring newcomers.'}
    ]

    for user in user_data:
        u, created = User.objects.get_or_create(username=user['username'], defaults={'email': user['email']})
        if created:
            u.set_password(user['password'])
            u.save()
        profile, created = Profile.objects.get_or_create(user=u)
        profile.role = user['role']
        profile.social_website = user['social_website']
        profile.bio = user['bio']
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
        },
        {
            'title': 'Advanced Django Querying',
            'slug': 'advanced-django-querying',
            'content': 'Explore advanced querying techniques in Django to efficiently retrieve data from your database.',
        },
        {
            'title': 'Django Admin Customization',
            'slug': 'django-admin-customization',
            'content': 'Learn how to customize the Django admin interface to better suit your project’s needs.',
        },
        {
            'title': 'Testing in Django',
            'slug': 'testing-in-django',
            'content': 'A guide to writing tests in Django to ensure your application works as expected.',
        },
        {
            'title': 'Deploying Django Applications',
            'slug': 'deploying-django-applications',
            'content': 'Best practices for deploying Django applications to production environments.',
        },
        {
            'title': 'Securing Django Applications',
            'slug': 'securing-django-applications',
            'content': 'Learn how to secure your Django applications against common security threats.',
        },
        {
            'title': 'Using Celery with Django',
            'slug': 'using-celery-with-django',
            'content': 'An introduction to using Celery for background task processing in Django projects.',
        },
        {
            'title': 'Integrating Django with React',
            'slug': 'integrating-django-with-react',
            'content': 'How to integrate Django with React to build modern web applications.',
        },
        {
            'title': 'Building RESTful APIs with Django',
            'slug': 'building-restful-apis-with-django',
            'content': 'Learn how to build RESTful APIs using Django and Django REST Framework.',
        },
        {
            'title': 'Django Performance Optimization',
            'slug': 'django-performance-optimization',
            'content': 'Tips and techniques for optimizing the performance of your Django applications.',
        },
        {
            'title': 'Working with Django Signals',
            'slug': 'working-with-django-signals',
            'content': 'An overview of using signals in Django to handle events and trigger actions.',
        },
        {
            'title': 'Django Middleware Explained',
            'slug': 'django-middleware-explained',
            'content': 'Understanding middleware in Django and how to create custom middleware for your projects.',
        },
        {
            'title': 'Internationalization in Django',
            'slug': 'internationalization-in-django',
            'content': 'How to internationalize and localize your Django applications for multiple languages.',
        },
        {
            'title': 'Using Django Channels',
            'slug': 'using-django-channels',
            'content': 'Learn how to use Django Channels to add WebSocket support to your Django applications.',
        },
        {
            'title': 'Working with Django Forms',
            'slug': 'working-with-django-forms',
            'content': 'A comprehensive guide to creating and handling forms in Django.',
        },
        {
            'title': 'Django Templating Engine',
            'slug': 'django-templating-engine',
            'content': 'An introduction to the Django templating engine and how to use it effectively.',
        },
        {
            'title': 'Building E-commerce Sites with Django',
            'slug': 'building-e-commerce-sites-with-django',
            'content': 'Steps to create a fully functional e-commerce site using Django.',
        },
        {
            'title': 'Django Authentication and Authorization',
            'slug': 'django-authentication-and-authorization',
            'content': 'Implementing authentication and authorization in Django applications.',
        }
    ]

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