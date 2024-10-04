'''from bs4 import BeautifulSoup
import requests
import time
import json

def get_user_skills():
    print('Enter a list of familiar skills separated by commas:')
    skills_input = input('> ')
    return [skill.strip() for skill in skills_input.split(',')]

def find_jobs(familiar_skills):
    job_list = []

    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if any(skill.lower() in skills.lower() for skill in familiar_skills):
                job_details = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'More Info': more_info
                }
                job_list.append(job_details)
                print(f'Job details added: {index}')

    return job_list

if __name__ == '__main__':
    familiar_skills = get_user_skills()

    while True:
        job_results = find_jobs(familiar_skills)

        # Convert the list of job details to JSON
        json_response = json.dumps(job_results, indent=2)

        # Print or return the JSON response as needed
        print(json_response)

        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)'''

from bs4 import BeautifulSoup
import requests
import json
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/jobs/")
async def get_jobs(familiar_skills: str = Query(...)):
    job_list = []

    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if any(skill.lower() in skills.lower() for skill in familiar_skills.split(',')):
                job_details = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'More Info': more_info
                }
                job_list.append(job_details)
                print(f'Job details added: {index}')

    return job_list

