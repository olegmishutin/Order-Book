from django.db.models import Sum
from rest_framework import serializers
from .models import Order, OrderProduct, Category, OrderRequest
from product.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['orders']


class UserOrderSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField(source='get_status_display')
    categories = CategorySerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        exclude = ['user']
        depth = 1

    def to_internal_value(self, data):
        returnedData = super(UserOrderSerializer, self).to_internal_value(data)
        products = data.get('products')

        if products:
            returnedData.update({'products': products})

            return returnedData
        raise serializers.ValidationError({'products': ['Не выбрано ни одного продукта']})

    # Метод добавляющий продукты в заказ и сохранающий заказ (понадобится далее)
    def addProductsInOrder(self, order, products, oldProducts=None):
        request = self.context['request']

        OrderProduct.objects.bulk_create([OrderProduct(order=order, product_id=product) for product in products])
        order.price = order.products.all().aggregate(priceSum=Sum('price'))['priceSum']

        if order.price >= 500 and order.price <= 100000:
            order.save(update_fields=['price'])
            return order

        if request.method == 'POST':
            order.delete()

        elif request.method == 'PATCH' or request.method == 'PUT':
            order.products.clear()
            OrderProduct.objects.bulk_create([OrderProduct(order=order, product_id=product) for product in oldProducts])

        raise serializers.ValidationError(
            {'message': 'Стоимость заказа должна начинаться с 500р и быть не больше 100000р'})

    # Перепись метода обновления для того, чтобы можно было изменить список продуктов
    def update(self, instance, validated_data):
        products = validated_data.pop('products', [])
        oldProductsIds = list(instance.products.all().values_list('id', flat=True))

        instance.products.clear()
        self.addProductsInOrder(instance, products, oldProductsIds)  # Вызов ранее описанного метода

        return super(UserOrderSerializer, self).update(instance, validated_data)

    # Перепись метода создания для добавления продуктов в заказ
    def create(self, validated_data):
        user = self.context['request'].user

        products = validated_data.pop('products', [])
        order = Order.objects.create(user=user, **validated_data)

        OrderRequest.objects.create(order=order)
        return self.addProductsInOrder(order, products)  # Вызов ранее описанного метода, который вернет данные заказа


class WorkOrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    comment = serializers.ReadOnlyField()
    place = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'
        depth = 1

    def to_internal_value(self, data):
        returnedData = super(WorkOrderSerializer, self).to_internal_value(data)
        returnedData.update({'categories': data.get('categories')})
        return returnedData

    def update(self, instance, validated_data):
        categories = validated_data.pop('categories', [])

        if not self.initial_data.get('status'):
            instance.categories.clear()

            if categories:
                instance.categories.add(*categories)

        return super(WorkOrderSerializer, self).update(instance, validated_data)


class UserOrderRequestSerializer(serializers.ModelSerializer):
    order = UserOrderSerializer(read_only=True)
    status = serializers.ReadOnlyField(source='get_status_display')

    class Meta:
        model = OrderRequest
        fields = '__all__'


class WorkerOrderRequestSerializer(serializers.ModelSerializer):
    order = WorkOrderSerializer(read_only=True)

    class Meta:
        model = OrderRequest
        fields = '__all__'
