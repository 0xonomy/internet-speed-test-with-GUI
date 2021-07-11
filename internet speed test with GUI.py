from tkinter import *
import speedtest
import socket
import time


def test():
    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
        print(f"You are not connected to internet! Please check you connection.")
        message.config(text = "CONNECT TO INTERNET!")
        time.sleep(6)
    else:
        test = speedtest.Speedtest()

        print(f"Loading servers...")
        test.get_servers()
        print("Chosing best server...")
        best = test.get_best_server()
        print(f"Found: {best['host']} located in {best['name']}, {best['country']}")

        print()

        ping_result = round(test.results.ping)

        print(f"Performing download test...")
        download_result = round((test.download()/1024)/1024)

        print(f"Performing upload test...")
        upload_result = round((test.upload()/1024)/1024)

        print("DONE!")

        ping_res.config(text = str(ping_result) + "ms")
        down_res.config(text = str(download_result) + "MB/s")
        upload_res.config(text = str(upload_result) + "MB/s")


root = Tk()
root.geometry('600x600')
root.resizable(False, False)
root.configure(bg='#42f5a4')
root.iconbitmap('icon.ico')
root.title("Internet Speed Test")


download = Label(root, text="Download:", font=('Source Sans Pro',16), bg='#42f5a4')
ping = Label(root, text="Ping:", font=('Source Sans Pro',16), bg='#42f5a4')
upload = Label(root, text="Upload:", font=('Source Sans Pro',16), bg='#42f5a4')
download.place(x=70, y=30)
ping.place(x=280, y=30)
upload.place(x=460, y=30)


down_res = Label(root, text=" ", font=('sans-serif', 16), bg='#42f5a4')
ping_res = Label(root, text=" ", font=('sans-serif', 16), bg='#42f5a4')
upload_res = Label(root, text=" ", font=('sans-serif', 16), bg='#42f5a4')
down_res.place(x=70, y=70)
ping_res.place(x=280, y=70)
upload_res.place(x=460, y=70)


message = Label(root, text="", bg='#42f5a4', font=('Nunito',18))
message.place(x=160 , y=300)


button = Button(root, text="Start Test", font=('Nunito',19), command=test)
button.place(x=230, y=370)

by = Label(root, text="By GoldenJoker", fg='#1577b0', bg='#42f5a4', font=('Helvetica',14))
by.place(x=0, y=575)

root.mainloop()