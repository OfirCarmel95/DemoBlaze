import pytest
import requests


class TestAPI:
    @pytest.fixture()
    def setup(self):
        self.api_url = "https://jsonplaceholder.typicode.com/users"
        self.user_id = 4
        self.parameters = {"id": self.user_id}
        self.user_name = "Patricia Lebsack"
        self.user_email = "Julianne.OConner@kory.org"
        self.user_phone = "493-170-9623 x156"
        self.user_city = "South Elvis"
        self.user_zipcode = "53919-4257"
        self.user_street = "Hoeger Mall"
        self.user_company_name = "Robel-Corkery"
        self.response = requests.get(self.api_url, params=self.parameters).json()[0]

    def test_user_name(self, setup):
        assert self.response['name'] == self.user_name

    def test_user_email(self, setup):
        assert self.response['email'] == self.user_email

    def test_user_phone(self, setup):
        assert self.response['phone'] == self.user_phone

    def test_user_city(self, setup):
        assert self.response['address']['city'] == self.user_city

    def test_user_zipcode(self, setup):
        assert self.response['address']['zipcode'] == self.user_zipcode

    def test_user_street(self, setup):
        assert self.response['address']['street'] == self.user_street

    def test_user_company_name(self, setup):
        assert self.response['company']['name'] == self.user_company_name
