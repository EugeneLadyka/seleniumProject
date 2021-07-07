# Реализация, написать assert и сообщение об ошибке
def test_input_text (expected_result, actual_result):
    actual_result = 8
    expected_result = 11
    assert actual_result == expected_result, f"expected {expected_result},  got {actual_result}"
