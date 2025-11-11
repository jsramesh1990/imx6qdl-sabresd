import tkinter as tk
import time

# LED labels according to boot flow
led_names = [
    "Power", 
    "U-Boot1","U-Boot2","U-Boot3","U-Boot4",
    "Kernel1","Kernel2","Kernel3","Kernel4",
    "RootFS1","RootFS2","RootFS3",
    "Wi-Fi","Bluetooth","Ethernet","System Ready"
]

# Boot stages mapping (index ranges)
boot_stages = [
    (0,0),    # Power
    (1,4),    # U-Boot
    (5,8),    # Kernel
    (9,11),   # RootFS
    (12,14),  # Services: Wi-Fi/BT/Ethernet
    (15,15)   # System Ready
]

class LedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("i.MX6QDL Sabre SD LED Simulation")
        self.led_labels = []
        self.create_leds()
        self.root.after(1000, self.simulate_boot)  # start after 1 second

    def create_leds(self):
        for i, name in enumerate(led_names):
            frame = tk.Frame(self.root, padx=5, pady=5)
            frame.grid(row=i//4, column=i%4)
            label = tk.Label(frame, text=name, bg="grey", width=12, height=2, relief="ridge")
            label.pack()
            self.led_labels.append(label)

    def turn_on_range(self, start, end):
        for i in range(start, end+1):
            self.led_labels[i].config(bg="green")
        self.root.update()
        time.sleep(1)

    def simulate_boot(self):
        print("Simulating boot LED sequence...")
        for stage in boot_stages:
            start, end = stage
            self.turn_on_range(start, end)
        print("Boot sequence complete!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = LedGUI(root)
    root.mainloop()

