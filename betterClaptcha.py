import claptcha,random
from PIL import Image, ImageDraw,ImageFont

class Claptcha(claptcha.Claptcha):
    def __init__(self, source, font,
                 size=(200, 80), margin=(20, 20),
                 **kwargs):
        super().__init__(source, font, size, margin, **kwargs)
        self.lines=kwargs.get("lines",1)
        self.baseColor=kwargs.get("color",(255,255,255))
    def _drawLine(self, image):
        """Draw morphed line in Image object."""
        w, h = image.size
        w *= 5
        h *= 5
        for _ in range(self.lines):
            l_image = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            l_draw = ImageDraw.Draw(l_image)

            x1 = int(w * random.uniform(0, 0.1))
            y1 = int(h * random.uniform(0, 1))
            x2 = int(w * random.uniform(0.9, 1))
            y2 = int(h * random.uniform(0, 1))

            # Line width modifier was chosen as an educated guess
            # based on default image area.
            l_width = round(((w * h)**0.5 * 2.284e-2)*0.8)

            # Draw
            l_draw.line(((x1, y1), (x2, y2)), fill=(0, 0, 0, 255), width=l_width)

            # Transform
            l_image = self._rndLineTransform(l_image)
            l_image = l_image.resize(image.size, resample=self.resample)

            # Paste onto image
            image.paste(l_image, (0, 0), l_image)
    def blendWhite(self,color,times):
        return tuple(map(lambda x: sum(([x]*times)+([255]*(100-times)))//100,color))
    def _whiteNoise(self, size):
        """Generate white noise and merge it with given Image object."""
        color=self.baseColor
        if self.noise > 0.003921569:  # 1./255.
            # noise = noise*255
            w, h = size
            pixel = (lambda noise: round(100 * random.uniform(1-noise, 1)))
            n_image = Image.new('RGB', size, (0, 0, 0))
            tmp = list(map(lambda _: pixel(self.noise),
                            [0] * w * h))
            rnd_grid=[]
            for i in tmp:
                rnd_grid.append(self.blendWhite(color,i))
            n_image.putdata(list(rnd_grid))
            return (n_image)
        else:
            return None
    def invertColor(self,color):
        return tuple(map(lambda x: 255-x,color))
    def _writeText(self,image, text, pos):
        color=self.invertColor(self.baseColor)
        """Write morphed text in Image object."""
        offset = 0
        x, y = pos

        for c in text:
            # Write letter
            c_size = self.font.getsize(c)
            c_image = Image.new('RGBa', c_size, (0, 0, 0, 0))
            c_draw = ImageDraw.Draw(c_image)
            c_draw.text((0, 0), c, font=self.font, fill=(0, 0, 0))

            # Transform
            c_image = self._rndLetterTransform(c_image)
            data=list(c_image.getdata())
            pixels=[]
            for i in data:
                pixels.append(self.blendWhite(color,i[3]))
            c_image = Image.new('RGBA', c_size, (0, 0, 0, 0))
            c_image.putdata(pixels)
            image.paste(c_image, (x+offset, y), c_image)
            offset += c_size[0]