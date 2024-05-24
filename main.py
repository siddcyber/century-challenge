import paramiko

# Define a dictionary to store the passwords for each level
password = {
    'century1': 'century1',
    'century2': '10.0.14393.6343',
    'century3': 'invoke-webrequest443',
    'century4': '123',
    'century5': '34182',
    'century6': 'underthewire3347',
    'century7': '197',
    'century8': '7points',
    'century9': '696',
    'century10': 'pierid',
    'century11': 'windowsupdates110'
}


# Function to execute a command on the SSH server and return the output
def ssh_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(str(command))
    value = stdout.read().decode().strip()
    return value


# Function to connect to the SSH server and execute commands based on the level
def ssh_connect(user, Password, level):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(port=22, hostname='century.underthewire.tech', username=user, password=Password)

    # Level-specific commands
    if level == 1:
        # Print the current path and the PowerShell version
        print(ssh_command(ssh, 'pwd'))
        print(ssh_command(ssh, 'echo $PSVersionTable'))
    if level == 2:
        # Get the name of the Invoke-WebRequest cmdlet and the name of the file on the desktop, and print them in
        # lowercase
        cmdlet_name = ssh_command(ssh, 'Get-Command -Verb Invoke -Noun WebRequest')
        lines = cmdlet_name.split('\n')
        cmdlet_line = lines[-1]
        output = cmdlet_line.split()[1]
        file_name = ssh_command(ssh, 'dir')
        lines = file_name.split('\n')
        file_line = lines[-1]
        output2 = file_line.split()[-1]
        print((output + output2).lower())
    if level == 3:
        # Print the number of items in the current directory
        print(ssh_command(ssh, '( Get-ChildItem | Measure-Object ).Count'))
    if level == 4:
        # Print the contents of the "Can You Open Me" directory
        print(ssh_command(ssh, 'cd ".\\Can You Open Me"; dir'))
    if level == 5:
        # Get the short name of the domain and the name of the file on the desktop, and print them in lowercase
        value2 = ssh_command(ssh, 'dir')
        lines = value2.split('\n')
        line = lines[-1]
        output = line.split()[-1]
        value1 = ssh_command(ssh, '(Get-WmiObject Win32_ComputerSystem).Domain ').lower()
        value1 = value1.replace('.tech', '')
        print((value1 + output).lower())
    if level == 6:
        # Print the current path and the number of items in the current directory
        print(ssh_command(ssh, 'pwd'))
        print(ssh_command(ssh, '( Get-ChildItem | Measure-Object ).Count'))
    if level == 7:
        # Print the contents of all readme.txt files in the current user's directory and subdirectories
        readme_files = ssh_command(ssh,
                                   'cat (Get-ChildItem -Path C:\\users\\century7 -Recurse -Filter readme.txt |  Select-Object -ExpandProperty FullName)')
        print(readme_files)
    if level == 8:
        # Print the length of the contents of the unique.txt file
        print(ssh_command(ssh, '(cat unique.txt).length'))
    if level == 9:
        # Print the 161st word in the Word_File.txt file
        print(ssh_command(ssh, '$content = [IO.File]::ReadAllText(".\Word_File.txt"); $content.split()[160]'))
    if level == 10:
        # Get the name of the file on the desktop and the 10th and 8th words of the Windows Update service description,
        # and print them in lowercase
        file_name = ssh_command(ssh, 'dir')
        lines = file_name.split('\n')
        file_name = lines[-1].split()[-1]
        print(file_name)
        service_description = ssh_command(ssh,
                                          '(Get-WmiObject win32_service | select * | where DisplayName -like "Windows Update*" ).Description')
        words = service_description.split()
        word_10 = words[17]  # 10th word
        word_8 = words[15]  # 8th word
        output = (word_10 + word_8 + file_name).lower()
        print(output)


# Connect to the SSH server and execute commands for each level
ssh_connect(user='century1', Password=password['century1'], level=1)
ssh_connect(user='century2', Password=password['century2'], level=2)
ssh_connect(user='century3', Password=password['century3'], level=3)
ssh_connect(user='century4', Password=password['century4'], level=4)
ssh_connect(user='century5', Password=password['century5'], level=5)
ssh_connect(user='century6', Password=password['century6'], level=6)
ssh_connect(user='century7', Password=password['century7'], level=7)
ssh_connect(user='century8', Password=password['century8'], level=8)
ssh_connect(user='century9', Password=password['century9'], level=9)
ssh_connect(user='century10', Password=password['century10'], level=10)

