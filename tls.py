import rsa

class Certificate:
    def __init__(self, common_name, public_key):
        self.common_name = common_name
        self.public_key = public_key

def simulate_server():
    # Generate the server's key pair and certificate (self-signed for simulation)
    server_key = rsa.full_gen()
    server_certificate = Certificate("Server Certificate", server_key[0])

    print("Server is waiting for the client...")

    while True:
        # Simulate a client connecting
        client_key = rsa.full_gen()

        # Simulate key exchange: Server sends its certificate to the client
        server_certificate_data = {
            "common_name": server_certificate.common_name,
            "public_key": server_certificate.public_key
        }
        print("Server sends its certificate to the client.")

        # Simulate the client receiving the server's certificate
        client_received_server_certificate_data = server_certificate_data

        server_public_key = server_key[0]
        print("Server public key -> client.")

        client_received_server_public_key = server_public_key

        # Simulate client message encryption (user input)
        client_msg = input("Enter a message to encrypt ('exit' to terminate): ")
        if client_msg.lower() == 'exit':
            break

        encrypted_message = rsa.encrypt(client_received_server_public_key, client_msg)

        print("Client encrypted message -> server.")

        decrypted_message = rsa.decrypt(server_key[1], encrypted_message)
        print(f"Server received and decrypted the message: {decrypted_message}")

def main():
    simulate_server()

if __name__ == '__main__':
    main()