from django import forms

class EasyGuess(forms.Form):
    digit_1 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_2 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_3 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)

class MediumGuess(forms.Form):
    digit_1 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_2 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_3 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_4 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)

class HardGuess(forms.Form):
    digit_1 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_2 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_3 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_4 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)
    digit_5 = forms.ChoiceField(choices=[(0,0), (1,1), (2,2), (3,3), (4,4),(5,5),(6,6),(7,7)], required=True)    

class Difficulty(forms.Form):
    difficulty = forms.MultipleChoiceField(choices=((3,'easy'), (4, 'medium'),(5,'hard')))