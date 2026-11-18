# 宿舍温湿度监测系统

ESP32 + DHT11 + OLED，实时监测温湿度，超阈值邮件告警。

## 功能
- 每 2 秒采集一次温湿度
- OLED 本地显示
- 数据经串口传到电脑，存为 CSV
- 温度超过 30℃ 自动发邮件（5 分钟限流）

## 硬件
| 元件 | 型号 |
|---|---|
| 主控 | ESP32-WROOM-32 |
| 传感器 | DHT11 |
| 显示屏 | 0.96" OLED (SSD1306, I2C) |

## 接线
| 元件 | 引脚 | 接到 ESP32 |
|---|---|---|
| DHT11 | VCC | 3V3 |
| DHT11 | DATA | GPIO4 |
| DHT11 | GND | GND |
| OLED | VDD | 3V3 |
| OLED | GND | GND |
| OLED | SDA | GPIO21 |
| OLED | SCL | GPIO22 |

## 软件
- Arduino IDE 2.3.10，esp32 支持包
- 库：DHT sensor library、Adafruit SSD1306、Adafruit GFX
- Python 3.14 + pyserial

## 运行
1. 上传 `dorm_monitor.ino` 到 ESP32
2. 改 `read_serial.py` 里的 COM 口
3. 运行脚本，数据写入 `data.csv`

## 踩坑记录
1. 卖家配的 Micro USB 线是**充电线**（无数据线芯），电脑识别不到板子 → 换数据线解决
2. 板子 USB 转串口芯片是 **FTDI FT232RQ**，不是 CH340/CP2102
3. DHT11 模块丝印不全，针脚顺序为 S / + / -
4. 串口独占：跑 Python 前必须关掉 Arduino 串口监视器
5. 启动时需 `reset_input_buffer()` 清空积压数据

## 后续计划
- WiFi/MQTT 上云，摆脱 USB 线
- 历史曲线网页
- ## 测试结果
连续运行 24 小时，采集 51,194 条数据，无异常断连。
（期间的 4 次中断均为调试时手动停止）
