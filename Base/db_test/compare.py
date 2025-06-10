import json
from base.db import *
from base.logfile import *

log=Logger().get_logger(__name__)
connect=Omnify_connect()

class sql_quries():
    def prodv2_business_check(self): 
        
        query_business_id_data = "select distinct business_id from businesses_features where feature_id=21;"
        business_ids = connect.fetch_data(query_business_id_data)
        business_ids_pretty = [row[0] for row in business_ids]
        ids_string = ', '.join(map(str, business_ids_pretty))
            
        query_access_policies = f"SELECT widgets, waivers, team_members, tax_settings, subscriptions, setup, services, sales, role_id, publish_services, plans, payment_gateway_settings, notification_settings, migration, member_benefits, link_multiple_stores, invoices, integrations, imports, id, home, frontdesk_checkins, facility_calendar, exports, event_calendar, discounts, custom_fields, clients, class_refunds, class_calendar, categories, business_id, bulk_bookings, breaks, bookings, booking_flow_settings, billing_invoices, auto_emails, appointment_calendar, analytics, access_management FROM access_policies where business_id in ({ids_string});"
        # print(query_access_policies)
        access_policites= connect.fetch_data(query_access_policies)
        if access_policites:
            access_policites_pretty = [str(row) for row in access_policites]
            if access_policites_pretty:
                print("access_policites:", access_policites_pretty)
            else:
                print("No valid business IDs found.")



sql_quries().prodv2_business_check()