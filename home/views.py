from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse(
        """
        <h1>Dodomatov Abdusami</h1><br>
        Najot Talim o'quvchisi, Backend Python(django) kursida<br>
        Yoshim 20 da
        
        """
    )
