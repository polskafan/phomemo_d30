import click
import serial
from wand.image import Image
from wand.font import Font
import PIL.Image
import image_helper
import os


@click.command()
@click.argument('text')
@click.option('--font', default="Helvetica", help='Path to TTF font file')
@click.option('--fruit', is_flag=True, show_default=True, default=False,
              help='Enable offsets to print on a fruit label')
def main(text, font, fruit):
    port = serial.Serial("/dev/rfcomm1", timeout=10)

    filename = generate_image(text, font, fruit, "temp.png")
    header(port)
    print_image(port, filename)
    os.remove(filename)


def header(port):
    # printer initialization sniffed from Android app "Print Master"
    packets = [
        '1f1138',
        '1f11121f1113',
        '1f1109',
        '1f1111',
        '1f1119',
        '1f1107',
        '1f110a1f110202'
    ]

    for packet in packets:
        port.write(bytes.fromhex(packet))
        port.flush()


def generate_image(text, font, fruit, filename):
    font = Font(path=font)
    if fruit:
        width, height = 240, 80
    else:
        width, height = 288, 88

    with Image(width=width, height=height, background="white") as img:
        # center text, fill canvas
        img.caption(text, font=font, gravity="center")

        # extent and rotate image
        img.background_color = "white"
        img.gravity = "center"
        if fruit:
            img.extent(width=320, height=96, x=-60)
        else:
            img.extent(width=320, height=96)
        img.rotate(270)
        img.save(filename=filename)

    return filename


def print_image(port, filename):
    width = 96

    with PIL.Image.open(filename) as src:
        image = image_helper.preprocess_image(src, width)

    # printer initialization sniffed from Android app "Print Master"
    output = '1f1124001b401d7630000c004001'

    # adapted from https://github.com/theacodes/phomemo_m02s/blob/main/phomemo_m02s/printer.py
    for chunk in image_helper.split_image(image):
        output = bytearray.fromhex(output)

        bits = image_helper.image_to_bits(chunk)
        for line in bits:
            for byte_num in range(width // 8):
                byte = 0
                for bit in range(8):
                    pixel = line[byte_num * 8 + bit]
                    byte |= (pixel & 0x01) << (7 - bit)
                output.append(byte)

        port.write(output)
        port.flush()

        output = ''


if __name__ == '__main__':
    main()
