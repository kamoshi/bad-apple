import time
import cv2


G_SCALE = " .:-=+*#%@"
SHAPE = (80, 30)
FRAME_RATE = 30


def display_ascii(ascii_img) -> None:
    concat = "\033[6;1H"
    for row in ascii_img:
        concat += "".join(row) + "\n"
    print(concat)


def main():
    video = cv2.VideoCapture('bad_apple.mp4')
    prev_t = 0
    while video.isOpened():
        ret, frame = video.read()

        if cv2.waitKey(1) and 0xFF == ord('q') or not ret:
            video.release()
            cv2.destroyAllWindows()
            break

        resized = cv2.resize(frame, SHAPE, interpolation=cv2.INTER_AREA)
        grayscale = (resized.mean(axis=-1) * 9 / 255).astype('uint8')
        ascii_img = map(lambda row: map(lambda pixel: G_SCALE[pixel], row), grayscale)

        while time.time() - prev_t < 1. / FRAME_RATE:
            pass
        prev_t = time.time()

        display_ascii(ascii_img)
        cv2.imshow('frame', frame)


if __name__ == '__main__':
    main()
