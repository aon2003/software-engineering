from django.test import TestCase
from elsys.models import Car
from datetime import datetime
from unittest.mock import Mock, patch
from elsys.processors.api_processor import ApiProcessor
import json


class TestCarModel(TestCase):
    def setUp(self):
        # called when test is started
        Car.objects.create(color="red", made=datetime.now(), brand="audi",
                           description="red audi", is_electric=False)
        Car.objects.create(color="green", made=datetime.now(), brand="bmw",
                           description="red bmw")
    
    def tearDown(self):
        # called after tests were run
        pass
    
    def test_car_is_red(self):
        assert Car.objects.get(brand="audi").color == "red"
    
    def test_car_is_green(self):
        assert Car.objects.get(brand="bmw").color == "green"
    
    def test_car_sound(self):
        assert Car.objects.get(brand="audi").sound_check() == "brum brum"


class TestC(TestCase):
    @patch("requests.get")
    def test_call_api(self, mocked_requests):
        data = json.load(open('./elsys/comments.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        response = ApiProcessor().longest_comment()
        assert response['id'] == 3
    
    @patch("requests.get")
    def test_call_api2(self, mocked_requests):
        data = json.load(open('./elsys/posts.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        response = ApiProcessor().post_with_longest_title()
        assert response['id'] == 50
