from django.test import Client, TestCase


class TestCRUD(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def setUp(self) -> None:
        return super().setUp()
    
    def test_crud(self):
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
        self.assertContains(response, 'aaaabbbbcccc')

        response = c.post('/login/', {'username': 'aaaabbbbcccc', 'password': '123'})
        id = c.session.get('user_id')
        print('id =', id)

        context['last_name'] = 'bnbnbry'
        response = c.post(f'/users/{id}/update/', context)
        print('assert update')
        response = c.get('/users/')
        self.assertContains(response, 'aaaa bnbnbry')

        response = c.post(f'/users/{id}/delete/')
        print('assert delete')
        response = c.get('/users/')
        self.assertNotContains(response, 'aaaa bnbnbry')
    
    # def test_read(self):
    #     c = Client()
    #     r = c.get('/users/')

    # def test_update(self):
    #     pass
    
    # def test_delete(self):
    #     pass
