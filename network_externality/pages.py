from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['will_buy']
    live_method = 'increment_num_of_bought'
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):
        return dict(profit=self.player.profit())
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
