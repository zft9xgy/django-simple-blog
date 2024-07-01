from blog.models import Tag


def global_variables(request):
    """
    Variables globales que serán lanzadas en todas las templates.
    """
    
    menuTags = Tag.get_tags_by_post(3)

    websiteTitle='Keep it simple.'
    websiteTagline="A simple blog made with Django"
    aboutFooter = "About del footer."

    context = {
        'menuTags': menuTags,
        'websiteTitle': websiteTitle,
        'websiteTagline': websiteTagline,
        'aboutFooter':aboutFooter,
    }
    return {'global': context}