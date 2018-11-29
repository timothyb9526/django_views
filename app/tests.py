from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class TestAdd(SimpleTestCase):
    '''
    if add is given two numbers it should
    render add.html
    '''

    def test_two_plus_two(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '2',
                'num2': '2'
            })

        self.assertEqual(response.context['answer'], 4)

    def test_two_plus_negative_one(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '2',
                'num2': '-1'
            })

        self.assertEqual(response.context['answer'], 1)

    def test_zero_plus_zero(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '0',
                'num2': '0'
            })

        self.assertEqual(response.context['answer'], 0)

    def test_2_3_plus_1_2(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '2.3',
                'num2': '1.2'
            })

        self.assertEqual(response.context['answer'], 3.5)

    def test_negative_two_plus_negative_three(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '-2',
                'num2': '-3'
            })

        self.assertEqual(response.context['answer'], -5)


class TestAddWithoutNumbers(SimpleTestCase):
    """ if add is not given two numbers it should 
    present the user with the add.html template 
    and not try to compute an answer."""

    def test_given_non_numeric_input(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': 'a',
                'num2': 'a'
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_empty_input(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '',
                'num2': ''
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_empty_plus_one(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '',
                'num2': '1'
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)

    def test_empty_plus_letter(self):
        response = self.client.get(
            path=reverse('add'), data={
                'num1': '',
                'num2': 'a'
            })

        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)


class TestDoubleCanDoubleRealNumbers(SimpleTestCase):
    """
    if you GET double with a int or a float as 'num', it should
    render double.html with double that number as 'answer'.
    """

    def test_double_four(self):
        response = self.client.get(
            path=reverse('double'), data={'number': '4'})

        self.assertEqual(response.context['answer'], 8)

    def test_double_eight(self):
        response = self.client.get(
            path=reverse('double'), data={'number': '8'})

        self.assertEqual(response.context['answer'], 16)

    def test_double_zero(self):
        response = self.client.get(
            path=reverse('double'), data={'number': '0'})

        self.assertEqual(response.context['answer'], 0)

    def test_double_one(self):
        response = self.client.get(
            path=reverse('double'), data={'number': '1'})

        self.assertEqual(response.context['answer'], 2)

    def test_double_two_two(self):
        response = self.client.get(
            path=reverse('double'), data={'number': '2.2'})

        self.assertEqual(response.context['answer'], 4.4)

    def test_double_negative_four(self):
        response = self.client.get(
            path=reverse('double'), data={'number': '-4'})

        self.assertEqual(response.context['answer'], -8)


class TestDoubleWithoutNumbers(SimpleTestCase):
    """
    if you GET double with a value that is not a number, it should
    render double.html without the answer
    """

    def test_empty_value(self):
        response = self.client.get(path=reverse('double'), data={'number': ''})

        self.assertTemplateUsed(response, 'app/double.html')

    def test_letter_as_input(self):
        response = self.client.get(
            path=reverse('double'), data={'number': 'foo'})

        self.assertTemplateUsed(response, 'app/double.html')


class TestMultiplyByThree(SimpleTestCase):
    """
    if the values are numbers, it should render 
    multiply.html with the three answers in the context
    """

    def test_one_times_three_times_two(self):
        response = self.client.get(
            path=reverse('multiply'), data={
                'x': '1',
                'y': '3',
                'z': '2'
            })

        self.assertEqual(response.context['answer'], 6)

    def test_one_times_three_times_zero(self):
        response = self.client.get(
            path=reverse('multiply'), data={
                'x': '1',
                'y': '3',
                'z': '0'
            })

        self.assertEqual(response.context['answer'], 0)

    def test_two_times_six_times_two(self):
        response = self.client.get(
            path=reverse('multiply'), data={
                'x': '2',
                'y': '6',
                'z': '2'
            })

        self.assertEqual(response.context['answer'], 24)


class TestMultiplyByThreeWithoutNumbers(SimpleTestCase):
    """
    if the values are not numbers, it should render 
    multiply.html without the three answers in the context
    """

    def test_a_by_a_by_a(self):
        response = self.client.get(
            path=reverse('multiply'), data={
                'x': 'a',
                'y': 'a',
                'z': 'a'
            })

        self.assertTemplateUsed(response, 'app/multiply.html')

    def test_emoty_by_empty_by_empty(self):
        response = self.client.get(
            path=reverse('multiply'), data={
                'x': '',
                'y': '',
                'z': ''
            })

        self.assertTemplateUsed(response, 'app/multiply.html')
