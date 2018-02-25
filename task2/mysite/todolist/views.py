from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Affair


def index(request):
    active_affairs = Affair.objects.filter(is_done=False)
    inactive_affairs = Affair.objects.filter(is_done=True)
    context = {'active_affairs': active_affairs,
               'inactive_affairs': inactive_affairs}
    return render(request, 'todolist/index.html', context)


def doer(request, affair_id):
    affair = get_object_or_404(Affair, pk=affair_id)
    try:
        action = request.POST['doer']
    except KeyError:
        return HttpResponseRedirect(reverse('todolist:index'))
    else:
        if action == 'Done!' or action == 'Undone!':
            affair.is_done = not affair.is_done
            affair.save()
        return HttpResponseRedirect(reverse('todolist:index'))


def adder(request):
    try:
        affair_text_ = request.POST['new_affair']
        new_affair = Affair(affair_text=affair_text_, pub_date=timezone.now())
        new_affair.save()
        return HttpResponseRedirect(reverse('todolist:index'))
    except KeyError:
        return HttpResponseRedirect(reverse('todolist:index'))
