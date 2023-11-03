import cv2
import mediapipe as mp
import numpy as np
import keyboard
import time

max_num_hands = 1

gesture = {
    0:'a', 1:'b', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
    9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p',
    16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w',
    23:'x', 24:'y', 25:'z', 26:'space', 27:'backspace'
}

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands = max_num_hands
    min_detection_confidence = 0.5
    min_tracking_confidence = 0.5
)

            