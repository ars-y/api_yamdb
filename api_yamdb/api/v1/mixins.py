from rest_framework import mixins, viewsets


class BaseMixinModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    Базовый класс, наследник от набора миксинов,
    представляющий обработку запросов:
    - POST (CreateModelMixin),
    - GET (ListModelMixin),
    - DELETE (DestroyModelMixin)
    и GeneriсViewSet для роутинга этих запросов.
    """
    pass
