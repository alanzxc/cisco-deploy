#!usr/bin/env python
# Script by Steven Grove (@sigwo)
#           www.sigwo.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# 08-31-13 - v 0.1 Alpha

import sys
import datetime
import getpass
import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

user = raw_input("Please enter your username: ")
pass1 = getpass.getpass("Please enter your password: ") #Need to hash or encrypt or something
host = raw_input("Please put in IP address: ") # Add ability to browse for hosts.txt file of IP addresses
timestart = datetime.datetime.today() #time the script started

# Starts the deploy
# Open this as read-only or open a text box to paste in configs
with open(dir_path + '\config.txt', 'r+') as f:
	ssh = paramiko.SSHClient()
	ssh.connect(remote, username=user, password=pass1)
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("config")
# Validate config syntax, ensure the command is issued correctly. This will be a huge undertaking... :-/
# Need to know if a command failed
	exit_status = ssh_stdout.channel.recv_exit_status()

timeend = datetime.datetime.today() #time the script ended