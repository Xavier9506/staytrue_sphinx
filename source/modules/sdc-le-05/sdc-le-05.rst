SDC-LE-05
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AB5605B核心，蓝牙双模设计，主打音频功能，支持FM接收、SD卡音频播放，适配带音频输出的消费电子。

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: sdc-le-05/images/sdc-le-05-img1.png
         :width: 200
         :alt: SDC-LE-05 模组正面图
     - .. image:: sdc-le-05/images/sdc-le-05-img2.png
         :width: 200
         :alt: SDC-LE-05 模组反面图

.. image:: sdc-le-05/images/sdc-le-05-img3.png
   :width: 300
   :align: center
   :alt: SDC-LE-05 模组尺寸图

核心性能
~~~~~~~~~~
- 处理器：32位RISC-V CPU，125MHz主频
- 存储：4Mbit Flash + 128KB RAM
- 蓝牙射频：BT5.4双模（QDID:215269），发射6dBm，接收-90.5dBm@EDR
- 音频功能：16bit立体声、软件EQ均衡器、1段DRC动态范围压缩，1路MIC输入，左右声道差分输出
- 扩展功能：8引脚引出,FM接收（76~108MHz）、SD卡音频播放、UART串口、MUTE静音控制
- 工作温度：-40℃~85℃
- 封装尺寸: 邮票孔封装，半孔间距1.27mm，尺寸18.1mm×20mm

关键引脚定义
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 关键引脚定义
   :widths: 15 20 45 20
   :header-rows: 1

   * - 引脚
     - 信号名
     - 描述
     - 引脚类型
   * - VBAT
     - VBAT
     - 电源正极，2~4.5V（典型3.3V）
     - P（电源）
   * - GND
     - GND
     - 模块地
     - P（电源）
   * - PE6
     - UART_RX
     - 串口RX数据接收端
     - I（输入）
   * - PE7
     - UART_TX
     - 串口TX数据发送端
     - O（输出）
   * - PE0
     - MUTE
     - 静音控制引脚,低电平时静音
     - O（输出）
   * - DACL
     - M DACL
     - 左声道音频输出
     - O（输出）
   * - DACR
     - M DACR
     - 右声道音频输出
     - O（输出）

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
     - 8~32
     - mA
   * - Iol
     - 灌电流
     - 8~32
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
  - 下载链接：`CE-RED证书 <../certificates/sdc-le-05-ce-red.pdf>`_
- **FCC**：符合美国联邦通信委员会标准，通过FCC认证
  - 下载链接：`FCC证书 <../certificates/sdc-le-05-fcc.pdf>`_
- **SRRC**：符合中国无线电管理委员会标准，通过SRRC认证
  - 下载链接：`SRRC证书 <../certificates/sdc-le-05-srrc.pdf>`_
- **BQB**：符合蓝牙技术联盟标准，通过BQB认证（QDID:215269）
  - 下载链接：`BQB证书 <../certificates/sdc-le-05-bqb.pdf>`_