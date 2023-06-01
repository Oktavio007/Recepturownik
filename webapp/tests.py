

from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from webapp.models import Category, Unit


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_load(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)


class CategoriesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', is_staff=True)
        self.user.set_password('12345')
        self.user.save()

    def test_categories_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

    def test_categories_not_logged_in(self):
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 302)

    def test_get_add_category_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/addcategory')
        self.assertEqual(response.status_code, 200)

    def test_get_add_category_not_logged_in(self):
        response = self.client.get('/addcategory')
        self.assertEqual(response.status_code, 302)

    def test_post_add_category_logged_in(self):
        self.client.login(username='testuser', password='12345')

        form_data = {
            'name': 'CategoryTest'
        }
        response = self.client.post('/addcategory', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/categories')
        self.assertTrue(Category.objects.filter(name='CategoryTest').exists())

    def test_post_add_category_not_logged_in(self):
        form_data = {
            'name': 'CategoryTest'
        }
        response = self.client.post('/addcategory', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login?next=/addcategory')
        self.assertFalse(Category.objects.filter(name='CategoryTest').exists())


    def test_category_delete_logged_in(self):
        self.client.login(username='testuser', password='12345')

        category = Category.objects.create(
            name='CategoryTest'
        )
        response = self.client.get('/categories/delete/' + str(category.id))
        self.assertRedirects(response, '/categories')
        self.assertFalse(Category.objects.filter(name='CategoryTest').exists())

    def test_category_delete_not_logged_in(self):
        category = Category.objects.create(
            name='CategoryTest'
        )
        response = self.client.get('/categories/delete/' + str(category.id))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='CategoryTest').exists())

    def test_get_category_edit_logged_in(self):
        self.client.login(username='testuser', password='12345')

        category = Category.objects.create(
            name='CategoryTest'
        )

        response = self.client.get('/editcategory/' + str(category.id))
        self.assertEqual(response.status_code, 200)

    def test_get_category_edit_not_logged_in(self):
        category = Category.objects.create(
            name='CategoryTest'
        )

        response = self.client.get('/editcategory/' + str(category.id))
        self.assertEqual(response.status_code, 302)

    def test_post_category_edit_logged_in(self):
        self.client.login(username='testuser', password='12345')

        category = Category.objects.create(
            name='CategoryTest'
        )

        form_data = {
            'id': category.id,
            'name': 'CategoryTest1'
        }

        response = self.client.post('/editcategory/' + str(category.id), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/categories')
        self.assertFalse(Category.objects.filter(name='CategoryTest').exists())
        self.assertTrue(Category.objects.filter(name='CategoryTest1').exists())

    def test_post_category_edit_not_logged_in(self):
        category = Category.objects.create(
            name='CategoryTest'
        )

        form_data = {
            'id': category.id,
            'name': 'CategoryTest1'
        }

        response = self.client.post('/editcategory/' + str(category.id), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='CategoryTest').exists())


class UnitsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', is_staff=True)
        self.user.set_password('12345')
        self.user.save()

    def test_units_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/units')
        self.assertEqual(response.status_code, 200)

    def test_units_not_logged_in(self):
        response = self.client.get('/units')
        self.assertEqual(response.status_code, 302)

    def test_get_add_unit_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/addunit')
        self.assertEqual(response.status_code, 200)

    def test_get_add_unit_not_logged_in(self):
        response = self.client.get('/addunit')
        self.assertEqual(response.status_code, 302)

    def test_post_add_unit_logged_in(self):
        self.client.login(username='testuser', password='12345')

        form_data = {
            'name': 'UnitTest'
        }
        response = self.client.post('/addunit', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/units')
        self.assertTrue(Unit.objects.filter(name='UnitTest').exists())

    def test_post_add_unit_not_logged_in(self):
        form_data = {
            'name': 'UnitTest'
        }
        response = self.client.post('/addunit', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login?next=/addunit')
        self.assertFalse(Unit.objects.filter(name='UnitTest').exists())

    def test_unit_delete_logged_in(self):
        self.client.login(username='testuser', password='12345')

        unit = Unit.objects.create(
            name='UnitTest'
        )
        response = self.client.get('/units/delete/' + str(unit.id))
        self.assertRedirects(response, '/units')
        self.assertFalse(Unit.objects.filter(name='UnitTest').exists())

    def test_unit_delete_not_logged_in(self):
        unit = Unit.objects.create(
            name='UnitTest'
        )
        response = self.client.get('/units/delete/' + str(unit.id))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Unit.objects.filter(name='UnitTest').exists())

    #====================== EDIT ======================

    def test_get_unit_edit_logged_in(self):
        self.client.login(username='testuser', password='12345')

        unit = Unit.objects.create(
            name='UnitTest'
        )

        response = self.client.get('/editunit/' + str(unit.id))
        self.assertEqual(response.status_code, 200)

    def test_get_unit_edit_not_logged_in(self):
        unit = Unit.objects.create(
            name='UnitTest'
        )

        response = self.client.get('/editunit/' + str(unit.id))
        self.assertEqual(response.status_code, 302)

    def test_post_unit_edit_logged_in(self):
        self.client.login(username='testuser', password='12345')

        unit = Unit.objects.create(
            name='UnitTest'
        )

        form_data = {
            'id': unit.id,
            'name': 'UnitTest1'
        }

        response = self.client.post('/editunit/' + str(unit.id), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/units')
        self.assertFalse(Unit.objects.filter(name='UnitTest').exists())
        self.assertTrue(Unit.objects.filter(name='UnitTest1').exists())

    def test_post_unit_edit_not_logged_in(self):
        unit = Unit.objects.create(
            name='UnitTest'
        )

        form_data = {
            'id': unit.id,
            'name': 'UnitTest1'
        }

        response = self.client.post('/editunit/' + str(unit.id), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Unit.objects.filter(name='UnitTest').exists())
