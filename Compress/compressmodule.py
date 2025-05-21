import zlib, base64 

def compress_file(input_file, output_file):
    data =  open(input_file, "r").read()
    data_bytes = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(output_file, "w")
    compressed_file.write(decoded_data)
    compressed_file.close()

def decompress_file(input_file, output_file):
    compressed_data = open(input_file, "r").read()
    data_bytes = compressed_data.encode('utf-8')
    compressed_data = base64.b64decode(data_bytes)
    decompressed_data = zlib.decompress(compressed_data)
    decompressed_file = open(output_file, "w")
    decompressed_file.write(decompressed_data.decode('utf-8'))
    decompressed_file.close()

decompress_file('ot.txt','dc1.txt') 