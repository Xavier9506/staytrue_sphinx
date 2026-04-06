SDC-LE-01
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
专为跑步机、单车、划船机等运动设备设计，板载天线+邮票孔封装，支持第三方APP直连。

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: images/sdc-le-01-img1.png
         :width: 300
         :alt: SDC-LE-01 模组正面图
     - .. image:: images/sdc-le-01-img2.png
         :width: 300
         :alt: SDC-LE-01 模组反面图

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: images/sdc-le-01-img3.png
         :width: 300
         :alt: SDC-LE-01 模组引脚图
     - .. image:: images/sdc-le-01-img4.png
         :width: 300
         :alt: SDC-LE-01 模组尺寸图

核心性能
~~~~~~~~~~
- 处理器：32位高性能RISC核心，16MHz时钟
- 存储：512KB Flash + 40KB SRAM
- 蓝牙射频：2.4GHz BLE5.0，-97dBm接收灵敏度，输出功率-20~+7dBm可编程
- 认证：SRRC、FCC、CE-RED、BQB、NCC
- 工作温度：-40℃ ~ +105℃
- 封装尺寸: 邮票孔封装，半孔间距1.27mm，尺寸13mm×19mm

关键引脚定义
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 关键引脚定义
   :widths: 15 20 45 20
   :header-rows: 1

   * - 引脚
     - 信号名
     - 描述
     - 引脚类型
   * - GND
     - GND
     - 模块地
     - P（电源）
   * - RST
     - RST
     - 复位脚，0=复位/1=正常工作，完成复位后应设置为悬浮输入
     - I（输入）
   * - PD2
     - UART_RX
     - 串口RX数据接收端
     - I（输入）
   * - PD3
     - UART_TX
     - 串口TX数据发送端
     - O（输出）
   * - 3V
     - VCC
     - 电源正极，2~3.6V（典型3.3V）
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
   * - VDD
     - 稳态电源电压
     - 2 ~ 3.6
     - V
   * - Tamb
     - 工作温度
     - -40~+105
     - ℃
   * - Tstg
     - 储藏温度
     - -40~+150
     - ℃
   * - Ground
     - 地
     - -0.3~0.3
     - V
   * - Voh
     - 数字输出高电平
     - VDD-0.3 ~ VDD+0.3
     - V
   * - Vol
     - 数字输出低电平
     - <0.4
     - V
   * - Ioh
     - 拉电流
     - 15
     - mA
   * - Iol
     - 灌电流
     - 11
     - mA
   * - Vih
     - 数字输入高电平
     - ≥0.7×VDD
     - V
   * - ViL
     - 数字输入低电平
     - ≤0.3×VDD
     - V

认证证书
~~~~~~~~~~
- **CE-RED**：符合欧盟无线电设备指令，通过CE认证
  - 下载链接：`CE-RED证书 <../certificates/sdc-le-01-ce-red.pdf>`_
- **FCC**：符合美国联邦通信委员会标准，通过FCC认证
  - 下载链接：`FCC证书 <../certificates/sdc-le-01-fcc.pdf>`_
- **NCC**：符合台湾通讯传播委员会标准，通过NCC认证
  - 下载链接：`NCC证书 <../certificates/sdc-le-01-ncc.pdf>`_
- **SRRC**：符合中国无线电管理委员会标准，通过SRRC认证
  - 下载链接：`SRRC证书 <../certificates/sdc-le-01-srrc.pdf>`_
- **BQB**：符合蓝牙技术联盟标准，通过BQB认证
  - 下载链接：`BQB证书 <../certificates/sdc-le-01-bqb.pdf>`_