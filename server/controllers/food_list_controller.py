from server.services.food_list_service import get_food_list, add_to_food_list


def get_list():
    return get_food_list()


def send_to_food_list(**kwargs):
    item = kwargs.get('body')
    return add_to_food_list(item)
