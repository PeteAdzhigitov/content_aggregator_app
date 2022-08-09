from django.shortcuts import render
from .models import AvailableSubscription
from django.views.generic import ListView, CreateView
from .forms import SubcribeToSomethingForm
from django.views.generic.edit import FormView

# Create your views here.

# class AvilableSubscriptionList(ListView):
#     form = SubcribeToSomethingForm
#     context_object_name = 'subscriptions'
#     template_name = 'available_subscriptions.html'

def all_available_subscriptions(request):
    c = AvailableSubscription.objects.all()

    a = AvailableSubscription.objects.all()
    b = a.values('feed_name')
    k = []
    for i in b:
        k.append(i)
    g = [x.get('feed_name') for x in k]
    c = AvailableSubscription.objects.all().filter(feed_name__in=g).first()
    form = SubcribeToSomethingForm(instance=c)
    return render(request,'available_subscriptions.html',{"form":form})

#
# def let_update_subscriptions(request):
#     something = AvailableSubscription.objects.get(id=1).name
#     form = SubcribeToSomethingForm(instance=something)
#     context = {"form":form}
#     return render(request,"available_subscriptions.html",context)



# class SomeFormView(CreateView):
#     model = AvailableSubscription
#     form = SubcribeToSomethingForm
#     context_object_name = 'form'
#     template_name = "available_subscriptions.html"
#     # success_url = "available_subscriptions/"

# class AvailableSubscriptionsListView(FormView):
# #     form = SubcribeToSomethingForm
#     model = AvailableSubscription
#     template_name = "available_subscriptions.html"
#     context_object_name = 'form'
    # form = AvailableSubscriptionsForm()
    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)

# def subscribe(request):
#
#         context = {"form":form}
#         return render(request,"available_subscriptions.html",context)




