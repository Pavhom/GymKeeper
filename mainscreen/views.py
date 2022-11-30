from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, auth_logout, login_required, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Exercise, Note, Photo, Chart, ChartData
from .forms import PostForm, ExerciseForm, RegisterUserForm, NoteForm, AddPhotoForm, ChartForm, ChartDataForm, PasChangeForm
from django.db.models import Sum
from django.core.paginator import Paginator


def get_page_context(queryset, request):
    """pagination function"""
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page


class TrainingsView(LoginRequiredMixin, CreateView):
    """displays a list of workouts, saves new ones.
    Pagination is also enabled via get_context_data.
    Through form_valid each workout is assigned the current user as the author"""
    model = Post
    form_class = PostForm
    template_name = 'mainscreen/post_list.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trainings = self.model.objects.filter(author=self.request.user).order_by('created_date')[::-1]
        context["page"] = get_page_context(trainings, self.request)
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        fields.save()
        return super().form_valid(form)


class NotesView(LoginRequiredMixin, CreateView):
    """displays a list of notes, saves new ones.
    Pagination is also enabled via get_context_data.
    Through form_valid each note is assigned the current user as the author"""
    model = Note
    form_class = NoteForm
    template_name = 'mainscreen/notes.html'
    success_url = reverse_lazy('notes_list')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes = self.model.objects.filter(author=self.request.user).order_by('created_date')[::-1]
        context["page"] = get_page_context(notes, self.request)
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        fields.save()
        return super().form_valid(form)


# class ChartsView(LoginRequiredMixin, CreateView):
#     """displays a list of charts, saves new ones.
#     Through form_valid each note is assigned the current user as the author"""
#     model = Chart
#     form_class = ChartForm
#     template_name = 'mainscreen/chart.html'
#     success_url = reverse_lazy('chart')
#     login_url = 'login'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page"] = self.model.objects.filter(author=self.request.user).order_by('created_date')[::-1]
#         return context
#
#     def form_valid(self, form):
#         fields = form.save(commit=False)
#         fields.author = self.request.user
#         fields.save()
#         return super().form_valid(form)
#
#
# class ChartDetailView(LoginRequiredMixin, CreateView):
#     """displays a list of data within the chart, saves new ones.
#     Through form_valid, chartdata are linked to chart"""
#     model = ChartData
#     form_class = ChartDataForm
#     template_name = 'mainscreen/chart_detail.html'
#     login_url = 'login'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['chart'] = get_object_or_404(Chart, pk=self.kwargs['pk'])
#         context['chart_data'] = self.model.objects.filter(chart_pk=self.kwargs.get('pk'))
#         return context
#
#     def form_valid(self, form):
#         fields = form.save(commit=False)
#         fields.chart_pk = get_object_or_404(Chart, pk=self.kwargs['pk'])
#         fields.save()
#         return super().form_valid(form)


class PhotosView(LoginRequiredMixin, CreateView):
    """displays all photos, saves new ones.
    Through form_valid each photo is assigned the current user as the author"""
    model = Photo
    form_class = AddPhotoForm
    template_name = 'mainscreen/photo.html'
    success_url = reverse_lazy('photo')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = self.model.objects.filter(author=self.request.user).order_by('created_date')[::-1]
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        fields.save()
        return super().form_valid(form)


class TrainingsDetailView(LoginRequiredMixin, CreateView):
    """displays a list of exercises within the workout, saves new ones.
    Through form_valid, exercises are linked to training"""
    model = Exercise
    form_class = ExerciseForm
    template_name = 'mainscreen/training_detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exrcise_list = self.model.objects.filter(tr_post=self.kwargs.get('pk')).order_by('id')
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['exercise'] = exrcise_list
        context['total_tonnage'] = exrcise_list.aggregate(Sum('exercise_tonnage'))['exercise_tonnage__sum']
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.tr_post = get_object_or_404(Post, pk=self.kwargs['pk'])
        fields.save()
        return super().form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'mainscreen/note_edit.html'
    success_url = reverse_lazy('notes_list')
    login_url = 'login'


class TrainingDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'mainscreen/delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'


class ExerciseDelete(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'mainscreen/exercise_delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('training_detail', kwargs={'pk': self.object.tr_post_id})


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'mainscreen/note_delete.html'
    success_url = reverse_lazy('notes_list')
    login_url = 'login'


class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'mainscreen/photo_delete.html'
    success_url = reverse_lazy('photo')
    login_url = 'login'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainscreen/register.html'
    success_url = reverse_lazy('login')


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = PasChangeForm
    template_name = 'mainscreen/password_change.html'
    success_url = reverse_lazy('password_change_done')


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'mainscreen/password_change_done.html'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'mainscreen/login.html'


def logout_user(request):
    auth_logout(request)
    return redirect('login')
