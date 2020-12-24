from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import QuesForm, QuesUpdateForm


@login_required
def ques(request):
    if request.method == 'POST':
        q_form = QuesUpdateForm(request.POST,
                                     instance=request.user.ques)
        if q_form.is_valid():
            q_form.save()
            messages.success(request, f'您填写的问卷已更新！')
            return redirect('ques')

    else:
        q_form = QuesUpdateForm(instance=request.user.ques)

    context = {
        'q_form': q_form
    }

    return render(request, 'sgpa/ques.html', context)
