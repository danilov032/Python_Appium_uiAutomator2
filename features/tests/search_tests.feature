Feature: Тесты для поиска

  Scenario: Пользователь вводит корректный результат в поиск
    Given Нажимаем поле поиска
    When Вводим слово в поле ввода
    Then Проверяем результат