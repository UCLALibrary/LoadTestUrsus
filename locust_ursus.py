from locust import HttpLocust, TaskSet, task
import random


class UserBehavior(TaskSet):

    @task(3)
    def index(self):
        self.client.get("/")

    @task(2)
    def collection(self):
        collections = ['/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Los+Angeles+Daily+News+Negatives','/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Bennett+%28Walter+E.%29+Photographic+Collection%2C+1937-1983+%28bulk+1952-1982%29','/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Connell+%28Will%29+Papers','/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Collection+of+California+Postcards','/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Ethiopic+Manuscripts','/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Arkatov+%28James%29+collection']
        self.client.get(random.choice(collections))

    @task(2)
    def search(self):
        search_terms = ['/catalog?utf8=✓&q=poppy&search_field=all_fields',
                       '/catalog?utf8=✓&q=bennett&search_field=all_fields',
                       '/catalog?utf8=✓&q=los+angeles&search_field=all_fields',
                       '/catalog?utf8=✓&q=still+image&search_field=all_fields',
                       '/catalog?utf8=✓&q=manuscript&search_field=all_fields',
                       '/catalog?q=piano&search_field=all_fields']
        self.client.get(random.choice(search_terms))

    @task(2)
    def facet(self):
        facet_term = ['/catalog?f%5Bsubject_sim%5D%5B%5D=Crime',
                      '/catalog?f%5Bhuman_readable_resource_type_sim%5D%5B%5D=text',
                      '/catalog?f%5Bgenre_sim%5D%5B%5D=cellulose+nitrate+film',
                      '/catalog?f%5Bnamed_subject_sim%5D%5B%5D=Wright%2C+Paul+A.',
                      '/catalog?f%5Blocation_sim%5D%5B%5D=California',
                      '/catalog?utf8=✓&search_field=dummy_range&range%5Byear_isim%5D%5Bbegin%5D=1960&range%5Byear_isim%5D%5Bend%5D=2007&commit=Limit']
        self.client.get(random.choice(facet_term))

    @task(2)
    def view(self):
        view_term = ['/catalog/fm2q1000zz-89112',
                     '/catalog/nj2bh100zz-89112',
                     '/catalog/gsqg5200zz-89112',
                     '/catalog/24wg5200zz-89112',
                     '/catalog/mt2w6200zz-89112']
        self.client.get(random.choice(view_term))

    @task(1)
    def about(self):
         self.client.get("/about")

class UserLocust(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000
