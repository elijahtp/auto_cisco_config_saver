import paramiko
import time
import socket
from pprint import pprint
import snoop
@snoop

def text_clear(text):
    """Удаление пунктуации"""
    import string
    for p in string.punctuation + '\n':
        if p in text:
            text = text.replace(p, '')
    return text




def send_show_command(
    ip,
    username,
    password,
    enable,
    command,
    max_bytes=60000,
    short_pause=1,
    long_pause=5,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with cl.invoke_shell() as ssh:
        ssh.send("enable\n")
        ssh.send(f"{enable}\n")
        time.sleep(short_pause)
        ssh.send("terminal length 0\n")
        time.sleep(short_pause)
        ssh.recv(max_bytes)
        result = {}
        resultstring=""
        for command in commands:
            ssh.send(f"{command}\n")
            ssh.settimeout(1)
            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break
            result[command] = output
        return result
if __name__ == "__main__":
    devices = ["172.16.99.101","172.16.99.102","172.16.99.103","172.16.99.104","172.16.99.105","172.16.99.106","172.16.99.107","172.16.99.108","172.16.99.109","172.16.99.110","172.16.99.111","172.16.99.112","172.16.99.113","172.16.99.114","172.16.99.115","172.16.99.116","172.16.99.117", "172.16.99.118", "172.16.99.120", "172.16.99.121"]

    for device in devices:
        status_connection = []
        commands = ["copy running-config tftp","172.16.99.205",""]
        result = send_show_command(device, "user", "password", "password", commands)
        print("commands applied to switch: {}".format(device))

