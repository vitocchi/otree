from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'network_externality'
    players_per_group = 12
    price = c(100)
    externality = c(30)
    reservation_prices = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
    reservation_prices_ex = [10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 90]
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1 :
            random_sampled = random.sample(Constants.reservation_prices, 12)
        else:
            random_sampled = random.sample(Constants.reservation_prices_ex, 12)
        players = self.get_players()
        for i in range(len(players)):
            reservation_price = random_sampled[i]
            players[i].reservation_price = c(reservation_price)
    pass


class Group(BaseGroup):
    num_of_bought = models.IntegerField(initial=0)
    def increment_num_of_bought(self, id_in_group, payload):
        self.num_of_bought += 1
        return {0: self.num_of_bought}

    def set_payoffs(self):
        players = self.get_players()
        for p in players:
            if p.will_buy:
                p.payoff  = p.reservation_price + Constants.externality * self.num_of_bought - Constants.price
            else:
                p.payoff = c(0)
    pass


class Player(BasePlayer):
    reservation_price = models.CurrencyField()
    will_buy = models.BooleanField()
    pass
