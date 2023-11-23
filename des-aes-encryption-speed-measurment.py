from Crypto.Cipher import DES,AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
import time

def DESPerformance():
    ## encryption speed = size of message / average time
    key = get_random_bytes(8)
    chunk_of_string_size = 16 * 1024 #16KB block size used for larger files
    cipher = DES.new(key, DES.MODE_CBC, IV=get_random_bytes(8))
    encrypted_data = b''
    start_time = time.perf_counter()

    with open('csi4460HW2','rb') as file:
          file.seek(0, 2)  # Move to the end of the file
          file_size = file.tell() / (1024 * 1024)  # Get the current position, which is the file size. Converts the size into MB
          file.seek(0)  # Reset file pointer to the beginning
          while True:
            chunkOfPlaintext = file.read(chunk_of_string_size)
            if not chunkOfPlaintext:
                break
            padded_chunk_of_plaintext = pad(chunkOfPlaintext, DES.block_size)
            encrypted_data += cipher.encrypt(padded_chunk_of_plaintext)
    encodedEncryptedData = b64encode(cipher.iv + encrypted_data)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    average_time = (end_time - start_time) / 2
    encryption_speed = file_size / elapsed_time
    stopProgram = False
    
    print(f'DES Performance Data: ')
    print(f'File size: {file_size:.1f} MB')
    print(f'Start Time: {start_time:.4f} seconds')
    print(f'End Time: {end_time:.4f} seconds')
    print(f'Elapsed Time:  {elapsed_time:.4f} seconds')
    print(f'Average Time: {average_time:.4f} seconds')
    print(f'Encryption Speed: {encryption_speed:.2f} MB/s')
    
    stopProgram = False
    show_full_encrypted_message = input('Do you want to see the full encrypted message? (yes/no): Yes for full and No for Partially Encrypted Message: ')
    
    while not stopProgram:
        if show_full_encrypted_message.lower() == 'yes':
            print(f'Encrypted Data: {encodedEncryptedData}')
            show_full_encrypted_message = ''
            returnBack = input('Do you want to see the statisitcs of the data encrypted message? (yes/no): ')
            if returnBack.lower() == 'yes':
                 print(f'File size: {file_size:.1f} MB')
                 print(f'Start Time: {start_time:.4f} seconds')
                 print(f'End Time: {end_time:.4f} seconds')
                 print(f'Elapsed Time:  {elapsed_time:.4f} seconds')
                 print(f'Average Time: {average_time:.4f} seconds')
                 print(f'Encryption Speed: {encryption_speed:.2f} MB/s')
                 stopProgram = True
            else:
                 stopProgram = True
        else:
            print(f'Encrypted message (truncated): {encodedEncryptedData[:50]}...')
            stopProgram = True

def AESPerformance():

    block_size = 16
    chunk_of_string_size = 16 * 1024 #16KB block size used for larger files
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, IV=get_random_bytes(16))
    encrypted_data = b''

    start_time = time.perf_counter()
    with open('csi4460HW2','rb') as file:
          file.seek(0, 2)  # Move to the end of the file
          file_size = file.tell() / (1024 * 1024)  # Get the current position, which is the file size. Converts the size into MB
          file.seek(0)  # Reset file pointer to the beginning
          while True:
            chunkOfPlaintext = file.read(chunk_of_string_size)
            if not chunkOfPlaintext:
                break
            padded_chunk_of_plaintext = chunkOfPlaintext
            if len(chunkOfPlaintext) % block_size != 0:
#If the length of the chunk isn't a multiple of the block size, it calculates the required 
# padding with null bytes (\x00) and appends it to the chunk to create the padded_chunk.
                padding = b'\x00' * (block_size - len(chunkOfPlaintext) % block_size)
                padded_chunk_of_plaintext = chunkOfPlaintext + padding

            encrypted_chunk = cipher.encrypt(padded_chunk_of_plaintext)
            encrypted_data += encrypted_chunk
    stop_time = time.perf_counter()

    encodedEncryptedData = b64encode(cipher.iv + encrypted_data)
    elapsed_time = stop_time - start_time
    average_time = (stop_time - start_time) / 2
    encryption_speed = file_size / elapsed_time
    
    print('')
    print(f'AES Performance Data: ')
    print(f'Data size: {file_size:.1f} MB')
    print(f'Start Time: {start_time:.4f} seconds')
    print(f'End Time: {stop_time:.4f} seconds')
    print(f'Elapsed Time:  {elapsed_time:.4f} seconds')
    print(f'Average Time: {average_time:.4f} seconds')
    print(f'Encryption Speed: {encryption_speed:.2f} MB/s')
    stopProgram = False
    show_full_encrypted_message = input('Do you want to see the full encrypted message? (yes/no): Yes for full and No for Partially Encrypted Message: ')

    while not stopProgram:
        if show_full_encrypted_message.lower() == 'yes':
            print(f'Encrypted Data: {encodedEncryptedData}')
            show_full_encrypted_message = ''
            returnBack = input('Do you want to see the statisitcs of the data encrypted message? (yes/no): ')
            if returnBack.lower() == 'yes':
                 print(f'File size: {file_size:.1f} MB')
                 print(f'Start Time: {start_time:.4f} seconds')
                 print(f'End Time: {stop_time:.4f} seconds')
                 print(f'Elapsed Time:  {elapsed_time:.4f} seconds')
                 print(f'Average Time: {average_time:.4f} seconds')
                 print(f'Encryption Speed: {encryption_speed:.2f} MB/s')
                 print('Thank You for using the Encryption Speed Statistics Python Program')
                 stopProgram = True
            else:
                 print('Thank You for using the Encryption Speed Statistics Python Program')
                 stopProgram = True
        else:
            print(f'Encrypted message (truncated): {encodedEncryptedData[:50]}...')
            stopProgram = True

DESPerformance()
AESPerformance()