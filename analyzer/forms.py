from django import forms
from analyzer.models import Preset
import datetime

class DateRangePresetForm(forms.ModelForm):
    class Meta:
        model = Preset
        fields = ['name', 'start_date', 'end_date', 'image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['preset_type'] = 'date_range'
        if not kwargs.get('instance'):
            today = datetime.date.today()
            first_day = today.replace(day=1)
            self.initial['start_date'] = first_day
            self.initial['end_date'] = today

class KeywordSearchPresetForm(forms.ModelForm):
    class Meta:
        model = Preset
        fields = ['name', 'keywords', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['preset_type'] = 'keyword_search'
        self.fields['keywords'].widget.attrs.update({'placeholder': 'Comma-seperared values e.g., Amazon, Netflix, Salary'})

class AmountFilterPresetForm(forms.ModelForm):
    class Meta:
        model = Preset
        fields = ['name', 'amount_value', 'comparison_type', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['preset_type'] = 'amount_filter'
        self.fields['amount_value'].widget.attrs.update({'placeholder': 'e.g., 1000'})
