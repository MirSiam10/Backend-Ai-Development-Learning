from django import forms  # type: ignore[import-untyped]

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
    