import cv2
import mediapipe as mp

# 1. MediaPipe 설정 (포즈 추출 모델)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def analyze_body_ratio(image_path):
    # 2. 이미지 로드
    image = cv2.imread(image_path)
    if image is None:
        print("이미지를 찾을 수 없습니다.")
        return

    # 3. 신체 관절 추출
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        print("신체 좌표 추출 성공!")
        # 여기에 체형 판정 알고리즘(수치 기반 Ratio)이 들어갈 예정입니다.
        
        # 샘플: 어깨 좌표 출력 (Landmark 11, 12)
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        print(f"왼쪽 어깨: {left_shoulder.x, left_shoulder.y}")
    else:
        print("신체 감지에 실패했습니다.")

# 실행 예시 (나중에 실제 사진 경로로 변경)
# analyze_body_ratio('data/sample_body.jpg')