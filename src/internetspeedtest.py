import speedtest as spd # speedtest-cli
test=spd.Speedtest()
x=test.download()
y=test.upload()
print("Download:",x)
print("Upload:",y)
