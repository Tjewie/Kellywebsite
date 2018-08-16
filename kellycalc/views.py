from django.shortcuts import render
from . import forms
from kellycalc import betformula
from django.http import HttpResponseRedirect


def home(request):
    test_value = 1
    #return HttpResponseRedirect('home')
    return render(request, 'home.html', context={"hello": test_value})


def calculator(request):
    optimum_betsize = 0.0

    if request.session.get("history") is None:
        request.session["history"] = []
        request.session.modified = True

    if request.method == 'POST':
        print('My post:', request.POST)
        form = forms.ContactForm(request.POST)
        if form.is_valid():

            d = {k: float(v) for k, v in form.cleaned_data.items()}
            optimum_betsize = betformula.betsize(d["odds"], d["edge"], d["bankroll"])
            request.session["history"].append((d["odds"], round(optimum_betsize), int(d["bankroll"]), d["edge"]))
            request.session.modified = True

        if 'clear_history' in request.POST:
            def clear_history():
                request.session['history'] = []
            clear_history()



    else:
        form = forms.ContactForm()
    return render(request, 'forms.html', {'form': form, 'result': round(optimum_betsize)})