import cv2

class Renderer(object):
    def __init__(s):
        s.current_frame = None
        s.width = 1000
        s.height = 800


    def render_frame(s,frame):
        s.current_frame = frame
        if frame is not None:
            ret, jpeg = cv2.imencode('.jpg', frame)
        else:
            frame = n.random.randint(0, 40, (s.height, s.width), 'uint8')

            font = cv2.FONT_HERSHEY_SIMPLEX
            text = 'No Available Input for Now'

            # get boundary of this text
            textsize = cv2.getTextSize(text, font, 1, 2)[0]

            textX = (frame.shape[1] - textsize[0]) / 2
            textY = (frame.shape[0] + textsize[1]) / 2

            cv2.putText(frame, text, (int(textX), int(textY)), font, 1, (255, 255, 255), 2)

            # frame = cv2.putText(frame,,(int(s.height//2.4),int(s.width//2.4)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
            ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()