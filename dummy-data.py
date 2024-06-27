from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Profile, Post, Tag  # Asegúrate de que el nombre del módulo sea correcto
import uuid

# Crear usuarios de prueba
#user1 = User.objects.create_user(username='dev_guru', password='password123')
#user2 = User.objects.create_user(username='marketing_master', password='password123')

# Crear perfiles de prueba
#profile1 = Profile.objects.create(user=user1, username='dev_guru', bio='Expert in Python development and web technologies.')
#profile2 = Profile.objects.create(user=user2, username='marketing_master', bio='Specialist in digital marketing strategies.')

# Crear etiquetas de prueba
tag1 = Tag.objects.create(name='Python', slug='python')
tag2 = Tag.objects.create(name='Django', slug='django')
tag3 = Tag.objects.create(name='Web Development', slug='web-development')
tag4 = Tag.objects.create(name='Digital Marketing', slug='digital-marketing')
tag5 = Tag.objects.create(name='SEO', slug='seo')

# Contenido de prueba en formato Markdown
content1 = """
# Introduction to Python

Python is a versatile language that you can use on the backend, frontend, or full stack of a web application. It's known for its readability and simplicity.

## Key Features
- Easy to learn and use
- Extensive libraries and frameworks
- Versatile for different applications

Learn Python to enhance your web development skills and build robust applications efficiently.
"""

content2 = """
# Getting Started with Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Why Django?
- Fast development
- Scalable
- Secure

Using Django, you can build powerful web applications with less code and in less time.
"""

content3 = """
# Web Development Trends in 2024

The web development landscape is constantly evolving. Here are the top trends to watch in 2024:

## Trends
1. Progressive Web Apps (PWA)
2. Artificial Intelligence (AI)
3. Single Page Applications (SPA)

Stay updated with these trends to remain competitive in the market.
"""

content4 = """
# Digital Marketing Strategies

In the digital age, marketing strategies have evolved significantly. Here are some effective strategies:

## Strategies
- Content Marketing
- Social Media Engagement
- Email Campaigns

Implement these strategies to enhance your digital presence and reach a wider audience.
"""

content5 = """
# Understanding SEO

Search Engine Optimization (SEO) is crucial for the visibility of your website. Here are some basic tips:

## Tips
- Use relevant keywords
- Optimize your website's speed
- Create high-quality content

Focus on SEO to improve your search engine rankings and attract more visitors to your site.
"""

# Crear publicaciones de prueba
post1 = Post.objects.create(
    title='Introduction to Python',
    slug='introduction-to-python',
    author=user1.profile,
    content=content1,
    published_date=timezone.now(),
    status='published'
)
post2 = Post.objects.create(
    title='Getting Started with Django',
    slug='getting-started-with-django',
    author=user1.profile,
    content=content2,
    published_date=timezone.now(),
    status='published'
)
post3 = Post.objects.create(
    title='Web Development Trends in 2024',
    slug='web-development-trends-2024',
    author=user1.profile,
    content=content3,
    published_date=timezone.now(),
    status='draft'
)
post4 = Post.objects.create(
    title='Digital Marketing Strategies',
    slug='digital-marketing-strategies',
    author=user2.profile,
    content=content4,
    published_date=timezone.now(),
    status='published'
)
post5 = Post.objects.create(
    title='Understanding SEO',
    slug='understanding-seo',
    author=user2.profile,
    content=content5,
    published_date=timezone.now(),
    status='published'
)

# Asignar etiquetas a las publicaciones
post1.tags.add(tag1)
post2.tags.add(tag2, tag3)
post3.tags.add(tag3)
post4.tags.add(tag4)
post5.tags.add(tag5)

print("Datos de prueba creados exitosamente.")
