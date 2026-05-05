from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .models import Message
from .forms import MessageForm


@login_required
def inbox(request):
    msgs = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging/inbox.html', {'msgs': msgs})


@login_required
def sent_box(request):
    msgs = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent.html', {'msgs': msgs})


@login_required
def message_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.receiver == request.user and not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'messaging/message_detail.html', {'msg': msg})


@login_required
def message_send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            django_messages.success(request, '¡Mensaje enviado!')
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send.html', {'form': form})


@login_required
def message_delete(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        msg.delete()
        django_messages.success(request, 'Mensaje eliminado.')
        return redirect('inbox')
    return render(request, 'messaging/message_confirm_delete.html', {'msg': msg})
