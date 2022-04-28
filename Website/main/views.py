from django.shortcuts import render


# index.html 파일 렌더링.
def main(request):
    return render(request, 'index.html')