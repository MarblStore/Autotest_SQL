import sender_stand_request

import data

# Автотест
def test_create_and_fetch_order():
    # Создание заказа
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201, f"Ошибка при создании заказа: {create_response.status_code}"

    tracker_id = create_response.json().get("track")
    assert tracker_id is not None, "В ответе отсутствует номер трекера"

    # Информация о заказе по трекеру
    fetch_response = sender_stand_request.fetch_order_by_tracker(tracker_id)
    assert fetch_response.status_code == 200, f"Ошибка при получении данных заказа: {fetch_response.status_code}"

