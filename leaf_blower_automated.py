import pyautogui

size = pyautogui.size()
print(size)

currently = pyautogui.position()
print(currently)

pos_list={"pos_1": (220, 195), "pos_2": (960, 195), "pos_3": (1700, 195),
		  "pos_a": (220, 367), "pos_b": (960, 367),	"pos_c": (1700, 367),
		  "pos_4": (220, 540), "pos_5": (960, 540), "pos_6": (1700, 540),
		  "pos_d": (220, 712), "pos_e": (960, 712), "pos_f": (1700, 712),
		  "pos_7": (220, 885), "pos_8": (960, 885), "pos_9": (1700, 885)}

def late_blower():
	while True:
		pyautogui.moveTo(pos_list["pos_1"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_3"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_6"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_4"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_7"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_9"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_6"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_4"], duration = 0.4)

def early_blower():
	while True:
		pyautogui.moveTo(pos_list["pos_1"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_3"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_c"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_a"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_4"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_6"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_f"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_d"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_7"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_9"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_f"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_d"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_4"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_6"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_c"], duration = 0.4)
		pyautogui.moveTo(pos_list["pos_a"], duration = 0.4)

mode = input()	
if mode == "late game":
	late_blower()
elif mode == "early game":
	early_blower()