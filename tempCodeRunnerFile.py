import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows인 경우
# plt.rcParams['font.family'] = 'AppleGothic'  # macOS인 경우
# plt.rcParams['font.family'] = 'NanumGothic'  # Linux(Ubuntu)인 경우

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False


# 사용자 초기값 설정
m = 80.0          # 사람의 질량 (kg)
m_device = 1.0    # 장치의 질량 (kg)
M_total = m + m_device  # 총 질량 (kg)
h = 0.05          # 수직 이동 거리 (m)
C_r = 0.015       # 구름저항 계수
rho = 1.2         # 공기 밀도 (kg/m^3)
C_d = 1.0         # 공기저항 계수
A = 0.5           # 단면적 (m^2)
g = 9.8           # 중력 가속도 (m/s^2)
gear_ratio = 5.0  # 기어비 (5:1)
r_wheel = 0.03    # 바퀴 반지름 (m)
r_pedal = 0.03    # 페달 암의 길이 (m)
I_crank = m * r_pedal**2  # 크랭크의 관성 모멘트 (kg·m^2)

# 시간 설정
dt = 0.001         # 시간 간격 (s)
t_total = 2.0      # 총 시뮬레이션 시간 (s)
time_steps = int(t_total / dt)
t = np.linspace(0, t_total, time_steps)

# 초기값 설정
v = np.zeros(time_steps)             # 속도 배열
x = np.zeros(time_steps)             # 위치 배열
theta_pedal = np.zeros(time_steps)   # 페달 각도 배열
omega_pedal = np.zeros(time_steps)   # 페달 각속도 배열

# 페달 초기 각도 설정 (0에서 시작)
theta_pedal[0] = 0.0 # 라디안 단위

# 최대 페달 각도 (90도)
theta_pedal_max = np.pi / 2  # 90도

# 시뮬레이션 시작
for i in range(1, time_steps):
    if theta_pedal[i-1] < theta_pedal_max:
        # 페달을 밟는 동안
        # 현재 각도에서 토크 계산
        tau_pedal = m * g * r_pedal * np.sin(theta_pedal[i-1])
        # 각가속도 계산
        alpha = tau_pedal / I_crank
        # 각속도 업데이트
        omega_pedal[i] = omega_pedal[i-1] + alpha * dt
        # 각도 업데이트
        theta_pedal[i] = theta_pedal[i-1] + omega_pedal[i] * dt
        if theta_pedal[i] > theta_pedal_max:
            theta_pedal[i] = theta_pedal_max
            omega_pedal[i] = 0.0
        # 뒷바퀴로 전달된 토크 (기어비 고려)
        tau_wheel = tau_pedal / gear_ratio
        # 뒷바퀴에 의한 추진력
        F_drive = tau_wheel / r_wheel
    else:
        # 페달 밟기가 끝난 후
        omega_pedal[i] = 0.0
        theta_pedal[i] = theta_pedal_max
        F_drive = 0.0

    # 저항력 계산
    F_roll = C_r * M_total * g
    F_air = 0.5 * C_d * rho * A * v[i-1]**2
    F_total = F_roll + F_air

    # 가속도 계산
    a = (F_drive - F_total) / M_total

    # 속도 업데이트
    v[i] = v[i-1] + a * dt
    if v[i] < 0:
        v[i] = 0.0

    # 위치 업데이트
    x[i] = x[i-1] + v[i] * dt

# 최종 속도
v_final = v[-1]

# 페달 내려가는 시간 계산
t_pedal_index = np.argmax(theta_pedal >= theta_pedal_max)
t_pedal = t[t_pedal_index] if t_pedal_index > 0 else 0.0

# 결과 출력
print(f"장치의 최종 속력: {v_final:.2f} m/s")
print(f"페달이 최상단에서 최하단까지 내려가는 시간: {t_pedal:.2f} 초")

# 그래프 그리기
plt.figure(figsize=(12,6))

# 속도 그래프 그리기
plt.subplot(2,1,1)
plt.plot(t, v)
plt.xlabel('시간 (s)')
plt.ylabel('속도 (m/s)')
plt.title('시간에 따른 속도 변화')
plt.grid()

# 페달 각도 그래프 그리기
plt.subplot(2,1,2)
plt.plot(t, theta_pedal)
plt.xlabel('시간 (s)')
plt.ylabel('페달 각도 (rad)')
plt.title('시간에 따른 페달 각도 변화')
plt.grid()

plt.tight_layout()
plt.show()
