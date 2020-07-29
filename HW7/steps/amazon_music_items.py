from behave import given, when, then

@when('Click on hamburger menu')
def click_hamburger(context):
    context.app.top_nav_menu.hamburger_click()


@when('Click on Amazon Music menu item')
def click_music(context):
    context.app.hamburger_nav.amazon_music_click(context.driver)


@then('6 menu items are present')
def check_menu_items(context):
    context.app.is_present.amazon_music_6_items_is_present()