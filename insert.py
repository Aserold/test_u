import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant.settings")

django.setup()

import json  # noqa: E402
from menu.models import FoodCategory, Food  # noqa: E402


with open('data.json', 'r', encoding='UTF-8') as f:
    data = json.loads(f.read())

for category_data in data:
    category = FoodCategory.objects.create(
        id=category_data["id"],
        name_ru=category_data["name_ru"],
        name_en=category_data["name_en"],
        name_ch=category_data["name_ch"],
        order_id=category_data["order_id"],
    )

    for food_data in category_data["foods"]:
        additional = food_data.get("additional")
        if additional == []:
            additional = None

        food = Food.objects.create(
            category=category,
            internal_code=food_data["internal_code"],
            code=food_data["code"],
            name_ru=food_data["name_ru"],
            description_ru=food_data["description_ru"],
            description_en=food_data["description_en"],
            description_ch=food_data["description_ch"],
            is_vegan=food_data["is_vegan"],
            is_special=food_data["is_special"],
            cost=food_data["cost"],
            is_publish=food_data.get("is_publish", False),
        )

        if additional:
            additional_foods = Food.objects.filter(
                internal_code__in=additional
                )
            food.additional.set(additional_foods)

print("Данные загружены.")
