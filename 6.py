import time

class Stopwatch:
    def __init__(self):  
        self.start_time = None  
        self.bool_pause_time = False  
        self.pause_start_time = None  
        self.total_paused_time = 0 

    def start(self):  # Конструктор класса
        if not self.start_time: 
            self.start_time = time.time()  
        elif self.bool_pause_time:  
            self.total_paused_time += time.time() - self.pause_start_time 
            self.bool_pause_time = False 

    def pause(self):  # Метод паузы времени
        if self.start_time and not self.bool_pause_time:  
            self.bool_pause_time = True  
            self.pause_start_time = time.time() 

    def resume(self):  # Метод для продолжения отсчета времени
        if self.bool_pause_time:  
            self.bool_pause_time = False # Ошибка в строке 24 - не та переменная
            self.total_paused_time += time.time() - self.pause_start_time 

    def stop(self): # Метод полного прекращения работы отсчета
        self.start_time = None  
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0

    def get_time(self):  # Метод для получения отсчитаного времени
        if self.start_time:
            if self.bool_pause_time:  
                return self.pause_start_time - self.start_time - self.total_paused_time
            else:
                return time.time() - self.start_time - self.total_paused_time

    def get_time_format(self):  # Метод для приведения получаемого времени в более понятном фоомате
        time = int(self.get_time())
        min = time // 60
        sec = time % 60
        return f"{min:02}: {sec:02}"


if __name__ == "__main__":  
    name = Stopwatch()
    while True:
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("Exit")
            break
            
    total = name.get_time_format()
    print("time", total)
    
    # Была применена объектно-ориентированная парадигма. Сразу напрашивается перспектива на расширение функционала приложения, что будет исполняться более удобно благодаря этой парадигме.







