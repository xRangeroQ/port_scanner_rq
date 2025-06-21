# Libraries
import socket
import threading
import time

# Module Class
class scan_port():
    # Initialize
    def __init__(self, Ip="127.0.0.1", ThreadCount=50, Timeout=0.05, Start_Port=1, End_Port=65535):
        # Set Values
        self.Ip=Ip
        self.ThreadCount=ThreadCount
        self.Timeout=Timeout
        self.Start_Port=Start_Port
        self.End_Port=End_Port
        self.Threads=[]
        self.Ports=[]
        self.ThreadLock=threading.Lock()


    # Scan Function
    def Scan(self, start_port):
        port=start_port
        while port <= self.End_Port:
            sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.Timeout)

            try:
                result=sock.connect_ex((self.Ip, port))

                with self.ThreadLock:
                    if result==0:
                        self.Ports.append(port)

            except Exception as e:
                print(e)
            
            finally:
                sock.close()

            port+=self.ThreadCount
    

    # Run Function
    def run(self):
        # Get Start Time
        startTime=time.time()

        # Create Threads
        for i in range(self.ThreadCount):
            start_port=self.Start_Port+i
            t1=threading.Thread(target=self.Scan, args=(start_port, ))
            t1.start()
            self.Threads.append(t1)

        for i in self.Threads:
            i.join()

        # Get End Time && Process time
        endTime=time.time()
        Process=endTime-startTime

        # Show TCP Ports
        print("Açık Portlar: " + ', '.join(map(str, self.Ports)))
        print(f"Geçen süre: {str(Process)[:6]} Saniye")
