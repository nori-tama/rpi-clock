import time

def current_time_str():
    """現在時刻を HH:MM:SS 形式の文字列で返す。"""
    return time.strftime("%H:%M:%S")

def main():
    print("Simple RPi Clock (Ctrl+C to stop)")
    try:
        while True:
            print(current_time_str(), end="\r", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped")

if __name__ == "__main__":
    main()

