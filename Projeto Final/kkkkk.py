from PIL import Image, ImageTk, ImageSequence

class AnimatedIconApp:
    def __init__(self, gif_path):
        self.gif = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(self.gif)]
        self.index = 0

    def get_next_frame(self):
        """Return the next frame in the animation."""
        frame = self.frames[self.index]
        self.index = (self.index + 1) % len(self.frames)  # Loop through frames
        return frame
