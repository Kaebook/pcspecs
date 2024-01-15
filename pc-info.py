import tkinter as tk
import wmi

def get_pc_info():
    computer = wmi.WMI()

    info = []
    
    try:
        for component in computer.Win32_ComputerSystem():
            info.append(f"Model: {component.Model}")
            info.append(f"Manufacturer: {component.Manufacturer}")
    except Exception as e:
        info.append("Failed to retrieve computer system information")

    try:
        for processor in computer.Win32_Processor():
            info.append(f"Processor: {processor.Name}")
    except Exception as e:
        info.append("Failed to retrieve processor information")

    try:
        for gpu in computer.Win32_VideoController():
            info.append(f"GPU: {gpu.Name}")
    except Exception as e:
        info.append("Failed to retrieve GPU information")

    try:
        for disk in computer.Win32_DiskDrive():
            info.append(f"Hard Drive: {disk.Model}")
    except Exception as e:
        info.append("Failed to retrieve hard drive information")

    try:
        for motherboard in computer.Win32_BaseBoard():
            info.append(f"Motherboard: {motherboard.Product}")
    except Exception as e:
        info.append("Failed to retrieve motherboard information")

    try:
        for power_supply in computer.Win32_Battery():
            info.append(f"Power Supply: {power_supply.Name}")
    except Exception as e:
        info.append("Failed to retrieve power supply information")

    try:
        for monitor in computer.Win32_DesktopMonitor():
            info.append(f"Monitor: {monitor.Name}")
    except Exception as e:
        info.append("Failed to retrieve monitor information")

    try:
        for keyboard in computer.Win32_Keyboard():
            info.append(f"Keyboard: {keyboard.Name}")
    except Exception as e:
        info.append("Failed to retrieve keyboard information")

    try:
        for mouse in computer.Win32_PointingDevice():
            info.append(f"Mouse: {mouse.Name}")
    except Exception as e:
        info.append("Failed to retrieve mouse information")

    try:
        for speaker in computer.Win32_SoundDevice():
            info.append(f"Speaker: {speaker.Name}")
    except Exception as e:
        info.append("Failed to retrieve speaker information")

    return info

def display_info():
    pc_info = get_pc_info()
    info_text.delete(1.0, tk.END)
    for item in pc_info:
        info_text.insert(tk.END, item + "\n")
    

window = tk.Tk()
window.title("PC Information")
window.geometry("800x600")
window.configure(bg="#282828")

info_text = tk.Text(window, height=25, width=80, bg="#323232", fg="white")
info_text.pack(fill=tk.BOTH, padx=10, pady=10)
info_text.configure(font=("Arial", 12))

get_info_btn = tk.Button(window, text="Get Info", command=display_info, bg="#4285F4", fg="white")
get_info_btn.pack(pady=10)

window.mainloop()
