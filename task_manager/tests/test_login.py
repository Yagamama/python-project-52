from django.test import Client, TestCase


class TestLogin(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def test_login(self):
        c = Client()
        response = c.post('/login/', {'username': '123', 'password': '123'})
        self.assertTrue(response.status_code == 200)
        