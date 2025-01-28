# titles/views.py
from django.http import JsonResponse
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
        
        max_similarity = max(cosine_sim)
        classification = "Too Similar" if max_similarity > 0.8 else "Unique"
        
        response = {
            "new_title": new_title,
            "max_similarity": float(max_similarity),
            "classification": classification,
            "results": results
        }
        return JsonResponse(response)
