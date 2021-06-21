import cv2

def py_game_toImg(pygame,screen):
    view = pygame.surfarray.array3d(screen)

    #  convert from (width, height, channel) to (height, width, channel)
    view = view.transpose([1, 0, 2])

    #  convert from rgb to bgr
    img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    # Display image, clear cell every 0.5 seconds
    return img_bgr

