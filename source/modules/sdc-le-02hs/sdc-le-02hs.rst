SDC-LE-02HS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AB5602B核心，蓝牙双模设计，主打音频功能，适配带音频输出的消费电子。采用贴片接口，支持FM接收和SD卡音频播放，支持3.0V~6V供电（典型5V），串口兼容3.3V/5V电平

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: images/sdc-le-02hs-img1.png
         :width: 200
         :alt: SDC-LE-02HS 模组正面图
     - .. image:: images/sdc-le-02hs-img2.png
         :width: 200
         :alt: SDC-LE-02HS 模组反面图
.. image:: images/sdc-le-02hS-img3.png
   :width: 300
   :align: center
   :alt: SDC-LE-02HS 模组尺寸图

核心性能
~~~~~~~~~~
- 处理器：32位RISC-V CPU，125MHz主频
- 存储：4Mbit Flash + 128KB RAM
- 蓝牙射频：BT5.4双模（QDID:215269），发射6dBm，接收-90.5dBm@EDR
- 音频功能：16bit立体声、软件EQ均衡器、1段DRC动态范围压缩，1路MIC输入，左右声道差分输出
- 扩展功能：UART串口、MUTE静音控制
- 典型供电：3.0V~6V供电（典型5V）
- 工作温度：-40℃~85℃
- 封装尺寸: ** mmx ** mm(贴片接口)


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
     - 3.0 ~ 6.0
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
  - 下载链接：`CE-RED证书 <certificates/sdc-le-02hs-ce-red.pdf>`_
- **FCC**：符合美国联邦通信委员会标准，通过FCC认证，认证中
- **SRRC**：符合中国无线电管理委员会标准，通过SRRC认证，认证中
- **BQB**：符合蓝牙技术联盟标准，通过BQB认证（QDID:215269/QDID:206297）