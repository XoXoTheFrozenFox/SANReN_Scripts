import zlib
import gzip
import bz2
import os

def decompress_zlib_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            compressed_data = file.read()

        # Try zlib decompression first
        try:
            decompressed_data = zlib.decompress(compressed_data)
        except zlib.error:
            # If zlib decompression fails, try gzip
            try:
                decompressed_data = gzip.decompress(compressed_data)
            except OSError:
                # If gzip fails, try bz2
                decompressed_data = bz2.decompress(compressed_data)

        with open(output_file, 'wb') as file:
            file.write(decompressed_data)

        print(f"Decompressed {input_file} to {output_file}")
    except Exception as e:
        print(f"Error decompressing {input_file}: {e}")

if __name__ == "__main__":
    downloads_folder = os.path.expanduser('~/Downloads')
    
    files = [
        (os.path.join(downloads_folder, '29.zlib'), os.path.join(downloads_folder, '29_decompressed.txt')),
        (os.path.join(downloads_folder, '29 (1).zlib'), os.path.join(downloads_folder, '29(1)_decompressed.txt'))
    ]

    for input_file, output_file in files:
        decompress_zlib_file(input_file, output_file)
