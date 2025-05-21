import zlib , base64

compressed_data = open("compressed.txt", "r").read()
data_bytes = compressed_data.encode('utf-8')
print(data_bytes)
compressed_data = base64.b64decode(data_bytes)
decompressed_data = zlib.decompress(compressed_data)
print(decompressed_data)