from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Bookshelf

class BookForm(ModelForm):
    class Meta:
        model = Bookshelf
        fields = ('judul', 'penulis', 'tahun')
        labels = {
            'judul': _('Judul'),
            'penulis': _('Penulis'),
            'tahun': _('Tahun')
        }
        error_messages = {
            'judul': {
                'required': _("Judul harus diisi."),
            },
            'penulis': {
                'required': _("Penulis harus diisi."),
            },
            'tahun': {
                'required': _("Tahun harus diisi."),
            },
        }