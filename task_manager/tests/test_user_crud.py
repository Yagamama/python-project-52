from django.test import Client, TestCase


class TestUserCRUD(TestCase):

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
        print('assert USER create')
        response = c.post('/users/create/', context)
        self.assertTrue(response.status_code == 302)

        print('assert user read')
        response = c.get('/users/')
        self.assertContains(response, 'aaaa bbbb')
        self.assertContains(response, 'aaaabbbbcccc')

        response = c.post('/login/', {'username': 'aaaabbbbcccc', 'password': '123'})
        id = c.session.get('user_id')
        # print('id =', id)

        print('assert user update')
        context['last_name'] = 'bnbnbry'
        response = c.post(f'/users/{id}/update/', context)
        response = c.get('/users/')
        self.assertContains(response, 'aaaa bnbnbry')

        print('assert user delete')
        response = c.post(f'/users/{id}/delete/')
        response = c.get('/users/')
        self.assertNotContains(response, 'aaaa bnbnbry')
    