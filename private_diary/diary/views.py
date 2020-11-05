import logging

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

from django.contrib import messages

logger = logging.getLogger(__name__) # ロガー取得

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry') #指定URLにリダイレクト

    def form_valid(self, form):
        form.send_email() # メール送信メソッド
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name'])) # ビューからログを出力
        return super().form_valid(form)

