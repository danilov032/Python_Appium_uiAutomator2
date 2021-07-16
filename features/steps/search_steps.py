from behave import given, when, then


@given("Нажимаем поле поиска")
def tab_search(context):
    context.app.main_page.tab_search()


@when("Вводим {search_phrase} в поле ввода")
def input_search(context, search_phrase):
    context.app.search_page.input_search()


@then("Проверяем результат {input_search}")
def verify_search_result(context, search_phrase):
    context.app.search_page.verify_search_result(search_phrase)
