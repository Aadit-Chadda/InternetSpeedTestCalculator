import speedtest

try:
  test = speedtest.Speedtest()
  print('Aadit... Your code is magic')
except:
  print('There was en error')

print("Loading SERVER")
test.get_servers()
print("Selecting Best SERVER")
best = test.get_best_server()
print("Performing Download Test")
download_result = test.download()
print("Performing Upload Test")
upload_test = test.upload()
ping_capture = test.results.ping

print()

print(f"Download speed: {download_result / 1024 /1024: .2f} Mbit/s")
print()
print(f"Upload speed: {upload_test / 1024 /1024: .2f} Mbit/s")
print()
print(f"Ping: {ping_capture: .2f} ms")

print()
print('#' * 30)
