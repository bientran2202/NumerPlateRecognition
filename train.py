from multiprocessing import Process
import time
from ultralytics import YOLO

start = time.perf_counter()


def do_something(time_for_sleep):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
    print('Done Sleeping...')


p1 = Process(target=do_something, args=[1])
p2 = Process(target=do_something, args=[2])


if __name__ == '__main__':
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2 )} second(s)')


# Create a new YOLO model from scratch
# model = YOLO('../Yolo-Weights/yolov8l.pt')
#
# # Train the model using the 'data.yaml' dataset for 1 epoch
# results = model.train(data='data.yaml', epochs=1, imgsz=640, device=0)

# # Evaluate the model's performance on teh validation set
# results = model.val()
#
# # Perform object detection on a imange using the model
# results = model('https://oto360.net/images/bai-viet/a_164337.jpg')
