from django import forms

class ContactForm(forms.Form):
    bankroll = forms.CharField(max_length=20)
    odds = forms.CharField(max_length=10)
    edge = forms.CharField(max_length=10,
        help_text='Write your edge in decimals eg. 0.030 (0.015-0.04 scales to a realistic ROI)'
    )