# python script showing battery details
try:
  import psutil
  from win10toast import ToastNotifier
  import time

  # function returning time in hh:mm:ss
  #def convertTime(seconds):
  #    minutes, seconds = divmod(seconds, 60)
  #    hours, minutes = divmod(minutes, 60)
  #    return "%d:%02d:%02d" % (hours, minutes, seconds)

  # returns a tuple
  battery = psutil.sensors_battery()

  #print("Battery percentage : ", battery.percent)
  #print("Power plugged in : ", battery.power_plugged)
    
  # converting seconds to hh:mm:ss
  #print("Battery left : ", convertTime(battery.secsleft))

  # create win10 notif
  toast = ToastNotifier()
  if battery.percent <= 30 and battery.power_plugged == False:
    while True:
      battery = psutil.sensors_battery()
      if battery.power_plugged == False:
        print(str(battery.power_plugged))
        toast.show_toast("CHARGE NOW!!!", "Battery is at " + str(battery.percent) + "%")
        while toast.notification_active(): time.sleep(0.1)
        time.sleep(60)
      else:
        break
  elif battery.percent >= 90 and battery.power_plugged == True:   
    while True:
      battery = psutil.sensors_battery()
      if battery.power_plugged == False:
        print(str(battery.power_plugged))
        toast.show_toast("REMOVE CHARGE NOW!!!", "Battery is at " + str(battery.percent) + "%")
        while toast.notification_active(): time.sleep(0.1)
        time.sleep(60)
      else:
        break
  else:
    quit()
except Exception as e:
  print(e)
finally:
  quit()