from django.contrib.auth.decorators import login_required
from humans.models import Human
from products.models import Product
from bags.models import BagItem


class Bag:
    def __init__(self, request):
        self.request = request
        self.session = request.session

    def get_bag_items(self):
        if self.user.is_authenticated:
            return BagItem.objects.filter(human=self.user)
        else:
            return []

    def add(self, product, quantity=1):
        if self.user.is_authenticated:
            bag_item, created = BagItem.objects.get_or_create(
                human=self.user, product=product, defaults={"quantity": quantity}
            )
            if not created:
                bag_item.quantity += quantity
                bag_item.save()
        else:
            print("Not Authenticated User.")

    def remove(self, product):
        if self.user.is_authenticated:
            BagItem.objects.get_or_create(human=self.user, product=product).delete()
        else:
            print("Not Authenticated User.")

    def update(self, product, quantity):
        if self.user.is_authenticated:
            bag_item = BagItem.objects.filter(human=self.user, product=product).first()
            if bag_item:
                bag_item.quantity = quantity
                bag_item.save()
        else:
            print("Not Authenticated User.")

    def clear(self):
        if self.user.is_authenticated:
            BagItem.objects.filter(human=self.user).delete()
        else:
            print("Not Authenticated User.")

    def get_total_price(self):
        bag_items = self.get_bag_items()
        total_price = sum(item.product.price * item.quantity for item in bag_items)
        return total_price

    def get_items_count(self):
        bag_items = self.get_bag_items()
        return sum(item.quantity for item in bag_items)
