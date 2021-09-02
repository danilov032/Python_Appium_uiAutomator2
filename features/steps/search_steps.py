from behave import step


@step("Нажимаем поле поиска")
def tab_search(context):
    context.app.main_page.tab_search()


@step("Вводим {search_phrase} в поле ввода")
def input_search(context, search_phrase):
    context.app.search_page.input_search(search_phrase)


@step("Проверяем результат {search_phrase}")
def verify_search_result(context, search_phrase):
    context.app.search_page.verify_search_result(search_phrase)
