from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import QueryDict
import datetime

# Create your tests here.

from .models import Question, Choice

class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        
        self.assertEqual(future_question.was_published_recently(), False)
        
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
        
class ChoiceMethodTests(TestCase):
    
    def test_str(self):
        """
        __str__ should return the choice_text
        """
        text = "This is a choice"
        choice = Choice(choice_text=text, votes=0)
        self.assertEqual("{}".format(choice), text)
        
def create_question(question_text, days):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    
def add_choice(choice_text, question):
    """
    Adds an choice to a question
    """
    return question.choice_set.create(choice_text=choice_text, votes=0)
    
class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
        
class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        choice_1 = add_choice(choice_text='Choice 1', question=past_question)
        choice_2 = add_choice(choice_text='Choice 2', question=past_question)
        
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        
        self.assertContains(response, past_question.question_text)
        self.assertContains(response, choice_1.choice_text)
        self.assertContains(response, choice_2.choice_text)
        
class QuestionVoteTests(TestCase):
    def test_vote_where_question_doesnt_exist(self):
        """
        Try to vote on a question that doesn't exist
        """
        url = reverse('polls:vote', args=("1",))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
        
    def test_vote_where_question_is_in_the_future(self):
        """
        Try to vote on a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:vote', args=(future_question.id,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
        
    def test_vote_with_a_past_question_choice_not_selected(self):
        """
        The voting on a question with a pub_date in the past, but not defining
        a choice should display the question's text, but will also complain 
        that a Choice was not selected
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        choice_1 = add_choice(choice_text='Choice 1', question=past_question)
        choice_2 = add_choice(choice_text='Choice 2', question=past_question)
        
        url = reverse('polls:vote', args=(past_question.id,))
        response = self.client.post(url)
        
        self.assertContains(response, past_question.question_text)
        self.assertContains(response, choice_1.choice_text)
        self.assertContains(response, choice_2.choice_text)
        self.assertContains(response, "You didn&#39;t select a choice.")
        
    def test_vote_with_a_past_question_choice_isnt_valid(self):
        """
        The voting on a question with a pub_date in the past, but defining a 
        choice that doesn't exist should display the question's text, but will 
        also complain that a Choice was not selected
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        choice_1 = add_choice(choice_text='Choice 1', question=past_question)
        choice_2 = add_choice(choice_text='Choice 2', question=past_question)
        
        url = reverse('polls:vote', args=(past_question.id,))
        response = self.client.post(url, {'choice' : 3})
        
        self.assertContains(response, past_question.question_text)
        self.assertContains(response, choice_1.choice_text)
        self.assertContains(response, choice_2.choice_text)
        self.assertContains(response, "You didn&#39;t select a choice.")
        
    def test_vote_with_a_past_question(self):
        """
        The voting on a question with a pub_date in the past, but defining a 
        choice that doesn't exist should display the question's text, but will 
        also complain that a Choice was not selected
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        choice_1 = add_choice(choice_text='Choice 1', question=past_question)
        choice_2 = add_choice(choice_text='Choice 2', question=past_question)
        
        url = reverse('polls:vote', args=(past_question.id,))
        response = self.client.post(url, {'choice' : 1}, follow=True)
        
        print response
        
        self.assertContains(response, past_question.question_text)
        self.assertContains(response, choice_1.choice_text + " -- 1 vote")
        self.assertContains(response, choice_2.choice_text + " -- 0 votes")