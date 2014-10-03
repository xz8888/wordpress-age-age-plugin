from xml.etree import ElementTree
from xml.dom import minidom

field_map = {
    'id': 'job_id', 'title': 'title', 'requisitionid': 'requisition_id',
    'category': 'category', 'jobtype': 'job_type', 'region':'region', 'location': 'location',
    'date': 'date', 'detail-url': 'detail_url', 'apply-url': 'apply_url',
    'description': 'description', 'briefdescription': 'brief_description',
}

class JobViteParser:
        
    def getByFieldAll(self, dic, field):
        """Get all data from specified field"""
        for k in dic:
            print dic[k][field]

    def getTitleByRegion(self, dic, region):
        """Get Job Titles by region"""
        string = "["
        for k in dic:
            if dic[k]['region'] == region:
                string += "{\"id\": \"%s\", \"title\": \"%s\"}," % (k, dic[k]['title'])
        string = string[:-1]
        if string:
            string += "]"
        return string
        
    def getJobDescription(self, dic, job_id):
        """Get Job Description and Apply Url"""
        description = None
        url = None
        
        for k in dic:
            if dic[k]['job_id'] == job_id:
                description = dic[k]['description']
                url = dic[k]['apply_url']
        
        string = description + '\n'
        string += '<a href="%s" target="_blank" ><div class="apply_now"></div></a>' % (url,)
        return string
                
    def parseXML(self, xml):
        """Given XML as a string, return a dictionary keyed on job id."""
        jobs = {}
        et = ElementTree.fromstring(xml)
        job_elements = et.findall('job')
        for element in job_elements:
            job_id = element.find('id').text
            jobs[job_id] = {}
            for element_name, field_name in field_map.iteritems():
                value = element.find(element_name).text
                jobs[job_id][field_name] = value
        return jobs
        
        