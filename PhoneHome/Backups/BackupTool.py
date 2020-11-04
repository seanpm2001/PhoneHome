# Start of script
formatSMS = ["*.txt", "*.xml", "*bin"]
formatPCALL = ["*.xml", "*.ogg", "*.mp3", "*.bin", "*.xspf"]
print ("Backup - PhoneHome")
confirmYN = str(input("Are you ready to backup your phone calls/messages? (Y/N)"))
answer = confirmYN.upper()
if (answer == "Y"):
  print ("Backup methods")
  print ("\nBackup text messages")
  print ("Formats: \n" + formatSMS())
  print ("\nBackup phone calls")
  print ("Formats: \n" + formatPCALL())
  pcallBackupYN = str(input("Do you want to backup phone calls? (Y/N)"))
  answer2 = pcallBackuPYN.upper()
  if (answer2 == "Y"):
    print ("Backing up phone calls...")
    print ("Progress: unknown")
    print ("This feature is not yet ready")
  else:
    print ("Phone call backup canceled")
  smsBackupYN = str(input("Do you want to backup text messages? (Y/N)"))
  answer3 = smsBackupYN.upper()
  if (answer3 == "Y"):
    print ("Backing up text messagess...")
    print ("Progress: unknown")
    print ("This feature is not yet ready")
  else:
    print ("Text message backup canceled")
  print ("Backup results: " + "This feature is not yet ready")
else:
  print ("Backup canceled")
noMore = input("Press [ENTER] key to exit")
print ("The program should be closed. If the program has not exited yet, press the close button. If this doesn't work, end the process with a resource manager/task manager")
# End of script
"""
File info
File version: 1 (Tuesday, November 4th 2020 at 2:07 pm)
File type: Python script file (*.py)
Line count (including blank lines and compiler line): 41
"""
