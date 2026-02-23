# 👔 StyleFit: AI 기반 남성 퍼스널 스타일링 분석 엔진
> **"데이터로 증명하는 나만의 핏, 사진 한 장으로 완성되는 정밀 큐레이션"**
>
> 
> 오프라인 전문가의 안목을 디지털 데이터로 이식하여, 모든 남성에게 '실패 없는 스타일'을 제공합니다.

---

### 💡 Project Background & Intent

#### **1. 패션 트렌드의 전략적 요충지, 대한민국**
* 대한민국은 외모와 스타일에 대한 안목이 매우 높아 전 세계 패션 트렌드를 선도하는 핵심 국가입니다.
* 이러한 시장성을 바탕으로 수많은 글로벌 어패럴 브랜드들은 한국인의 체형과 취향을 정밀 분석하기 위해 별도의 한국 지사를 운영하며 전용 라인을 생산하고 있습니다.

#### **2. 오프라인 컨설팅의 한계와 기술적 기회**
* 최근 퍼스널 컬러 및 골격 진단은 스타일링에 실질적인 도움을 주는 것으로 입증되었으나, 전문가 대면의 번거로움과 높은 비용이라는 장벽이 존재합니다.
* 특히 진단 이후 본인에게 어울리는 옷을 직접 찾아다녀야 하는 **'실행 단계의 막막함'**은 사용자가 다시 무난한 스타일로 회귀하게 만드는 결정적인 페인 포인트(Pain Point)입니다.

#### **3. 우리의 솔루션: 퍼스널 코디네이터 엔진**
* **StyleFit**은 이러한 오프라인 컨설팅의 강점을 AI 기술로 자동화합니다.
* 정밀한 이미지 분석을 통해 '안 입어보고도 인생 핏을 찾는' 과학적 기준을 정립하고, 단순한 추천을 넘어 사용자의 신체 데이터를 가장 완벽하게 이해하는 디지털 코디네이터를 지향합니다.

---

### 🛠 Tech Stack

**AI & Computer Vision**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

**Service & Infrastructure**
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

---

### 📌 Core Engine Logic

**1. 정밀 데이터 추출 (Data Extraction)**
* 가이드라인 기반 이미지 촬영을 통해 오차 없는 신체 수치(골격 좌표) 및 피부톤 데이터 도출
* OpenCV 화이트 밸런스 보정을 통한 환경 무관 데이터 신뢰성 확보

**2. 유형화 알고리즘 (Typology)**
* 기존 남성 5대 체형 이론을 수치(Ratio) 기반 판정 로직으로 구현
* 전문가 수준의 진단 결과를 디지털 태그 형태로 자동 생성

**3. 스마트 매칭 (Matching Algorithm)**
* 체형 보정 이론과 의류 실측 데이터를 결합한 큐레이션 로직
* '적정 여유분(Ease)' 계산을 통한 과학적 사이즈 및 스타일 추천

---

### 👥 Team Role (R&R)

| 역할 | 담당자 | 핵심 업무 |
| :--- | :--- | :--- |
| **PM / AI Eng.** | **택근,나영** | 전체 시스템 설계 및 데이터 파이프라인 규격화, Streamlit UI 구현 |
| **Vision (Body)** | **지현,택근** | MediaPipe 활용 신체 관절 좌표 추출 및 실제 비율 수치화 |
| **Vision (Color)** | **현승,소현님** | OpenCV 기반 이미지 전처리 및 피부 영역(ROI) 분석 |
| **ML & Cloud** | **C님** | Azure Custom Vision 학습 및 배포, ML Studio 모델 관리 |
| **Data Eng.** | **D님** | 학습용 데이터셋 구축 및 브랜드별 의류 실측 데이터베이스 설계 |
| **Algorithm** | **E님** | 체형-의류 데이터 매칭 엔진 및 TPO 기반 추천 로직 개발 |

---

### 📅 Milestone (1st Week)
- [ ] GitHub 레포지토리 환경 설정 및 공통 폴더 구조 생성
- [ ] 남성 5대 체형 및 사계절 컬러 분석을 위한 기초 데이터 확보
- [ ] MediaPipe와 OpenCV를 활용한 데이터 추출 프로토타입 개발


