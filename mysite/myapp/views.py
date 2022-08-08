from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # вернем n опубликованных вопросов, исключая те что в будущем
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:100]





