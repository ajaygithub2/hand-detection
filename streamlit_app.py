import streamlit as st
import cv2
st.write("cv2 imported")
import mediapipe as mp
st.write("mediapipe imported")

# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# mp_drawing_styles = mp.solutions.drawing_styles
# color = (0,0,0) #RGB
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 0.5
# thickness = 1
# line_type = cv2.LINE_AA
# hands = mp_hands.Hands(
#         model_complexity=1,
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5,
#         static_image_mode= False
#         )
    
# cap = cv2.VideoCapture(0)
# run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])
# def main():
#     # Add your detect_hands function here
#     st.write("Check the box to start the model...")
#     while run:
#         ret, frame = cap.read()
#         frame.flags.writeable = False
#         frame = cv2.cvtColor(cv2.flip(frame,1), cv2.COLOR_BGR2RGB)

#         results = hands.process(frame)
#         frame.flags.writeable = True

#         cv2.rectangle(frame, (0,0),(640, 40), (0, 255, 0), -1)
#         cv2.putText(frame, "Hand:                                 Prob:",(12,25),
#                         fontFace=font, fontScale=font_scale, color=color, thickness=thickness, lineType=line_type)

#         landmarks = results.multi_hand_world_landmarks
#         try:
#             if landmarks is None:
#                 side = "No Hands in frame"
#                 surity = "Pretty sure"
#             elif len(landmarks) == 1:
#                 surity = f"{float(str(results.multi_handedness[0].classification[0])[16:20]) * 100}%"
#                 if "Left" in str(results.multi_handedness[0].classification[0]):
#                     side = "Left"
#                 elif "Right" in str(results.multi_handedness[0].classification[0]):
#                     side = "Right"
#             elif len(landmarks) > 1 :
#                 surity = f"{(float(str(results.multi_handedness[0].classification[0])[16:20])*50) + (float(str(results.multi_handedness[1].classification[0])[16:20])*50)}%"
#                 side = "Both"
#             cv2.putText(frame, side,
#                         (70,25),
#                         #tuple(np.multiply(left_wrist,[640,480]).astype(int)),
#                         fontFace=font, fontScale=font_scale, color=color, thickness=thickness, lineType=line_type)
#             cv2.putText(frame, f"{surity}",
#                         (380,25),
#                         #tuple(np.multiply(left_wrist,[640,480]).astype(int)),
#                         fontFace=font, fontScale=font_scale, color=color, thickness=thickness, lineType=line_type)
#         except:
#             pass

#         if results.multi_hand_landmarks:
#                 for hand_landmarks in results.multi_hand_landmarks:
#                     mp_drawing.draw_landmarks(
#                         frame,
#                         hand_landmarks,
#                         mp_hands.HAND_CONNECTIONS,
#                         mp_drawing_styles.get_default_hand_landmarks_style(),
#                         mp_drawing_styles.get_default_hand_connections_style())

#         FRAME_WINDOW.image(frame)

# if __name__ == "__main__":
#     main()
