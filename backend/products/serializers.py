from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import unique_prod_title
from api.serializers import UserPublicSerilizer

from api.serializers import UserProductInlineSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
            read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerilizer(source='user', read_only=True)
    # related_products = UserProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[unique_prod_title])
    email = serializers.EmailField(write_only=True)
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            # 'related_products',
            # 'my_user_data',
            'url',
            # 'user',
            'email',
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'my_discount',
            'public',
            'path',
            'endpoint'
        ]

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)

    # def create(self, validated_data):
    #     obj = super().create(validated_data)
    #     return obj

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def ger_user_data(self, obj):
        return {
            "username": obj.user.username
        }


