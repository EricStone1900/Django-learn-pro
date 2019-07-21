from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
from django.urls.base import reverse
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DayArchiveView,
    DetailView,
    RedirectView,
    UpdateView,
)

from cueeneh.forms import QuestionForm
from cueeneh.models import Question, Answer
# Create your views here.
class AskQuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'cueeneh/ask.html'

    def get_initial(self):
    	# print(self.request.user.id)
    	# print('user id is {}'.format(self.request.user.id))
        return {
            'user': self.request.user.id
        }

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            # save and redirect as usual.
            print('Save user id is {}'.format(self.request.user.id))
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Question(
                question=form.cleaned_data['question'],
                title=form.cleaned_data['title'])
            ctx = self.get_context_data(preview=preview)
            return self.render_to_response(context=ctx)
        return HttpResponseBadRequest()