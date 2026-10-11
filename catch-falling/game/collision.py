def is_caught(basket_rect, obj):
    """Caught only when the object is horizontally over the basket AND has
    actually reached basket height."""
    in_x = basket_rect.left <= obj.x <= basket_rect.right
    reached_basket = obj.y + obj.radius >= basket_rect.top
    not_past_basket = obj.y <= basket_rect.bottom
    return in_x and reached_basket and not_past_basket
