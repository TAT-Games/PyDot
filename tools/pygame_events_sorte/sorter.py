sorted_notifications: list = []

notifications_file = open("sandbox/notifications.txt", "r")
for notification in notifications_file:
    if notification.startswith("<Event"):
        sorted_notifications.append(notification)
    
    elif len(sorted_notifications) > 0:
        sorted_notifications[-1] += notification
        print(len(sorted_notifications))
        print(notification)

notifications_file.close()

sorted_notifications_file = open("sandbox/sorted_notifications.txt", "w")
for notification in sorted_notifications:
    sorted_notifications_file.write(notification)

sorted_notifications_file.close()

print("Done")