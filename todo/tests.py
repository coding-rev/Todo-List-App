from django.test import TestCase
from api.models import Todo
from django.urls import reverse
# Create your tests here.

class ViewTest(TestCase):

	def todo(self):
		todo 		= Todo.objects.create(body="Second Todo Test")
		return todo
	
	def test_index_view(self):
		response = self.client.get(reverse('todo:index'))
		self.assertEqual(response.status_code, 200)

	def test_createTodo_view(self):
		data 	 		= {"body": "Todo Create Test"}
		response 		= self.client.post(reverse('todo:create'), data)
		created_todo 	= Todo.objects.get(body="Todo Create Test")
		self.assertEqual(created_todo.body, "Todo Create Test")

	def test_updateTodo_view_set_todo_to_finished(self):
		getTodo 		= self.todo()
		data 		 	= {"todo_id": getTodo.id}
		response 		= self.client.post(reverse('todo:update'), data)
		updated_todo 	= Todo.objects.get(id=getTodo.id)
		self.assertTrue(updated_todo.done)

	def test_deleteTodo_view(self):
		getTodoDel 		= self.todo()
		data 			= {"todo_id": getTodoDel.id}
		response 		= self.client.post(reverse('todo:delete'), data)
		check 			= Todo.objects.filter(id=getTodoDel.id).exists()
		self.assertFalse(check)