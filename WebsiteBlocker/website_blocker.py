import sys
from datetime import datetime as dt


# Creating the variable to hold the file path for the hosts file
hosts_file_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

# The IP to redirect for unwanted websites(this machine)
redirect_ip = "127.0.0.1"

# Unwanted website list
# Getting this unwanted list from the user
unwanted_websites = sys.argv[1:]

# The starting hour from which the websites should be blocked
start_hour = 8

# The ending hour to unblock the websites
end_hour = 16


def block_websites():
    """
    Method which reads the host file and appends the unwanted websites
    if not already present
    :return:
    """
    with open(hosts_file_path, "r+") as file_handler:
        content = file_handler.read()

        # Iterate through the website list
        for website in unwanted_websites:
            if website in content:
                # Website already blocked
                pass
            else:
                # Modify the hosts file
                file_handler.write(redirect_ip + " " + website + "\n")


def unblock_websites():
    """
    Method to unblock the websites and modify the hosts file
    :return:
    """
    with open(hosts_file_path, "r+") as file_handler:
        content = file_handler.readlines()

        # Seeking the file pointer to the beginning of the file
        file_handler.seek(0)
        for line in content:
            if not any(website in line for website in unwanted_websites):
                file_handler.write(line)
        file_handler.truncate()


while True:
    # Check if the current time is between the time range
    # where you do not want to browse the website

    # Comparing datetime objects

    if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                                   dt.now().day, end_hour):
        # Block the websites
        # Need to have administrator permission to access the host file

        # Open the host file and read the contents
        # Read and append mode r+
        block_websites()

    else:
        # These are not the hours where you want the website blocked
        # Open the hosts file and read the contents
        # Reading contents line by line
        unblock_websites()
