from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['will_buy']
    live_method = 'increment_num_of_bought'
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(payoff=self.player.payoff, buy = self.player.will_buy>0)
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
