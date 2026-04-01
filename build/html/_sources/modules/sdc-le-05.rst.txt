SDC-LE-05
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AB5605B核心，蓝牙双模设计，主打音频功能，支持FM接收、SD卡音频播放，适配带音频输出的消费电子。

.. image:: ../images/sdc-le-05-img1.png
   :width: 300
   :align: center
   :alt: SDC-LE-05 模组实物图
   
.. image:: ../images/sdc-le-05-img2.png
   :width: 300
   :align: center
   :alt: SDC-LE-05 模组接线示意图

核心性能
~~~~~~~~~~
- 处理器：32位RISC-V CPU，125MHz主频
- 存储：4Mbit Flash + 128KB RAM
- 蓝牙射频：BT5.4双模（QDID:215269），发射6dBm，接收-90.5dBm@EDR(2M带宽)
- 音频功能：16bit立体声、软件EQ均衡器、1段DRC动态范围压缩，1路MIC输入，左右声道差分输出
- 扩展功能：FM接收（76~108MHz）、SD卡音频播放、UART串口、MUTE静音控制
- 封装：18引脚引出，支持差分/单端音频输出
- 温宽：工业级，工作-40℃~85℃，存储-65℃~150℃

核心电气参数
~~~~~~~~~~~~~~~~

.. list-table:: 核心电气参数
   :widths: 25 15 15 15 15
   :header-rows: 1

   * - 名称
     - 最小值
     - 典型值
     - 最大值
     - 单位
   * - VBAT供电电压
     - 2.4
     - 3.3
     - 4.5
     - V
   * - I/O电源电压
     - -
     - 3.3
     - -
     - V
   * - VDDIO
     - -
     - 3.3
     - -
     - V
   * - 工作温度
     - -40
     - -
     - 85
     - ℃
   * - 存储温度
     - -65
     - -
     - 150
     - ℃

关键功能引脚
~~~~~~~~~~~~~~~~
- MUTE：P5引脚（PE0），高电平触发静音
- UART：P3（Tx/PE7）、P4（Rx/PE6）
- 音频输出：P1（VCMBU/音频负端，差分输出时有效）、P17（DACR/右声道）、P18（DACL/左声道）
- FM天线：P2（FM_ANT）
- SD卡：P13（SDDAT/PA7）、P14（SDCLK/PA6）、P15（SDCMD/PA5）
- MIC输入：P16（MICIN/PF2）
- 电源输入：P8（VBAT）、P6（VUSB，使用内置充电时需串1R电阻+对地10uF滤波电容）
- 复位：P10（PWRKEY），10S拉低触发软开/关机
- 电源输出：P7（VDDIO）