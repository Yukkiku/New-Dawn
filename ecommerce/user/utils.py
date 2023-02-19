from ecommerce.user.serializers.user_serializer import generic_serializer
from ecommerce.utils import get_model_by_name, url_params_validation


APP_NAME_LABEL = 'user'


def get_generic_serializer(name):
    model_name = url_par