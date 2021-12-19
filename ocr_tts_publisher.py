import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile # 퍼블리셔의 QoS 설정
from std_msgs.msg import String # 퍼블리시 메시지 타입

class OCR_TTS_Publisher(Node): # Node 클래스 상속

    def __init__(self):
        super().__init__('OCR_TTS_Publisher') # 노드 이름 지정
        qos_profile = QoSProfile(depth=10) # 퍼블리시할 데이터를 버퍼에 10개까지 저장
        self.tts_publisher = self.create_publisher(String, 'ocr_tts_message', qos_profile)
        self.timer = self.create_timer(1, self.publish_msg) # 콜백함수 : n초마다 지정한 콜백함수 실행
        self.count = 0

    def publish_msg(self):
        msg = String() # 퍼블리시할 메시지
        msg.data = '송민영'.format(self.count) # 메시지 저장
        self.tts_publisher.publish(msg) # 메시지 퍼블리시
        self.get_logger().info('Published message: {0}'.format(msg.data)) # 콘솔창에 출력 (==print함수)

def main(args=None):
    rclpy.init(args=args) # 초기화
    node = TTS_Publisher()
    try:
        node.get_logger().info("spin될까?")
        rclpy.spin_once(node) # 콜백함수 실행
        node.get_logger().info("spin된다!!")

    except KeyboardInterrupt: # 'Ctrl+c'와 같은 인터럽트 시그널 예외 상황
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node() # 노드 소멸
        rclpy.shutdown() # 함수 종료

if __name__ == '__main__':
    main()

