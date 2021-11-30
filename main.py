# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
import Server
def print_program_info():
    # TODO - Change your name
    print("Fiseha Tessema")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results
    #The IP address is passed as a string to the Server class in the server.py module
    ec2Server = Server.Server("52.41.99.1")
