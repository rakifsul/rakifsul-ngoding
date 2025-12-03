# file: main.py

# begin: import modules
import _thread
import time
# end: import modules

# buat class PenampungThread
# walaupun kita tidak sedang menggunakan modul threading.Thread, ini juga bisa
class PenampungThread:

    # class constructor dengan input nama thread
    def __init__(self, nama_thread):
        # assign nama
        self.nama = nama_thread

    # method ini dijalankan dengan thread
    # jeda adalah waktu jedanya
    def run(self, jeda):
        # counter
        ctr = 0

        # sampai selama mungkin
        while 1:
            # terapkan jeda sebesar jeda
            time.sleep(jeda)
            # print nama thread dan counter nya
            print(self.nama, ":", str(ctr))
            # naikkan counter
            ctr+=1

# begin: membuat objek PenampungThread
th1 = PenampungThread("thread-a")
th2 = PenampungThread("thread-b")
# end: membuat objek PenampungThread

try:
      # begin: mulai thread
      _thread.start_new_thread(th1.run, (2,))
      _thread.start_new_thread(th2.run, (4,))
      # end: mulai thread
except:
      # kalau thread tidak bisa dijalankan
      print ("Error: tidak bisa memulai thread")

# mencegah program keluar sebelum thread berjalan
while 1:
      pass