# -*- coding: utf-8 -*-

import base64
from odoo import http, _
from odoo.http import request
#from odoo import models,registry, SUPERUSER_ID odoo13
from odoo.addons.portal.controllers.portal import CustomerPortal as website_account

class MachineRepairSupport(http.Controller):

    def prepare_vals_machine_repair(self, Partner, **post):
        team_obj = request.env['machine.support.team']
        team_match = team_obj.sudo().search([('is_team','=', True)], limit=1)
        support_vals = {
            'subject': post['subject'],
            'team_id' :team_match.id,
#            'partner_id' :team_match.leader_id.id, odoo13
            'team_leader_id' :team_match.leader_id.id,
            'user_id' :team_match.leader_id.id,
            'email': post['email'],
            'phone': post['phone'],
            'description': post['description'],
            'priority': post['priority'],
            'partner_id': Partner.id,
            'website_brand': post['brand'],
            'website_model': post['model'],
            'damage': post['damage'],
            'website_year': post['year'],
            'nature_of_service_id': int(post['service_id']),
            'custome_client_user_id': request.env.user.id,
        }
        return support_vals
                                                             
    def prepare_open_machine_repair_vals(self, **post):
        service_ids = request.env['service.nature'].sudo().search([])
        srvice_type_ids = request.env['repair.type'].sudo().search([])
        vals = {
            'service_ids': service_ids,
            'srvice_type_ids': srvice_type_ids,
        }
        return vals

    @http.route(['/page/machine_repair_support_ticket'], type='http', auth="public", website=True)
    def open_machine_repair_request(self, **post):
        vals = self.prepare_open_machine_repair_vals(**post)
        return request.render("machine_repair_management.website_machine_repair_support_ticket", vals)

    @http.route(['/machine_repair_management/request_submitted'], type='http', auth="public", methods=['POST'], website=True)
    def request_submitted(self, **post):
#         cr, uid, context, pool = http.request.cr, http.request.uid, http.request.context, request.env
#        Partner = request.env['res.partner'].sudo().search([('email', '=', post['email'])]) odoo13
        if request.env.user.has_group('base.group_public'):
            Partner = request.env['res.partner'].sudo().search([('email', '=', post['email'])], limit=1)
        else:
            Partner = request.env.user.partner_id
        if Partner:
            support_vals = self.prepare_vals_machine_repair(Partner, **post)
            support = request.env['machine.repair.support'].sudo().create(support_vals)
            values = {
                'support':support,
                'user':request.env.user
            }
            attachment_list = request.httprequest.files.getlist('attachment')
            for image in attachment_list:
                if post.get('attachment'):
                    attachments = {
                               'res_name': image.filename,
                               'res_model': 'machine.repair.support',
                               'res_id': support,
                               'datas': base64.encodebytes(image.read()),
                               'type': 'binary',
                               # 'datas_fname': image.filename, odoo13
                               'name': image.filename,
                           }
                    attachment_obj = http.request.env['ir.attachment']
                    attach = attachment_obj.sudo().create(attachments)
            if len(attachment_list) > 0:
                group_msg = _('Customer has sent %s attachments to this machine repair ticket. Name of attachments are: ') % (len(attachment_list))
                for attach in attachment_list:
                    group_msg = group_msg + '\n' + attach.filename
                group_msg = group_msg + '\n'  +  '. You can see top attachment menu to download attachments.'
                support.sudo().message_post(body=group_msg,message_type='comment')
            return request.render('machine_repair_management.thanks_mail_send', values)
        else:
            return request.render('machine_repair_management.support_invalid',{'user':request.env.user})
       
