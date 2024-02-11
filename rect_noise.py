import cv2 

donel = False
doner = False
x1,y1,x2,y2 = 0,0,0,0


def select(event, x, y, flag, param):
    global x1,x2,y1,y2,donel, doner
    if event == cv2.EVENT_LBUTTONDOWN:#indicates that the left mouse button is down.
        x1,y1 = x,y 
        donel = True
    elif event == cv2.EVENT_RBUTTONDOWN:#indicates that the left mouse button is down.
        x2,y2 = x,y
        doner = True    
        print(doner, donel)

def rect_noise():

    global x1,x2,y1,y2, donel, doner
    cap = cv2.VideoCapture(0)#VideoCapture has the device index or the name of a video file. The device index is just an integer to define a Camera. If we pass 0, it is for the first or primary camera, 1 for the second camera, etc.

    

    cv2.namedWindow("select_region")#namedWindow() method is used to create a window with a suitable name and size to display images and videos on the screen. 
    #The image by default is displayed in its original size, so we may need to resize the image for it to fit our screen.
    
    cv2.setMouseCallback("select_region", select)
    #The line cv2.setMouseCallback ('select_region',select) will set the function select as a response to any event received from mouse on the OpenCV window "select_region". 

    while True:
        _, frame = cap.read()#it returns a flag that will be true if frame is ready to be processed

        cv2.imshow("select_region", frame)#cv2.imshow() method is used to display an image in a window.

        if cv2.waitKey(1) == 27 or doner == True:
            #waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
            # It takes time in milliseconds as a parameter and waits for the given time to destroy the window,
            # if 0 is passed in the argument it waits till any key is pressed. 
            
            cv2.destroyAllWindows()
            #Python Opencv destroyAllWindows() function allows users to destroy or close all windows at any time after exiting the script. 
            # If you have multiple windows open at the same time and you want to close then you would use this function. It doesn’t take any parameters and doesn’t return anything.
            # It is similar to destroyWindow() function but this function only destroys a specific window unlike destroyAllWindows().

            
            print("gone--")
            break

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        frame1only = frame1[y1:y2, x1:x2]
        frame2only = frame2[y1:y2, x1:x2]

        diff = cv2.absdiff(frame2only, frame1only)#frames diffence with mod on all pixels
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (5,5))#cv2.blur() method is used to blur an image using the normalized box filter.blurring kernal size
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)#src,thresold value,maxpixel value,method
        #thresh_binary->converts pixels with less than thresold value to 0 otherwise to 255

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #findContours() method of cv2 library to find all boundary points(x,y) of an object in the image.
        # cv2.RETR_TREE finds all the promising contour lines and reconstructs a full hierarchy of nested contours.
        # the method cv2.CHAIN_APPROX_SIMPLE returns only the endpoints that are necessary for drawing the contour line.
        #Contours in OpenCV Contours are the lines or curves that connect all the points that lie on the boundary of the object.
        
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)#Cv2. ContourArea Method (InputArray, Boolean) Calculates the contour area
            x,y,w,h = cv2.boundingRect(max_cnt)#The cv2.boundingRect() function of OpenCV is used to draw an approximate rectangle around the binary image.
            # This function is used mainly to highlight the region of interest after obtaining contours from an image.
            
            cv2.rectangle(frame1, (x+x1, y+y1), (x+w+x1, y+h+y1), (0,255,0), 2)
            #v2.rectangle(image, start_point, end_point, color, thickness)
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)

        else:
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)
            #used to give a string up of an image
            #when we use cv2.FONT_HERSHEY_SIMPLEX” increase contrast cv2 color to black and white cv2

        cv2.rectangle(frame1, (x1,y1), (x2, y2), (0,0,255), 1)
        cv2.imshow("esc. to exit", frame1)

        if cv2.waitKey(1) == 27:
            cap.release()#closes video file
            cv2.destroyAllWindows()
            break
 