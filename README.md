# kuinasupport
kuinasupportのデバイスを監視、データ収集するためのコード類

## UM24C：ラズパイのbluetooth設定方法
bluetoothctlを使ってペアリングをする
(アドレスは任意)
```
sudo bluetoothctl
scan on 
pair AA:AA:AA:AA:AA:AA
paired-devices
```

その後、rfcommで接続
```
sudo rfcomm bind 0 AA:AA:AA:AA:AA:AA
```