# not necessary  odoo13
#    @http.route(['/machine_repair_management/invite'], auth='public', website=True, methods=['POST'])
#    def index_user_invite(self, **kw):
#        email = kw.get('email')
#        name = kw.get('name')
##         cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
#        user = request.env['res.users'].browse(request.uid)
#        user_exist = request.env['res.users'].sudo().search([('login','=',str(email))])
#        vals = {
#                  'user_id':user_exist,
#                }
#        if user_exist:
#            return http.request.render('machine_repair_management.user_alredy_exist', vals)
#        value={
#              'name': name,
#              'email': email,
#              'invitation_date':datetime.date.today(),
#              'referrer_user_id':user.id,
#              }
#        user_info_id = self.create_history(value)
#        base_url = http.request.env['ir.config_parameter'].get_param('web.base.url', default='http://localhost:8069') + '/page/machine_repair_management.user_thanks'
#        url = "%s?user_info=%s" %(base_url, user_info_id.id)
#        reject_url = http.request.env['ir.config_parameter'].get_param('web.base.url', default='http://localhost:8069') + '/page/machine_repair_management.user_thanks_reject'
#        rejected_url = "%s?user_info=%s" %(reject_url, user_info_id.id)
#        local_context = http.request.env.context.copy()
#        issue_template = http.request.env.ref('machine_repair_management.email_template_machine_ticket')
#        local_context.update({'user_email': email, 'url': url, 'name':name,'rejected_url':rejected_url})
#        issue_template.sudo().with_context(local_context).send_mail(request.uid)
       
    @http.route(['/machine_repair_email/feedback/<int:order_id>'], type='http', auth='public', website=True)
    def feedback_email(self, order_id, **kw):
        values = {}
        values.update({'machine_ticket_id': order_id})
        return request.render("machine_repair_management.machine_repair_feedback", values) 
       
    @http.route(['/machine_repari/feedback/'],
                methods=['POST'], auth='public', website=True)
    def start_rating(self, **kw):
        partner_id = kw['partner_id']
        user_id = kw['machine_ticket_id']
        ticket_obj = request.env['machine.repair.support'].sudo().browse(int(user_id))
        #if partner_id == UserInput.partner_id.id:
        vals = {
              'rating':kw['star'],
              'comment':kw['comment'],
            }
        ticket_obj.sudo().write(vals)
        customer_msg = _(ticket_obj.partner_id.name + 'has send this feedback rating is %s and comment is %s') % (kw['star'],kw['comment'],)
        ticket_obj.sudo().message_post(body=customer_msg)
        return http.request.render("machine_repair_management.successful_feedback")
            
class website_account(website_account):

    def _prepare_portal_layout_values(self): # odoo11
        values = super(website_account, self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'repair_request_count': request.env['machine.repair.support'].search_count([('partner_id', 'child_of', [partner.commercial_partner_id.id])]),
            'page_name': 'repair_requests',
        })
        return values
#     @http.route()
#     def account(self, **kw):
#         """ Add ticket documents to main account page """
#         response = super(website_account, self).account(**kw)
#         partner = request.env.user.partner_id
#         ticket = request.env['machine.repair.support']
#         ticket_count = ticket.sudo().search_count([
#         ('partner_id', 'child_of', [partner.commercial_partner_id.id])
#           ])
#         response.qcontext.update({
#         'ticket_count': ticket_count,
#         })
#         return response
        
    @http.route(['/my/repair_requests', '/my/repair_requests/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_repair_request(self, page=1, **kw):
        response = super(website_account, self)
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        support_obj = http.request.env['machine.repair.support']
        domain = [
            ('partner_id', 'child_of', [partner.commercial_partner_id.id])
        ]
        # pager
        pager = request.website.pager(
            url="/my/repair_requests",
            total=values.get('repair_request_count'),
            page=page,
            step=self._items_per_page
        )
        # content according to pager and archive selected
        repair_request = support_obj.sudo().search(domain, limit=self._items_per_page, offset=pager['offset'])
        values.update({
            'repair_requests': repair_request,
            'page_name': 'repair_requests',
            'pager': pager,
            'default_url': '/my/repair_requests',
        })
        return request.render("machine_repair_management.display_repair_requests", values)
       
    @http.route(['/my/repair_request/<model("machine.repair.support"):repair_request>'], type='http', auth="user", website=True)
    def my_repair_request(self, repair_request=None,  access_token=None,**kw):
        attachment_list = request.httprequest.files.getlist('attachment')
        support_obj = http.request.env['machine.repair.support'].sudo().browse(repair_request.id)
        for image in attachment_list:
            if kw.get('attachment'):
                attachments = {
                           'res_name': image.filename,
                           'res_model': 'machine.repair.support',
                           'res_id': repair_request.id,
                           'datas': base64.encodebytes(image.read()),
                           'type': 'binary',
                           # 'datas_fname': image.filename, odoo13
                           'name': image.filename,
                       }
                attachment_obj = http.request.env['ir.attachment']
                attachment_obj.sudo().create(attachments)
        if len(attachment_list) > 0:
            group_msg = _('Customer has sent %s attachments to this Machine repair ticket. Name of attachments are: ') % (len(attachment_list))
            for attach in attachment_list:
                group_msg = group_msg + '\n' + attach.filename
            group_msg = group_msg + '\n'  +  '. You can see top attachment menu to download attachments.'
            support_obj.sudo().message_post(body=group_msg,message_type='comment')
            customer_msg = _('%s') % (kw.get('ticket_comment'))
            support_obj.sudo().message_post(body=customer_msg,message_type='comment')
            return http.request.render('machine_repair_management.successful_ticket_send',{
            })
        if kw.get('ticket_comment'):
            customer_msg = _('%s') % (kw.get('ticket_comment'))
            support_obj.sudo().message_post(body=customer_msg,message_type='comment')
            return http.request.render('machine_repair_management.successful_ticket_send',{
            })
        return request.render("machine_repair_management.display_repair_request_from", {'repair_request': repair_request, 'token':access_token,'user': request.env.user})
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


