from django import forms



class addSerialForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    season = forms.IntegerField(initial=0)
    counter = forms.IntegerField(initial=0)



class searchForm(forms.Form):

    search = forms.CharField(max_length=100)