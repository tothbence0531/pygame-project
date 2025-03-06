class Debug:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def draw(self, string):
        debug_text = self.font.render(string, True, (255, 255, 255))
        self.screen.blit(debug_text, (0, 0))