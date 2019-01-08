from locust import HttpLocust, TaskSet, task
from random import randint


class UserBehavior(TaskSet):

    ACCESS_KEY = '7e9efa7eb3b3b21c4488439449acfd4c'

    @staticmethod
    def generate_ip_address():
        ip = '.'.join([str(randint(0, 255)) for x in range(4)])
        return ip

    @task(4)
    def make_request(self):
        self.client.get('{}?acces_key={}'.format(self.generate_ip_address(), self.ACCESS_KEY), name="/get_info")

    @task
    def check_own_ip(self):
        self.client.get('{}?acces_key={}'.format('check', self.ACCESS_KEY), name='/get_own_info')


class WebsiteUser(HttpLocust):
    host = "http://api.ipstack.com/"
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000


if __name__ == '__main__':
    WebsiteUser().run()
