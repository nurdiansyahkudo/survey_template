# -*- coding: utf-8 -*-
# from odoo import http


# class SurveyTemplate(http.Controller):
#     @http.route('/survey_template/survey_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/survey_template/survey_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('survey_template.listing', {
#             'root': '/survey_template/survey_template',
#             'objects': http.request.env['survey_template.survey_template'].search([]),
#         })

#     @http.route('/survey_template/survey_template/objects/<model("survey_template.survey_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('survey_template.object', {
#             'object': obj
#         })

