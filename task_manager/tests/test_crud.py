from django.test import Client, TestCase


class TestCRUD(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def setUp(self) -> None:
        return super().setUp()
    
    def test_create(self):
        c = Client()
        context = {
            'first_name': 'aaaa',
            'last_name': 'bbbb',
            'username': 'aaaabbbbcccc',
            'password1': '123',
            'password2': '123',
        }
        response = c.post('/users/create/', context)
        print('assert create')
        self.assertTrue(response.status_code == 302)

        response = c.get('/users/')
        print('assert read')
        self.assertContains(response, 'aaaa bbbb')
    
    # def test_read(self):
    #     c = Client()
    #     r = c.get('/users/')

    # def test_update(self):
    #     pass
    
    # def test_delete(self):
    #     pass
