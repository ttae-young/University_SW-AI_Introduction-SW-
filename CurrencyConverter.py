import requests

class CurrencyConverter:
    """기본 화폐 변환기 클래스"""
    def __init__(self, base_currency, target_currency):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = None

    def get_rate(self):
        """환율 API에서 가져오는 메소드"""
        api_key = "b99f132ee63b480f3282143d" #내 키임
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{self.base_currency}"
        response = requests.get(url)
        data = response.json() #json형식으로
        self.rate = data['conversion_rates'][self.target_currency]
        return self.rate

    def convert(self, amount):
        """금액 변환"""
        rate = self.get_rate()
        return amount * rate


class JPYtoKRW(CurrencyConverter):
    """엔화 -> 원화 변환"""
    def __init__(self):
        super().__init__("JPY", "KRW")

class KRWtoJPY(CurrencyConverter):
    """원화 -> 엔화 변환""" 
    def __init__(self):
        super().__init__("KRW", "JPY")



