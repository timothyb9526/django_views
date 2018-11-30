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

    def test_empty_by_empty_by_empty(self):
        response = self.client.get(
            path=reverse('multiply'), data={
                'x': '',
                'y': '',
                'z': ''
            })

        self.assertTemplateUsed(response, 'app/multiply.html')


class TestEarnings(SimpleTestCase):
    """
    determines the earnings provided how many a, b, c seats are sold
    'a' seats are $15
    'b' seats are $12
    'c' seats are $9
    """

    def test_two_plus_two_plus_two(self):
        response = self.client.get(
            path=reverse('earnings'), data={
                'a': '2',
                'b': '2',
                'c': '2'
            })
        self.assertEqual(response.context['answer'], 72)

    def test_five_plus_one_plus_seven(self):
        response = self.client.get(
            path=reverse('earnings'), data={
                'a': '5',
                'b': '1',
                'c': '7'
            })
        self.assertEqual(response.context['answer'], 150)

    def test_ten_plus_two_plus_fifteen(self):
        response = self.client.get(
            path=reverse('earnings'), data={
                'a': '10',
                'b': '2',
                'c': '15'
            })
        self.assertEqual(response.context['answer'], 309)


class TestEarningsWithoutNumbers(SimpleTestCase):
    """
    If the values are not numbers, it should render app/earnings.html
    without the values in the context
    """

    def test_a_plus_two_plus_c(self):
        response = self.client.get(
            path=reverse('earnings'), data={
                'a': 'a',
                'b': '2',
                'c': 'c'
            })
        self.assertTemplateUsed(response, 'app/earnings.html')

    def test_a_plus_empty_plus_empty(self):
        response = self.client.get(
            path=reverse('earnings'), data={
                'a': 'a',
                'b': '',
                'c': ''
            })
        self.assertTemplateUsed(response, 'app/earnings.html')


class TestTrueOrFalse(SimpleTestCase):
    """
    if the two values are equal to each other, 
    it should render t_or_f.html with either true or false in the context
    """

    def test_true_and_true(self):
        response = self.client.get(
            path=reverse('t_or_f'), data={
                'num1': 'true',
                'num2': 'true'
            })
        self.assertEqual(response.context['answer'], True)

    def test_false_and_true(self):
        response = self.client.get(
            path=reverse('t_or_f'), data={
                'num1': 'false',
                'num2': 'true'
            })
        self.assertTemplateUsed(response, 'app/t_or_f.html')

    def test_false_and_false(self):
        response = self.client.get(
            path=reverse('t_or_f'), data={
                'num1': 'false',
                'num2': 'false'
            })
        self.assertEqual(response.context['answer'], False)


class TestHowPopulated(SimpleTestCase):
    """
    calculate how populated an area is depending on the land_area and the population
    """

    def test_400_divided_by_5000(self):
        response = self.client.get(
            path=reverse('population'),
            data={
                'population': '400',
                'area': '5000'
            })
        self.assertEqual(response.context['answer'], 'Sparsely Populated')

    def test_20000_divided_by_2(self):
        response = self.client.get(
            path=reverse('population'),
            data={
                'population': '20000',
                'area': '2'
            })
        self.assertEqual(response.context['answer'], 'Densely Populated')


class TestHowPopulatedWithoutNumbers(SimpleTestCase):
    """
    Without numbers, it should render population.html without the answer in the context
    """

    def test_a_divided_by_2(self):
        response = self.client.get(
            path=reverse('population'), data={
                'population': 'a',
                'area': '2'
            })
        self.assertTemplateUsed(response, 'app/population.html')

    def test_empty_divided_by_empty(self):
        response = self.client.get(
            path=reverse('population'), data={
                'population': 'a',
                'area': '2'
            })
        self.assertTemplateUsed(response, 'app/population.html')

    def test_a_divided_by_a(self):
        response = self.client.get(
            path=reverse('population'), data={
                'population': 'a',
                'area': 'a'
            })
        self.assertTemplateUsed(response, 'app/population.html')


class TestGoldStar(SimpleTestCase):
    """
    displays a certain amount of stars depending on the score
    """

    def test_900(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': '900'})
        self.assertEqual(response.context['answer'], "*")

    def test_2000(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': '2000'})
        self.assertEqual(response.context['answer'], "**")

    def test_6000(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': '6000'})
        self.assertEqual(response.context['answer'], "***")

    def test_9000(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': '9000'})
        self.assertEqual(response.context['answer'], "****")

    def test_20000(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': '20000'})
        self.assertEqual(response.context['answer'], "*****")


class TestGoldStarWithoutNumbers(SimpleTestCase):
    """
    without numbers, it should render gold_star.html without answer in the context
    """

    def test_a(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': 'a'})
        self.assertTemplateUsed(response, 'app/gold_star.html')

    def test_empty(self):
        response = self.client.get(
            path=reverse('gold_star'), data={'score': ''})
        self.assertTemplateUsed(response, 'app/gold_star.html')


class TestScoringAction(SimpleTestCase):
    """
    Gives extra points depending on the type of scoring action is played
    """

    def test_extra_kick(self):
        response = self.client.get(
            path=reverse('scoring_action'), data={'action': 'extra kick'})
        self.assertEqual(response.context['answer'], 1)

    def test_extra_conversion(self):
        response = self.client.get(
            path=reverse('scoring_action'),
            data={'action': 'extra conversion'})
        self.assertEqual(response.context['answer'], 2)

    def test_safety(self):
        response = self.client.get(
            path=reverse('scoring_action'), data={'action': 'safety'})
        self.assertEqual(response.context['answer'], 2)

    def test_fg(self):
        response = self.client.get(
            path=reverse('scoring_action'), data={'action': 'fg'})
        self.assertEqual(response.context['answer'], 3)

    def test_td(self):
        response = self.client.get(
            path=reverse('scoring_action'), data={'action': 'td'})
        self.assertEqual(response.context['answer'], 6)


class TestScoringActionWithWrongInputs(SimpleTestCase):
    def test_goal(self):
        response = self.client.get(
            path=reverse('scoring_action'), data={'action': 'goal'})
        self.assertTemplateUsed(response, 'app/scoring_action.html')

    def test_256(self):
        response = self.client.get(
            path=reverse('scoring_action'), data={'action': '256'})
        self.assertTemplateUsed(response, 'app/scoring_action.html')


class TestWalkOrDrive(SimpleTestCase):
    def test_24_and_true(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'miles': '.20',
                'weather': True
            })
        self.assertEqual(response.context['answer'], 'walk')

    def test_50_and_true(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'miles': '.50',
                'weather': True
            })
        self.assertEqual(response.context['answer'], 'drive')


class TestWalkOrDriveWithWrongInput(SimpleTestCase):
    def test_ff_and_false(self):
        response = self.client.get(
            path=reverse('walk_or_drive'),
            data={
                'miles': 'ff',
                'weather': False
            })
        self.assertTemplateUsed(response, 'app/walk_or_drive.html')
