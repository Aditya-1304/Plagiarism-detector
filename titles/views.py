from django.shortcuts import render
from .models import Title
from .utils import preprocess_title, compute_similarity

def check_similarity(request):
    if request.method == 'POST':
        new_title = request.POST.get('title')

        existing_titles = [t.title for t in Title.objects.all()]
        var = ""
        if new_title in existing_titles:
            var = "high"
            results = {"title": new_title, "msg": "yes exists","var": var,"existing_titles": existing_titles}
        else: 
            var = "less"
            results = {"title": new_title, "msg": "no exists","var": var, "existing_titles": existing_titles}

    
        return render(request, 'titles/similarity_results.html', {'results': results})
    return render(request, 'titles/similarity_form.html')