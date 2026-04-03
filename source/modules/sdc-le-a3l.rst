SDC-LE-A3L
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SDC-LE-A3升级款，双安装方式（贴片+插针），适配多形态产品，21引脚高扩展，适配多外设场景。

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: sdc-le-a3l/images/sdc-le-a3l-img1.png
         :width: 300
         :alt: SDC-LE-A3L 模组正面图
     - .. image:: sdc-le-a3l/images/sdc-le-a3l-img2.png
         :width: 300
         :alt: SDC-LE-A3L 模组反面图

.. image:: sdc-le-a3l/images/sdc-le-a3l-img3.png
   :width: 300 
   :align: center    
   :alt: SDC-LE-A3L 模组尺寸图模组引脚图

核心性能
~~~~~~~~~~
- 处理器：32位RISC-V CPU，主频最高120MHz
- 存储：4Mbit Flash + 64KB RAM + 8K cache
- 蓝牙射频：BLE5.4（QDID:222495），发射+9dBm，接收-94dBm@1M BLE
- 典型供电：2~4.5V（3.3V）
- 扩展功能：21引脚引出，支持UART/IIC/SPI、44按键矩阵扫描、Touch Key、LEDC幻彩灯驱动
- 特殊IO：2路高压IO（PA0/PA1），支持5V MCU通信
- 工作温度：-40℃~85℃
- 封装尺寸：21mm×25mm，采用贴片+插针双安装方式，半孔间距1.5mm

关键引脚定义
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 关键引脚定义
   :widths: 15 20 45 20
   :header-rows: 1

   * - 引脚
     - 信号名
     - 描述
     - 引脚类型
   * - PA7
     - L+
     - 蓝牙未连接时电平为高电平
     - O（输出）
   * - PB4
     - P
     - 心率传感器接口,悬浮输入，上升沿有效
     - I（输入）
   * - PB2
     - S
     - 速度传感器接口,悬浮输入，下降沿有效
     - I（输入）
   * - PB1
     - L-
     - 蓝牙未连接时电平为低电平
     - O（输出）
   * - PB1
     - UART_TX
     - 串口TX数据发送端
     - O（输出）
   * - PB0
     - UART_RX
     - 串口RX数据接收端
     - I（输入）
   * - GND
     - GND
     - 模块地
     - P（电源）
   * - VBAT
     - VBAT
     - 电源正极，2~4.5V（典型3.3V）
     - P（电源）

极限参数
~~~~~~~~~~

.. list-table:: 极限参数
   :widths: 20 30 20 10
   :header-rows: 1

   * - 参数
     - 说明
     - 范围
     - 单位
   * - VBAT
     - 稳态电源电压
     - 2 ~ 4.5
     - V
   * - VDDIO 
     - I/O 电源电压
     - 3.3
     - V
   * - Tamb
     - 工作温度
     - -40~+85
     - ℃
   * - Tstg
     - 储藏温度
     - -65~+150
     - ℃
   * - Ground
     - 地
     - -0.3~0.3
     - V
   * - Voh
     - 数字输出高电平
     - VDDIO-0.3 ~ VDDIO+0.3
     - V
   * - Vol
     - 数字输出低电平
     - <0.4
     - V
   * - Ioh
     - 拉电流
     - 6~24
     - mA
   * - Iol
     - 灌电流
     - 6~24
     - mA
   * - Vih
     - 数字输入高电平
     - ≥0.7×VDDIO
     - V
   * - ViL
     - 数字输入低电平
     - ≤0.3×VDDIO
     - V

认证证书
~~~~~~~~~~
- **CE-RED**：符合欧盟无线电设备指令，通过CE认证
  - 下载链接：`CE-RED证书 <../certificates/sdc-le-a3l-ce-red.pdf>`_
- **FCC**：符合美国联邦通信委员会标准，通过FCC认证
  - 下载链接：`FCC证书 <../certificates/sdc-le-a3l-fcc.pdf>`_
- **SRRC**：符合中国无线电管理委员会标准，通过SRRC认证
  - 下载链接：`SRRC证书 <../certificates/sdc-le-a3l-srrc.pdf>`_
- **BQB**：符合蓝牙技术联盟标准，通过BQB认证（QDID:222495）
  - 下载链接：`BQB证书 <../certificates/sdc-le-a3l-bqb.pdf>`_