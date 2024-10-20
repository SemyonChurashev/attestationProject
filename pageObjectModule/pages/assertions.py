

class Assertions:
    @staticmethod
    def test_input_field_value(field_value: str, expected_results: str):
        assert field_value == expected_results, (f'Неверное состояние поля ввода, ожидалось {expected_results},'
                                                 f'получено {field_value}')

    @staticmethod
    def test_is_element_present(what, description):
        assert what, f'Не найден нужный элемент на странице {description}'
