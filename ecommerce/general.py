from .models import *

def global_data(request):
    data= {
        'categoryData': Category.objects.all(),
        'comData':Settings.objects.all(),

    }
    return data
  