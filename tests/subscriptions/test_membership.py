import time
import pytest
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.waiver_vima import waiver_vima_action
# from base.discount import apply_discount
from base.custom_field import custom_fields_actions
from pages.membership_booking_elements import MembershipBooking
from tests.login import loginAction
from tests.add_on import add_on_test

log=Logger().get_logger(__name__)

class Test_Membership_bookings_actions():
    @pytest.mark.order(13)
    def test_Membership_bookings_actions(self,driver):
        mb=MembershipBooking(driver)
        sr=select_random()
        loginAction().login_action(driver)
        mb.click_subscriptions_page()
        time.sleep(2)

        service_type=mb.get_checkbox_text()
        log.info("service_type: %s",service_type)

        if service_type.lower()=="memberships":
            mb.click_checkbox()
            mb.click_apply_filter()

        else:
            raise Exception("Unable to locate the memberships in filters")
        
        time.sleep(5)

        script="""return document.getElementsByClassName('ss-card-details top-align').length;"""
        service_count=driver.execute_script(script)
        log.info("Total service count: %s",service_count)
        selected_service=sr.random_number(service_count)
        mb.click_service_selection(selected_service)

        mb.click_expand()
        time.sleep(2)
        mb.click_book()
        time.sleep(2)

        script="""return document.getElementsByClassName('bcbg checkbox-hover-effect').length;"""
        membership_duration_count=driver.execute_script(script)
        log.info("Total membership duration count: %s",membership_duration_count)
        selected_duration=sr.random_number(membership_duration_count)
        # log.info("Selected membership duration index: %s",selected_duration)
        mb.click_membership_duration(selected_duration)

        mb.click_checkout_proceed()
        time.sleep(3)
        
        script="""return document.getElementsByClassName("w-checkbox-input waitlist-checkbox").length;"""
        recived_count=driver.execute_script(script)
        attendee=select_random().random_number(recived_count)
        
        for i in range (attendee, (attendee+1)):
            mb.click_attendee_box(i)
            # log.info("Selected attendee index: %s",str(i))
        mb.click_attendee_proceed()
        time.sleep(3)
        
        if mb.visible_addon_page():
            add_on_test().add_on_page(driver)

        custom_fields_actions().custom_field_action(driver)
        
        waiver_vima_action().waiver(driver)
        time.sleep(3)

        mb.click_review_proceed()
        stripe_action().stripe_data_enty(driver)
        time.sleep(7)
        mb.click_back_to_home()
        loginAction().authenticate_cookie(driver)