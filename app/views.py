from django.shortcuts import render

# View для главной страницы
def main_view(request):
    return render(request, 'app/index.html')