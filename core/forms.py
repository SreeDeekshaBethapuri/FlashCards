from django import forms
from.models import Flashcard

class FlashcardForm(forms.ModelForm):
    keyword = forms.CharField(
        max_length=50,
        required= True,
        error_messages={
        'required': "The keyword is empty, buddy!"
    }
    )
    definition = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea,
        error_messages={
        'required': "Definition cannot be empty, buddy!"
    }
    )
    class Meta:
        model = Flashcard
        fields = ['keyword', 'definition']
        widgets = {
            'keyword' : forms.TextInput(attrs={
                'placeholder' : 'Enter Keyword (e.g., Gradient, DNN, etc.)',
                'class' : 'form-input'
            }),
            'definition' : forms.Textarea(attrs={
                'placeholder' : 'Enter the definition here',
                'rows' : 4,
                'class' : 'form-text-area'
            }),
        }
    def clean_keyword(self):
        print("clean keyword called")
        keyword = self.cleaned_data.get('keyword')
        if not keyword or keyword.strip() == '':
            raise forms.ValidationError("The keyword is empty, buddy!")
        if len(keyword) > 10:
            raise forms.ValidationError("Whoa! That keyword is *too* long. 100 chars max plz.")
        return keyword
    
    def clean_definition(self):
        print("clean_definition called")
        definition = self.cleaned_data.get('definition')
        if not definition or definition.strip() == '':
            raise forms.ValidationError("Defintion cannot be empty, buddy!")
        if len(definition) > 1000:
            raise forms.ValidationError("WOAH EASY THERE TIGER! We don't want the definition to be too long for a flashcard. How does 1000 character sound?? Try and keep it between that huh")
        return definition