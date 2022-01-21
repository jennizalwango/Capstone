from locust import HttpUser, task

class HelloWorldUser(HttpUser):
  @task
  def helloworld(self):
    self.client.get(url="http://127.0.0.1:5000/")

