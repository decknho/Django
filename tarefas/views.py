from django.shortcuts import render

def home(request):
    """
    Render the home page for the tarefas app.
    """
    return render(request, 'tarefas/home.html')