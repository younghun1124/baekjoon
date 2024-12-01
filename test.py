import numpy as np

# 사용자 초기값 설정
m = 80.0        # 사람의 질량 (kg)
m_bicycle = 1.0  # 자전거의 질량 (kg)
M_total = m + m_bicycle  # 총 질량 (kg)
h = 0.05           # 페달의 수직 낙하 높이 (m)
C_r = 0.015        # 구름저항 계수
rho = 1.2          # 공기 밀도 (kg/m^3)
C_d = 1.0          # 공기저항 계수
A = 0.5            # 단면적 (m^2)
g = 9.8            # 중력 가속도 (m/s^2)
gear_ratio = 5.5   # 기어비
r_wheel = 0.03     # 바퀴 반지름 (m)
r_pedal = 0.03   # 페달 암의 길이 (m)

# 1. 페달의 회전 각도 계산
cos_theta = 1 - h / r_pedal
theta_pedal = np.arccos(cos_theta)  # 라디안 단위

# 2. 자전거의 전진 거리 계산
theta_wheel = theta_pedal * gear_ratio         # 뒷바퀴의 회전 각도
d = r_wheel * theta_wheel                      # 자전거의 전진 거리 (m)

# 3. 위치 에너지 계산
E_potential = m * g * h                        # 위치 에너지 (J)

# 4. 구름 저항에 의한 에너지 손실
F_roll = C_r * M_total * g                     # 구름 저항력 (N)
E_roll = F_roll * d                            # 구름 저항에 의한 에너지 손실 (J)

# 5. 공기 저항에 의한 에너지 손실
# 속도를 모르는 상태이므로 일단 식을 설정합니다.
# 총 운동 에너지 방정식:
# E_potential = 0.5 * M_total * v**2 + E_roll + 0.5 * C_d * rho * A * v**2 * d

# 공기 저항에 의한 에너지 손실 계수:
E_air_coeff = 0.5 * C_d * rho * A * d

# 운동 에너지 방정식 정리:
# E_potential = (0.5 * M_total + E_air_coeff) * v**2 + E_roll

# v^2에 대한 방정식:
coeff_v2 = 0.5 * M_total + E_air_coeff
constant = E_potential - E_roll

v_squared = constant / coeff_v2
if v_squared > 0:
    v = np.sqrt(v_squared)
else:
    v = 0.0

# 6. 페달이 내려가는 시간 계산
# 관성 모멘트를 무시하고 단순화하여 계산합니다.

# 페달의 이동 거리 (호의 길이):
s_pedal = r_pedal * theta_pedal  # m

# 페달의 평균 속도를 자전거의 속도와 연관시켜 계산
# 기어비를 고려하여 페달 속도 계산
v_pedal = v / gear_ratio  # 페달의 선형 속도 (m/s)

# 페달 내려가는 시간 계산
t_pedal = s_pedal / v_pedal  # 페달 내려가는 시간 (s)

# 결과 출력
print(f"자전거의 최종 속력: {v:.2f} m/s")
print(f"페달이 최상단에서 최하단까지 내려가는 시간: {t_pedal:.2f} 초")