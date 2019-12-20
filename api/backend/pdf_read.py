import json

import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize

# creating a pdf file object
from cv_upload.settings import MEDIA_ROOT
import textract
import re

from pyresparser import ResumeParser
import en_core_web_sm
nlp = en_core_web_sm.load()

def read_pdf(file_name):
    file_name = str(file_name).replace(" ", "_")
    data = ResumeParser(MEDIA_ROOT+'/CV/data/{}'.format(file_name)).get_extracted_data()
    print(data)
    result_dict = {}
    result_dict['name'] = data['name']

    email = re.findall(r'[\w\.-]+@[\w\.-]+', data['email'])
    result_dict['email'] = email[0]
    result_dict['skill'] = json.dumps({'skill': data['skills']})
    result_dict['mobile_number'] = data['mobile_number']
    # new_dict['Phone_no'] = data['mobile_number']
    print(result_dict)

    return result_dict

