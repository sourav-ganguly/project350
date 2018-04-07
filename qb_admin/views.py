from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from add_content.models import Question, UserDetail, RoleTable


# Create your views here.
def detail(request):
    return HttpResponse("Hello admin")


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'qb_admin/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        user_detail = UserDetail.objects.get(user=self.request.user)
        user_group = user_detail.user_group
        user_access = RoleTable.objects.filter(
            user_group=user_group,
            access_name="ACC_PENDING_QUESTION"
        )
        if not user_access:
            return Question.objects.none()

        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')


@login_required
def get_question_accept_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        if 'question_accept' in request.POST:
            question.status = "ACCEPTED"
            question.save()
            return redirect('qb_admin:index')
        elif 'question_delete' in request.POST:
            question.status = "DISCARDED"
            question.save()
            return redirect('qb_admin:index')
