from django import forms  # type: ignore[import-untyped]

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        Model = Reservation
        fields = '__all__'
    