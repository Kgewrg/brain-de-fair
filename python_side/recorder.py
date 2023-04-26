import mindwave, time, datetime,random

print('Connecting to Mindwave...')
headset = mindwave.Headset('COM9')

print('Connected, waiting 10 seconds for data to start streaming')
time.sleep(10)
#time for recording
testtime=10 #minutes

now = time.time()
future = now + 60 * testtime
    # text = str(headset.poor_signal) + "," + str(headset.raw_value) + "," + str(headset.attention) + "," + str(headset.meditation) 
    #f.write("poor_signal , raw,attention , meditation\n")
while time.time() < future:
    number = random.randint(30, 100)#bot player
    text= str(headset.attention)+","+str(number)
    print(text,"  poor ",headset.poor_signal)
    try:
        with open("C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv", "w") as f :
            f.write(text + "\n")
    except (PermissionError):
        print("File was not opened: skiping")
    print("wrote to file:", text)
    time.sleep(0.9)
