import cv2
import mediapipe as mp
import pygame
import random
import time

# تنظیمات Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hand Shooting Game")

# رنگ‌ها و فونت
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
font = pygame.font.SysFont(None, 35)

# بارگذاری تصاویر
background_img = pygame.image.load('background.png')  # تصویر پس‌زمینه
gun_img = pygame.image.load('gun.png')  # تصویر تفنگ
enemy_img = pygame.image.load('enemy.png')  # تصویر دشمن
bullet_img = pygame.image.load('bullet.png')  # تصویر گلوله

# تنظیمات تصاویر
gun_width, gun_height = gun_img.get_width(), gun_img.get_height()
bullet_width, bullet_height = bullet_img.get_width(), bullet_img.get_height()
enemy_width, enemy_height = enemy_img.get_width(), enemy_img.get_height()

# تنظیمات بازی
score = 0
game_duration = 30  # مدت زمان بازی به ثانیه
bullets = []
enemies = []

# تنظیمات برای MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# راه‌اندازی دوربین
cap = cv2.VideoCapture(0)

# موقعیت‌ها
gun_x, gun_y = screen_width // 2, screen_height - gun_height - 10

# زمان شروع بازی
start_time = time.time()

def create_enemy():
    x = random.randint(0, screen_width - enemy_width)
    y = -enemy_height
    return [x, y]

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

# حلقه بازی
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    running = True
    while running:
        success, image = cap.read()
        if not success:
            print("نمی‌توان تصویر را از دوربین دریافت کرد.")
            continue

        # معکوس کردن تصویر و تبدیل به RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        # رسم تشخیص‌های دست
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # گرفتن موقعیت انگشتان دست
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # محاسبه فاصله بین سر انگشت شست و اشاره
                distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

                # گرفتن موقعیت دست برای حرکت دادن تفنگ
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                gun_x = int(wrist.x * screen_width)

                # بررسی شلیک گلوله
                if distance < 0.05:  # اگر دست مشت شده است
                    bullets.append([gun_x + gun_width // 2, gun_y])

        # به روزرسانی صفحه بازی
        screen.blit(background_img, (0, 0))  # رسم پس‌زمینه

        # رسم تفنگ
        screen.blit(gun_img, (gun_x, gun_y))

        # رسم و حرکت گلوله‌ها
        for bullet in bullets:
            bullet[1] -= 5  # حرکت گلوله به سمت بالا
            screen.blit(bullet_img, (bullet[0], bullet[1]))
            if bullet[1] < 0:
                bullets.remove(bullet)

        # تولید دشمنان
        if random.randint(1, 50) == 1:  # هر از گاهی یک دشمن اضافه می‌شود
            enemies.append(create_enemy())

        # حرکت دشمنان
        for enemy in enemies:
            enemy[1] += 3  # حرکت دشمن به سمت پایین
            screen.blit(enemy_img, (enemy[0], enemy[1]))
            if enemy[1] > screen_height:
                enemies.remove(enemy)

        # بررسی برخورد گلوله با دشمن
        for bullet in bullets:
            for enemy in enemies:
                if bullet[0] in range(enemy[0], enemy[0] + enemy_width) and bullet[1] in range(enemy[1], enemy[1] + enemy_height):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1

        # نمایش امتیاز و زمان باقی‌مانده
        elapsed_time = time.time() - start_time
        remaining_time = max(0, game_duration - int(elapsed_time))
        draw_text(f'Score: {score}', font, black, screen, 10, 10)
        draw_text(f'Time: {remaining_time}s', font, black, screen, 10, 50)

        # بررسی پایان بازی
        if remaining_time == 0:
            running = False

        # به روزرسانی صفحه
        pygame.display.update()

        # بررسی رویدادهای Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

cap.release()
cv2.destroyAllWindows()
pygame.quit()

print(f"بازی تمام شد! امتیاز نهایی: {score}")
