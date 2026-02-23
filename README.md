# stylefit
MS ai9기 3팀 프로젝트
👔 StyleFit: AI 기반 남성 퍼스널 스타일링 분석 엔진
"데이터로 찾는 나만의 핏, 사진 한 장으로 완성되는 스타일링" > 2040 남성을 위한 AI 체형 분석 및 퍼스널 컬러 진단 솔루션입니다.

📝 프로젝트 개요
목표: 사용자의 전신 사진을 분석하여 정확한 **신체 수치(골격)**와 퍼스널 컬러를 도출하고, 이를 바탕으로 최적의 의류를 추천하는 핵심 엔진을 개발합니다.

핵심 가치: 비대면으로 이루어지는 정밀한 체형 진단과 과학적 근거에 기반한 패션 큐레이션 서비스를 제공합니다.

🛠 기술 스택 (Tech Stack)
이번 1차 프로젝트에서는 Azure 머신러닝 로드맵에 명시된 핵심 기술들을 활용합니다.

AI & Machine Learning: Azure Custom Vision, Machine Learning Studio, PyTorch, sklearn

Computer Vision: MediaPipe (Pose Estimation), OpenCV

Language & Framework: Python, Streamlit

Collaboration: GitHub

🏗 시스템 아키텍처 (System Architecture)
Input: 사용자의 전신/얼굴 사진 및 기본 정보(키) 입력 (Streamlit)

Preprocessing: 조명 및 화이트 밸런스 보정 (OpenCV)

Analysis:

골격: 관절 좌표 추출(MediaPipe) 및 신체 비율 계산

컬러: 피부색 추출 및 계절별 톤 분류 (Azure Custom Vision)

Matching: 분석 데이터 기반 의류 DB 매칭 알고리즘 (sklearn)

Output: 개인화된 스타일 분석 리포트 및 코디 추천

👥 팀원 역할 (R&R)
PM / AI Engineer (본인): 전체 시스템 설계(Architecture), Streamlit UI 구현 및 모듈 통합

AI Vision (A님): MediaPipe 활용 신체 관절 좌표 추출 및 수치화 알고리즘 개발

AI Vision (B님): OpenCV 기반 이미지 전처리 및 피부 영역 분석 로직 구현

ML & Data (C님): Azure Custom Vision 학습 및 Machine Learning Studio 배포 관리

Data Engineer (D님): 학습용 체형/컬러 이미지 데이터셋 구축 및 의류 DB 크롤링

Backend (E님): 체형-의류 데이터 매칭 추천 엔진 개발 (sklearn)

📅 1주차 주요 마일스톤
[ ] GitHub 협업 환경 구축 및 파트별 기술 테스트

[ ] 분석용 기초 데이터셋(체형/컬러) 확보

[ ] MediaPipe 및 OpenCV 기초 프로토타입 코드 작성
