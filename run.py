from time import sleep

from connectivity.bitstamp_api import BitstampAPI
from connectivity.feeds import NewsAPI


class Trading:
    def __init__(self):
        self.market_api = BitstampAPI()
        self.news_api = NewsAPI()
        self.market_api.register_observer(self)
        self.news_api.register_observer(self)

        self.market_api.start()
        self.news_api.start()

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)

    def run(self):
        while True:
            # self.market_api.notify_observers('test')
            self.news_api.notify_observers('test')
            sleep(1)


def run():
    trd = Trading()
    trd.run()


if __name__ == '__main__':
    run()