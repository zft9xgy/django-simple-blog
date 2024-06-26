Django simple blog pretende ser un blog personal inspirado en wordpress, pero minimizandolo y dejandolo solo en lo que considero lo esencial.

En cuanto a tipos de contenido, va a tener los mismos que wordpress page and post.

Las páginas destinadas a contenidos únicos y los post destinados a ser entradas del blog.

En cuanto a taxonomias, pretendo usar solo etiquetas, descartando las categorias.

Opcionales a desarrollar:

- sección de comentarios

Modelo:

USER
id
created_date
username
first_name
last_name
email
password
other django atributes
https://docs.djangoproject.com/en/5.0/ref/contrib/auth/

POST
id
post_creation_date
post_author -> user
post_content -> contenido
post_title
post_excerpt
post_status -> draft, published
post_slug
post_modified_date
