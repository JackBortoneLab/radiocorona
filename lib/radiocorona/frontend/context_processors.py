from radiocorona.frontend.models import Category

def categories(request):
    return {
        'all_categories': Category.objects.all().order_by('name')
    }
