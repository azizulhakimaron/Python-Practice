import speedtest as spd
test=spd.Speedtest()
x=test.download()
y=test.upload()
print("Download:",x)
print("Upload:",y)