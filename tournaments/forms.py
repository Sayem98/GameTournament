from django import forms

# Create your forms here

game_type_choices = (('PUBG', 'PUBG'),
                     ('Sea of Theves', 'Sea of Theves'),
                     ('Call of duty', 'Call of Duty'))


class TournamentsForm(forms.Form):
    game_type = forms.ChoiceField(choices=game_type_choices)
    tournament_name = forms.CharField(max_length=30, label='Tournament Name')
    your_email = forms.EmailField(label='Your Email')
    fee = forms.CharField(max_length=5, label='Fee')
    team_numbers = forms.CharField(max_length=2)


