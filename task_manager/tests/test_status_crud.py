from django.test import Client, TestCase


class TestStatusCRUD(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def setUp(self) -> None:
        # c = Client()
        return super().setUp()
    
    def test_status_crud(self):
        c = Client()
        context = {
            'first_name': 'a',
            'last_name': 'a',
            'username': 'aa',
            'password1': '123',
            'password2': '123',
        }
        c.post('/users/create/', context)
        c.post('/login/', {'username': 'aa', 'password': '123'})
        
        print('assert STATUS create')
        response = c.post('/statuses/create/', {'name': 'uiopjklasdf 9078;; jjj'})
        self.assertTrue(response.status_code == 302)

        print('assert status read')
        response = c.get('/statuses/')
        self.assertContains(response, 'uiopjklasdf 9078;; jjj')

        print('assert status update')
        response = c.post(f'/statuses/1/update/', {'name': 'uiopjklasdf 9078;; jj754'})
        response = c.get('/statuses/')
        self.assertContains(response, 'uiopjklasdf 9078;; jj754')

        print('assert status delete')
        response = c.post(f'/statuses/1/delete/')
        response = c.get('/statuses/')
        self.assertNotContains(response, 'uiopjklasdf 9078;; jj')
    