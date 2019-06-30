from django.views.generic import TemplateView, FormView, DetailView, ListView, CreateView , UpdateView, DeleteView
from pastes.forms import pasteform
from django.urls import reverse
from pastes.models import Paste
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

class HomepageView(CreateView):
    template_name = 'website/index.html'
    form_class = pasteform
    success_message = "Message sent successfully"
    
    def get_success_url(self):
        return reverse('home')
        # return reverse('home') + '?success=True'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pastes'] = Paste.objects.all().order_by('-created')
        # data['current_user'] = self.request.user
        return data

    # def get_initial(self):
    #     initial = super(HomepageView, self).get_initial()
    #     initial.update({'author': self.request.user})
    #     print(self.request.user)
    #     return initial
    #
    #
    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated:
            print("dasda")

            self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'website/signup.html'

class PasteDetailView(DetailView):
    model = Paste
    template_name = 'website/paste_detail.html'

class PasteUpdateView(UpdateView):
    model = Paste
    template_name = 'website/paste_edit.html'
    fields = ['name','code']
    success_url = reverse_lazy('home')

class PasteDeleteView(DeleteView):
    model = Paste
    template_name = 'website/paste_delete.html'
    success_url = reverse_lazy('home')