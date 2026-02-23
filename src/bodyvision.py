import cv2
import mediapipe as mp
import numpy as np
 
# 초기화
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
 
cap = cv2.VideoCapture(0)
 
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
 
    # CLAHE 조명 보정
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b_chan = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    frame_preprocessed = cv2.merge((l, a, b_chan))
    frame_preprocessed = cv2.cvtColor(frame_preprocessed,
                                      cv2.COLOR_LAB2BGR)
 
    # Pose 처리
    img_rgb = cv2.cvtColor(frame_preprocessed,
                           cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)
 
    if results.pose_landmarks:
 
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )
 
        lm = results.pose_landmarks.landmark
 
        # 어깨 거리 계산
        l_sh = lm[mp_pose.PoseLandmark.LEFT_SHOULDER]
        r_sh = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]
 
        dist = np.sqrt(
            (l_sh.x - r_sh.x)**2 +
            (l_sh.y - r_sh.y)**2
        )
 
        cv2.putText(frame,
                    f"Shoulder Dist: {round(dist, 2)}",
                    (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)
 
        # 🔥 추가: 발 감지 체크
        l_ankle = lm[mp_pose.PoseLandmark.LEFT_ANKLE]
        r_ankle = lm[mp_pose.PoseLandmark.RIGHT_ANKLE]
 
        if l_ankle.visibility < 0.5 or r_ankle.visibility < 0.5:
            cv2.putText(frame,
                        "Move Back - Show Full Body",
                        (30, 70),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 3)
 
    cv2.imshow('AI Vision Lab Test', frame)
 
    if cv2.waitKey(5) & 0xFF == 27:
        break
 
cap.release()
cv2.destroyAllWindows()