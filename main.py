import paramiko
import os

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


def ssh_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(str(command))
    value = stdout.read().decode().strip()
    return value


def ssh_connect(user, Password, level):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(port=22, hostname='century.underthewire.tech', username=user, password=Password)
    # Execute a command to get the current path
    if level == 1:
        print(ssh_command(ssh, 'pwd'))
        print(ssh_command(ssh, 'echo $PSVersionTable'))
    if level == 2:
        # Get the name of the cmdlet
        cmdlet_name = ssh_command(ssh, 'Get-Command -Verb Invoke -Noun WebRequest')
        lines = cmdlet_name.split('\n')
        cmdlet_line = lines[-1]
        output = cmdlet_line.split()[1]
        # Get the name of the file on the desktop
        file_name = ssh_command(ssh, 'dir')
        lines = file_name.split('\n')
        file_line = lines[-1]
        output2 = file_line.split()[-1]
        print((output + output2).lower())
    if level == 3:
        # print(ssh_command(ssh, 'dir'))
        print(ssh_command(ssh, '( Get-ChildItem | Measure-Object ).Count'))
    if level == 4:
        print(ssh_command(ssh, 'cd ".\\Can You Open Me"; dir'))
    if level == 5:
        value2 = ssh_command(ssh, 'dir')
        lines = value2.split('\n')
        line = lines[-1]
        output = line.split()[-1]
        # Get the short name of the domain
        value1 = ssh_command(ssh, '(Get-WmiObject Win32_ComputerSystem).Domain ').lower()
        # remove .tech before using as the password
        value1 = value1.replace('.tech', '')
        print((value1 + output).lower())
    if level == 6:
        print(ssh_command(ssh, 'pwd'))
        print(ssh_command(ssh, '( Get-ChildItem | Measure-Object ).Count'))
    if level == 7:
        readme_files = ssh_command(ssh,
                                   'cat (Get-ChildItem -Path C:\\users\\century7 -Recurse -Filter readme.txt |  Select-Object -ExpandProperty FullName)')
        print(readme_files)
    if level == 8:
        print(ssh_command(ssh, '(cat unique.txt).length'))
    if level == 9:
        print(ssh_command(ssh, '$content = [IO.File]::ReadAllText(".\Word_File.txt"); $content.split()[160]'))
    if level == 10:
        file_name = ssh_command(ssh, 'dir')
        lines = file_name.split('\n')
        file_name = lines[-1].split()[-1]
        print(file_name)
        # Execute a command to get the Windows Update service description and get the 10th and 8th words
        service_description = ssh_command(ssh,
                                          '(Get-WmiObject win32_service | select * | where DisplayName -like "Windows Update*" ).Description')
        words = service_description.split()
        word_10 = words[17]  # 10th word
        word_8 = words[15]  # 8th word
        # Combine the words and the file name to form the password
        password = (word_10 + word_8 + file_name).lower()
        print(password)


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
