import pytest
import requests
from Base.read_json_data import read_data


class TestAPI:
    @pytest.mark.parametrize("user_id, user_name, user_email, user_phone, user_city, user_zipcode, user_street, user_company_name",
                             read_data('../data_files/api_data.json'))
    def test_api(self, user_id, user_name, user_email, user_phone, user_city, user_zipcode, user_street, user_company_name):
        self.api_url = "https://jsonplaceholder.typicode.com/users"
        self.parameters = {"id": user_id}
        self.response = requests.get(self.api_url, params=self.parameters).json()[0]
        print("checking user's name...")
        assert self.response['name'] == user_name
        print("checking user's email...")
        assert self.response['email'] == user_email
        print("checking user's phone...")
        assert self.response['phone'] == user_phone
        print("checking user's city...")
        assert self.response['address']['city'] == user_city
        print("checking user's zipcode...")
        assert self.response['address']['zipcode'] == user_zipcode
        print("checking user's street...")
        assert self.response['address']['street'] == user_street
        print("checking user's company name...")
        assert self.response['company']['name'] == user_company_name
