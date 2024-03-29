import logging
import requests
from exchange.platforms.base import BaseExchange


logger = logging.getLogger(__name__)


class Wallex(BaseExchange):
    def get_price(self, coin, market):
        logger.info("Wallex.get_price(%s, %s)", coin, market)
        api_addr = "https://api.wallex.ir/v1/markets"
        try:
            coin = requests.get(api_addr, timeout=10).json()["result"]["symbols"][
                f"{coin}{market}"
            ]
            return round(float(coin["stats"]["lastPrice"]), 2)
        except Exception:
            return None

    def cache_all_prices(self):
        pass
