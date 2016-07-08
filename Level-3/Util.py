#-------------------------
# test if whether two objects has collided based on their .img surface
#-------------------------
def hasCollideRect(a, b):
    a_rect = a.img.get_rect()
    a_rect = a_rect.move(a.x, a.y)
    b_rect = b.img.get_rect()
    b_rect = b_rect.move(b.x, b.y)
    return a_rect.colliderect(b_rect)
