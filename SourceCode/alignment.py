import pygame


class CreateWindow:
    def __init__(self):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 645, 600
        self.SCREEN = None

    def create(self, caption):
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(caption)

    def align_to_center_horizontally(self, graphic, is_text: bool = False):
        if is_text:
            return (self.SCREEN_WIDTH - graphic.get_size()[0]) // 2
        else:
            return (self.SCREEN_WIDTH - graphic.get_width()) // 2

    def align_to_center_vertically(self, graphic, is_text: bool = False):
        if is_text:
            return (self.SCREEN_HEIGHT - graphic.get_size()[1]) // 2
        else:
            return (self.SCREEN_HEIGHT - graphic.get_height()) // 2

    def align_to_center(self, graphic, is_text: bool = False):
        if is_text:
            align_horizontally = (self.SCREEN_WIDTH - graphic.get_size()[0]) // 2
            align_vertically = (self.SCREEN_HEIGHT - graphic.get_size()[1]) // 2
        else:
            align_horizontally = (self.SCREEN_WIDTH - graphic.get_width()) // 2
            align_vertically = (self.SCREEN_HEIGHT - graphic.get_height()) // 2
        return [align_horizontally, align_vertically]
