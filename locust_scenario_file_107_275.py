import os
from locust import HttpLocust, HttpUser, SequentialTaskSet, task, between
from locust.clients import HttpSession
import random
import json
from lxml import html
import re
import csv
import itertools

user_count = 0
variables_index = {}


resource_paths = [
        '//link[@rel="stylesheet"]/@href',
        '//link[@rel="Stylesheet"]/@href',
        '//link[@rel="STYLESHEET"]/@href',
        "//script/@src",
        "//img/@src",
        "//source/@src",
        "//embed/@src",
        "//body/@background",
        '//input[@type="image"]/@src',
        '//input[@type="IMAGE"]/@src',
        '//input[@type="Image"]/@src',
        "//object/@data",
        "//frame/@src",
        "//iframe/@src",
    ]

def get_embedded_resources(response_content, filter='.*'):
    resources = []
    tree = html.fromstring(response_content)
    for resource_path in resource_paths:
        for resource in tree.xpath(resource_path):
            if re.search(filter, resource): resources.append(resource)
    return resources

def group_url_name(url):
    directory, filename = os.path.split(url)
    url = re.sub(r'\b\d+\b', ':id', directory) + '/' + filename
    return re.sub(r'\?.*', '', url)

class ScenarioTask(SequentialTaskSet):
    def __init__(self, parent):
        super().__init__(parent)

    def on_start(self):
        # paramsデータが存在したらon_startでload
        global user_count
        self.params_data = {}
        self.random_prefix = f'{user_count}_' + ''.join([random.choice('1234567890abcdefghijklmnopqrstuvwxyz') for _ in range(10)]) + '_'
        user_count += 1

        self.variables_dict = {}
        

        self.csv_data = {}
        self.csv_row = {}
        # イテレートオブジェクトを格納
        

    def on_stop(self):
        
        None


    # scenario_order: 1
    @task
    def req_get_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /'

    
        
    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 2
    @task
    def req_get_about(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/about', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /about'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 3
    @task
    def req_get_portfolio(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 4
    @task
    def req_get_blog(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 5
    @task
    def req_get_contact(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/contact', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /contact'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 6
    @task
    def req_get_portfolio_use_less_brand_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio/use-less-brand/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio/use-less-brand/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 7
    @task
    def req_get_portfolio_kio_tape_2_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio/kio-tape-2/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio/kio-tape-2/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 8
    @task
    def req_get_portfolio_osen_clock_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio/osen-clock/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio/osen-clock/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 9
    @task
    def req_get_portfolio_seamless_watch_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio/seamless-watch/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio/seamless-watch/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 10
    @task
    def req_get_portfolio_page_2_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio/page/2/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio/page/2/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 11
    @task
    def req_get_blog_design_inspiration_the_best_projects_from_december_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog/design-inspiration-the-best-projects-from-december/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog/design-inspiration-the-best-projects-from-december/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 12
    @task
    def req_get_blog_the_10_biggest_rebrands_and_logo_designs_of_2019_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog/the-10-biggest-rebrands-and-logo-designs-of-2019/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog/the-10-biggest-rebrands-and-logo-designs-of-2019/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 13
    @task
    def req_get_blog_design_inspiration_the_best_projects_from_november_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog/design-inspiration-the-best-projects-from-november/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog/design-inspiration-the-best-projects-from-november/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 14
    @task
    def req_get_blog_pt_chooses_classic_blue_for_its_colour_of_the_year_2020_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog/pt-chooses-classic-blue-for-its-colour-of-the-year-2020/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog/pt-chooses-classic-blue-for-its-colour-of-the-year-2020/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 15
    @task
    def req_get_blog_page_2_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog/page/2/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog/page/2/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 16
    @task
    def req_get_portfolio_kio_tape_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/portfolio/kio-tape/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /portfolio/kio-tape/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    


    # scenario_order: 17
    @task
    def req_get_blog_the_10_biggest_product_stories_of_2019_(self):
        req_params = ""
        header_params = {}
        url = '%s%s' % ('/blog/the-10-biggest-product-stories-of-2019/', req_params)
        body_params = {}
        files = {}
        request_name = 'GET /blog/the-10-biggest-product-stories-of-2019/'

    

    

    
    
    
    
    
    
        response = self.client.get(url=url, headers=header_params, name=group_url_name(request_name))
    
        json_response = response.json()
        
    



    @task
    def stop(self):
        self.interrupt()

class LocustUser(HttpUser):
    tasks = [ScenarioTask]
    # TODO: betweenはparam化する、当面はこのsettingで見てみる
    wait_time = between(0.2, 0.4)