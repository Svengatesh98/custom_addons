from odoo.http import request,route,Controller

class ProjectDashboard(Controller):
    @route('/get/project/data', auth='user', type='json')
    def fetch_project_data(self):
        project_object=request.env['project.project']
        project_ids=project_object.search([])
        data_dct={
            "projects_count":len("project_ids"),
            "project_ids":project_ids.mapped('id')
        }
        
        # Print the values for debugging purposes
        print("Projects Count:", data_dct["projects_count"])
        print("Project IDs:", data_dct["project_ids"])
        return data_dct
        
  