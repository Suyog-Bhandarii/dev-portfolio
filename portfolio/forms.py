from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80, label='Your name')
    email = forms.EmailField(label='Your email')
    message = forms.CharField(max_length=2000, label='Your message', widget=forms.Textarea)
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_website(self):
        website = self.cleaned_data['website']
        if website:
            raise forms.ValidationError('This submission could not be sent.')
        return website