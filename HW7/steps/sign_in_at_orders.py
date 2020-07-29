from behave import given, when, then

@given('Open Amazon Page')
def open_base_page(context):
    context.app.page.open_page()


@when('Click Amazon Orders link')
def click_orders(context):
    context.app.top_nav_menu.orders_click()


@then('Verify Sign In page is opened')
def signin_is_present(context):
    context.app.is_present.signin_is_present()