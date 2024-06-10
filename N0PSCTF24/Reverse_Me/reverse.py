input_file_path = 'img.jpg'
output_file_path = 'img'

with open(input_file_path, 'rb') as file:
    reversed_content = file.read()[::-1]

with open(output_file_path, 'wb') as reversed_file:
    reversed_file.write(reversed_content)

print(f'Done.\nFile: {output_file_path}')
