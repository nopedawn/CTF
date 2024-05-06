def extract_png(filename, start, end):
    with open(filename, 'rb') as f:
        f.seek(start)
        png = f.read(end - start)
    return png

def save_png(png, output_filename):
    with open(output_filename, 'wb') as f:
        f.write(png)

def main():
    filename = 'floppy.img'
    output_filename = 'floppy.png'  # Output file name

    # Offsets for the PNG file
    start = 0x00004400  # PNG header offset
    end = 0x0000ba00  # IEND chunk offset

    png = extract_png(filename, start, end)
    save_png(png, output_filename)

if __name__ == '__main__':
    main()
