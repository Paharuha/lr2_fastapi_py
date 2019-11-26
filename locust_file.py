from locust import HttpLocust, TaskSet, between, task


class PublishedBookBehavior(TaskSet):
    @task(1)
    def get_publishedbooks(self):
        self.client.get('/api/publishedbooks')

    @task(1)
    def add_get_publishedbook(self):
        payload = {
            "user_id": 1,
            "book_id": 1,
        }
        self.client.post('/api/publishedbooks', json=payload)

    @task(2)
    def get_book(self):
        self.client.get('/api/books/1')

    @task(2)
    def get_userbook(self):
        self.client.get('/api/userbooks/1')

    @task(2)
    def get_publishedbook(self):
        self.client.get('/api/publishedbooks/1')

    @task(2)
    def get_books(self):
        self.client.get('/api/books')

    @task(1)
    def add_book(self):
        payload = {
            "nameBook": "Zabigal",
            "avtor": "sto tuki",
            "genre": "comedy",
            "kindOf": "Rusalka",
            "year": 1234,
            "code": "1314"
        }
        self.client.post('/api/books', json=payload)

    @task(1)
    def add_userbook(self):
        payload = {
            "first_name": "rem",
            "last_name": "unicorn",
            "surname_name": "Unic",
            "email": "rem_unicorn@gmail.com",
            "number": "12314"
        }
        self.client.post('/api/userbooks', json=payload)


class WebsiteUser(HttpLocust):
    task_set = PublishedBookBehavior
    wait_time = between(1.0, 2.0)