from .models import Test, Question, Option, ANSWER, QUESTION_TYPE
from django import forms
from django.forms import ModelForm

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['test_id','question_type','question_name']

    test_id = forms.ModelChoiceField(queryset=Test.objects.all(), empty_label=None, label='Test',
            widget=forms.Select(
                attrs={
                    'id': "test_id",
                    'title': 'Select a Test',
                    'class': 'selectpicker form-control test_id',
                    'data-style': 'btn btn-primary btn-sm',
                    'data-size': '7',
                }
            )
    )
    question_type = forms.ChoiceField(choices = QUESTION_TYPE, initial='QCM',
            widget=forms.Select(
                attrs={
                    'id': "question_type",
                    'title': 'Select a Test',
                    'class': 'selectpicker form-control question_type',
                    'data-style': 'btn btn-primary btn-sm',
                    'data-size': '7',
                }
            )
    )
    question_name = forms.CharField(label='Question', 
        widget=forms.TextInput(
            attrs={
                'id': "question_name",
                'class': 'form-control question_name',
                'placeholder': 'Add question here...',
            }
        )
    )

class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = ['option_name','answer']
    
    option_name = forms.CharField(label='Option', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Option...',
            }
        )
    )

    answer = forms.ChoiceField(choices = ANSWER, initial='F',
            widget=forms.Select(
                attrs={
                    'title': 'Select an Answer',
                    'class': 'selectpicker ',
                    'data-style': 'btn btn-primary btn-sm',
                    'data-size': '7',
                }
            )
    )