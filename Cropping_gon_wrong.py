import os
import zlib
import struct

def validate_and_repair_png(file_path):
    repaired = False
    valid = True
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Validate the PNG signature
        signature = data[:8]
        if signature != b'\x89PNG\r\n\x1a\n':
            print(f"{file_path}: Invalid PNG signature")
            return False, repaired

        chunks = []
        offset = 8
        while offset < len(data):
            # Ensure there are enough bytes to read the chunk length
            if offset + 4 > len(data):
                print(f"{file_path}: Not enough data to read chunk length. Skipping incomplete chunk.")
                valid = False
                break

            # Read chunk length
            length = struct.unpack('>I', data[offset:offset + 4])[0]
            offset += 4

            # Ensure there are enough bytes to read the chunk type
            if offset + 4 > len(data):
                print(f"{file_path}: Not enough data to read chunk type. Skipping incomplete chunk.")
                valid = False
                break

            # Read chunk type
            chunk_type = data[offset:offset + 4]
            offset += 4

            # Ensure there are enough bytes to read the chunk data
            if offset + length > len(data):
                print(f"{file_path}: Not enough data to read chunk data. Skipping incomplete chunk.")
                valid = False
                break

            # Read chunk data
            chunk_data = data[offset:offset + length]
            offset += length

            # Ensure there are enough bytes to read the CRC
            if offset + 4 > len(data):
                print(f"{file_path}: Not enough data to read CRC. Skipping incomplete chunk.")
                valid = False
                break

            # Read and validate CRC
            crc_read = struct.unpack('>I', data[offset:offset + 4])[0]
            offset += 4

            crc_calculated = zlib.crc32(chunk_type + chunk_data) & 0xffffffff
            if crc_read != crc_calculated:
                print(f"{file_path}: CRC mismatch in chunk {chunk_type.decode('ascii')}. Repairing...")
                crc_read = crc_calculated
                repaired = True

            # Append chunk to the list
            chunks.append((length, chunk_type, chunk_data, crc_read))

        if chunks:
            # Rebuild the PNG file with only the valid chunks
            repaired_file_path = file_path.replace('.png', '_repaired.png')
            with open(repaired_file_path, 'wb') as f:
                f.write(signature)
                for length, chunk_type, chunk_data, crc in chunks:
                    f.write(struct.pack('>I', length))
                    f.write(chunk_type)
                    f.write(chunk_data)
                    f.write(struct.pack('>I', crc))

            print(f"{file_path}: Repaired and saved as {repaired_file_path}.")
        else:
            print(f"{file_path}: No valid chunks to rebuild the file.")

        return valid, repaired

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return False, repaired

# Ensure correct path structure
folder_path = r'C:/Users/User/Downloads/screenshots'

if not os.path.isdir(folder_path):
    print(f"The folder path {folder_path} does not exist.")
else:
    files_found = False
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.png'):
            files_found = True
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                print(f"Processing {file_name}...")
                valid, repaired = validate_and_repair_png(file_path)
                if valid:
                    if repaired:
                        print(f"{file_name} was repaired.")
                    else:
                        print(f"{file_name} is a valid PNG file.")
                else:
                    print(f"{file_name} is not a valid PNG file and could not be fully repaired.")

    if not files_found:
        print("No PNG files found in the folder.")
