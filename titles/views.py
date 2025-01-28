from django.shortcuts import render
from .models import Title
from .utils import preprocess_title, compute_similarity

def check_similarity(request):
    if request.method == 'POST':
        new_title = request.POST.get('title')
        existing_titles = [t.title for t in Title.objects.all()]
        
        preprocessed_title = preprocess_title(new_title)
        cosine_sim, fuzzy_sim = compute_similarity(new_title, existing_titles)
        
        results = [{"title": t, "cosine_similarity": float(cosine), "fuzzy_similarity": fuzzy} 
                   for t, cosine, fuzzy in zip(existing_titles, cosine_sim, fuzzy_sim)]
        
        return render(request, 'titles/similarity_results.html', {'results': results})
    return render(request, 'titles/similarity_form.html')