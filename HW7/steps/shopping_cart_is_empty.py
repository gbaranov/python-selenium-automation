from behave import given, when, then

@when('Click on cart icon')
def cart_click(context):
    context.app.top_nav_menu.cart_click()


@then("Verify {expected_text} text present")
def verify_cart_is_empty(context, expected_text):
    context.app.is_present.cart_is_empty_is_present(expected_text)
