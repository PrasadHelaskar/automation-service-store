from base.db import *
from base.logfile import *

log=Logger().get_logger()
connect=Omnify_connect()

class compare_data():
    def customer_count_check(): 
        query_sub_booking_data = "select count(*) from subscription_bookings where business_id=25882 and reference_subscription_booking_id is null;"
        sub_booking_data = connect.fetch_data(query_sub_booking_data)
        print(f"sub_booking_data: {sub_booking_data}")  # Debugging output

        query_customer_sub_data = "select count(*) from customer_subscriptions where business_id=25882;"
        customer_sub_data = connect.fetch_data(query_customer_sub_data)
        print(f"customer_sub_data: {customer_sub_data}")  # Debugging output

        if sub_booking_data[0][0] == customer_sub_data[0][0]:
            print("Count matched \n No customer made duplicate booking")
        else:
            print("Count mismatched \n Customer made duplicate booking \n Check the details")