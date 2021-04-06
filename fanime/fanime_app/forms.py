from django.forms import ModelForm
from .models import Comment


#making form from comment model only input is the comment
class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']

