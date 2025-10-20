import time
import math
import os
from datetime import datetime

class ASCIIClock:
    def __init__(self):
        self.digits = {
            '0': [" ███ ", "█   █", "█   █", "█   █", " ███ "],
            '1': ["  █  ", " ██  ", "  █  ", "  █  ", " ███ "],
            '2': [" ███ ", "    █", " ███ ", "█    ", "█████"],
            '3': [" ███ ", "    █", " ███ ", "    █", " ███ "],
            '4': ["█   █", "█   █", "█████", "    █", "    █"],
            '5': ["█████", "█    ", "█████", "    █", "████ "],
            '6': [" ███ ", "█    ", "████ ", "█   █", " ███ "],
            '7': ["█████", "    █", "   █ ", "  █  ", "  █  "],
            '8': [" ███ ", "█   █", " ███ ", "█   █", " ███ "],
            '9': [" ███ ", "█   █", " ████", "    █", " ███ "],
            ':': ["     ", "  █  ", "     ", "  █  ", "     "],
            ' ': ["     ", "     ", "     ", "     ", "     "]
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_digital(self):
        try:
            while True:
                self.clear_screen()
                now = datetime.now()
                time_str = now.strftime("%H:%M:%S")
                date_str = now.strftime("%A, %B %d, %Y")
                
                print("\n" + "=" * 80)
                print("╔" + "═" * 78 + "╗")
                print("║" + " " * 25 + "DIGITAL CLOCK" + " " * 40 + "║")
                print("║" + " " * 25 + "by wortex213433" + " " * 38 + "║")
                print("╚" + "═" * 78 + "╝")
                print()
                
                lines = ["", "", "", "", ""]
                for char in time_str:
                    digit_lines = self.digits.get(char, self.digits[' '])
                    for i in range(5):
                        lines[i] += digit_lines[i] + "  "
                
                for line in lines:
                    print(" " * 15 + line)
                
                print()
                print(" " * 28 + "─" * 24)
                print(" " * 28 + f"   {date_str}")
                print(" " * 28 + "─" * 24)
                print()
                
                timezone = time.strftime("%Z")
                print(" " * 25 + f"Time Zone: {timezone} (24-hour format)")
                print()
                print("=" * 80)
                print(" " * 25 + "Press Ctrl+C to exit")
                print(" " * 28 + "Made by wortex213433") 
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.clear_screen()
            print("\n👋 Clock stopped. Goodbye!\n")
    
    def display_analog(self):
        try:
            while True:
                self.clear_screen()
                now = datetime.now()
                hour = now.hour % 12
                minute = now.minute
                second = now.second
                
                date_str = now.strftime("%A, %B %d, %Y")
                time_str = now.strftime("%H:%M:%S")
                
                print("\n" + "=" * 80)
                print("╔" + "═" * 78 + "╗")
                print("║" + " " * 26 + "ANALOG CLOCK" + " " * 40 + "║")
                print("║" + " " * 25 + "by wortex213433" + " " * 38 + "║")
                print("╚" + "═" * 78 + "╝")
                print()
                
                size = 25
                canvas = [[' ' for _ in range(size)] for _ in range(size)]
                center = size // 2
                
                for y in range(size):
                    for x in range(size):
                        dx = x - center
                        dy = y - center
                        dist = math.sqrt(dx*dx + dy*dy)
                        if 9.5 <= dist <= 10.5:
                            canvas[y][x] = '○'
                
                numbers = [
                    (12, center, center - 10, '12'),
                    (3, center + 9, center, '3'),
                    (6, center, center + 9, '6'),
                    (9, center - 9, center, '9')
                ]
                
                for num, x, y, label in numbers:
                    if 0 <= y < size and 0 <= x < size:
                        canvas[y][x] = '█'
                    if num == 12 and y - 1 >= 0:
                        for i, c in enumerate(label):
                            if x - 1 + i < size:
                                canvas[y-1][x-1+i] = c
                    elif num == 6 and y + 1 < size:
                        canvas[y+1][x] = label[0]
                    elif num == 3 and x + 2 < size:
                        canvas[y][x+2] = label
                    elif num == 9 and x - 2 >= 0:
                        canvas[y][x-2] = label
                
                hour_angle = math.radians(90 - (hour * 30 + minute * 0.5))
                for i in range(1, 6):
                    x = int(center + i * math.cos(hour_angle))
                    y = int(center - i * math.sin(hour_angle))
                    if 0 <= y < size and 0 <= x < size:
                        canvas[y][x] = '█'
                
                minute_angle = math.radians(90 - minute * 6)
                for i in range(1, 9):
                    x = int(center + i * math.cos(minute_angle))
                    y = int(center - i * math.sin(minute_angle))
                    if 0 <= y < size and 0 <= x < size:
                        canvas[y][x] = '▓'
                
                second_angle = math.radians(90 - second * 6)
                for i in range(1, 10):
                    x = int(center + i * math.cos(second_angle))
                    y = int(center - i * math.sin(second_angle))
                    if 0 <= y < size and 0 <= x < size:
                        canvas[y][x] = '·'
                
                canvas[center][center] = '●'
                
                for row in canvas:
                    print(" " * 28 + ''.join(row))
                
                print()
                print(" " * 28 + "─" * 24)
                print(" " * 32 + f"{time_str}")
                print(" " * 28 + f"   {date_str}")
                print(" " * 28 + "─" * 24)
                print()
                print(" " * 25 + f"Time Zone: {time.strftime('%Z')} (24-hour format)")
                print()
                print("=" * 80)
                print(" " * 25 + "Press Ctrl+C to exit")
                print(" " * 28 + "Made by wortex213433")
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.clear_screen()
            print("\n👋 Clock stopped. Goodbye!\n")

def main():
    clock = ASCIIClock()
    
    print("\n" + "╔" + "═" * 48 + "╗")
    print("║" + " " * 16 + "ASCII CLOCK" + " " * 21 + "║")
    print("║" + " " * 13 + "by wortex213433" + " " * 20 + "║")
    print("╚" + "═" * 48 + "╝")
    print("\n⏰ Choose clock type:")
    print("  1. Digital Clock")
    print("  2. Analog Clock")
    print()
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        clock.display_digital()
    elif choice == '2':
        clock.display_analog()
    else:
        print("Invalid choice! Starting digital clock...")
        time.sleep(1)
        clock.display_digital()

if __name__ == "__main__":
    main()
